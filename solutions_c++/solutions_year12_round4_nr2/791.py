//B
#include<iostream>
#include<cmath>
#include<time.h>
using namespace std;
#define N 10005
struct point{
	double x,y;
}p[N];
int r[N],W,L,n;
double dist(point a,point b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
int check(point a,int k)
{
	if(a.x>W) return 0;
	if(a.y>L) return 0;
	for(int j=0;j<k;j++)
	{
		if(dist(p[j],a)<r[j]+r[k]) return 0;
	}
	return 1;
}
void getP(int k)
{
	point P;
	for(int i=0;i<k;i++)
	{
		P.x=p[i].x+r[i]+r[k];
		P.y=p[i].y;
		if(check(P,k)) {p[k]=P;return;}
		P.x=p[i].x;
		P.y=p[i].y+r[i]+r[k];
		if(check(P,k)) {p[k]=P;return;}	
	}
	do{
		P.x=double(int(10*W*rand()/(RAND_MAX)))/10;
		P.y=double(int(10*L*rand()/(RAND_MAX)))/10;
		//cout<<P.x<<" "<<P.y<<endl;
	}while(check(P,k)==0);
	p[k]=P;
}
int main(){
	int T;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	cin>>T;
	srand((int)time(0));
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>n>>W>>L;
		for(int i=0;i<n;i++)
			scanf("%d",&r[i]);
		cout<<"Case #"<<cnt<<": ";
		p[0].x=0;
		p[0].y=0;
		for(int i=1;i<n;i++) getP(i);
		for(int i=0;i<n;i++)
		{
			printf(" %.1lf %.1lf",p[i].x,p[i].y);
		}
		cout<<endl;
	}
	return 0;
}
