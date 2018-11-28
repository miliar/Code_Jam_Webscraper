#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<time.h>
#include<math.h>
using namespace std;
int s[2000],n,w,l;
int bigr(){
	return rand()*10000+rand()%10000;
}
class nod{
	public:
	int id, r;
	double x, y;
	bool operator<(nod d)const{
		return r<d.r;
	}
}p[2000];
double x[2000],y[2000];
int cmp(nod a, nod b){
	return a.id<b.id;
}
int main(void){
	int t;
	srand(time(0));
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		scanf("%d%d%d",&n,&w,&l);
		for(int i=0;i<n;i++){
			scanf("%d",&p[i].r);
			p[i].id=i;
		}
		sort(p,p+n);
		for(int i=n-1;i>=0 && i>=n-2;i--){
			x[i]=(i==n-1?0:w);
			y[i]=(i==n-1?0:l);
		}
		for(int i=n-3;i>=0;i--){
			while(1){
				double xi = bigr()%(w);
				double yi = bigr()%(l);
				int j;
				for(j=n-1;j>i;j--)
					if(pow(xi-x[j],2)+pow(yi-y[j],2)<pow(p[i].r+p[j].r,2))
						break;
				if(j>i)
					continue;
				x[i]=xi;
				y[i]=yi;
				break;
			}
		}
		for(int i=0;i<n;i++)
		{
			p[i].x = x[i];
			p[i].y = y[i];
		}
		sort(p,p+n,cmp);
		printf("Case #%d:", tt);
		for(int i=0;i<n;i++)
			printf(" %lf %lf", p[i].x,p[i].y);
		puts("");
	}
	return 0;
}
