
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAXN 1010
#define LOOP 1000

struct node{
	double e;
	int index,p;
	bool g;
};

double p[MAXN];
int l[MAXN],p_[MAXN];
int n;
node info[ MAXN ];


void init(){
	cin>>n;
	for (int i=1;i<=n;i++){
		cin>>l[i];
		info[i].index=i-1;
	}
	for (int i=1;i<=n;i++){
		cin>>p_[i];
		p[i]=p_[i]/100.0;
		info[i].p=p_[i];
		if (p_[i]==0)
			info[i].g=1;
		else
			info[i].g=0;
	}
}

bool cmp( node x,node y){
	if (x.g!=y.g)
		return (x.g<y.g);
	if (x.g==0)
		return x.e < y.e;
	return x.index<y.index;
}

void cal(){
	int i,j;
	double b;

	for (i=1;i<=n;i++)
		if (info[i].g==0){
			b=1-p[i];
			info[i].e=l[i]*(1-p[i]);
			for (j=2;j<=LOOP;j++){
				b=b*(1-p[i]);
				info[i].e+=b*j*l[i];
			}
		}
	sort(info+1,info+n+1,cmp);
	for (i=1;i<n;i++){
		cout <<info[i].index<<" ";
	}
	cout<<info[n].index<<endl;
}

bool cmp1(node x,node y){
	if (x.p!=y.p)
		return x.p>y.p;
	return x.index<y.index;
}

void cal1(){
	sort(info+1,info+n+1,cmp1);
	for (int i=1;i<n;i++){
		cout <<info[i].index<<" ";
	}
	cout<<info[n].index<<endl;
}

int main()
{
	freopen("ii.txt","r",stdin );
	//freopen( "ao.txt","w",stdout );
	int t,i;
	scanf("%d\n",&t );
	for (i=1;i<=t;i++ ){
		init();
		cout<<"Case #"<<i<<": ";
		cal1();
	}
	return 0;
}

