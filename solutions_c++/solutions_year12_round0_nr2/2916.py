#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define TSTCASE(n) int T=(n); while(T--) 
#define SWAP(a,b,t) {t=a; a=b; b=t;}
          
using namespace std;

int sp2(int,int,int,int);
        
int main()
{
	int T, j=0;
	int a[100], b[100];
	scanf("%d",&T);
	while(j++ < T)
	{
		int  n, s, p, rs=0;
		scanf("%d %d %d",&n,&s,&p);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&(a[i]));
			b[i]=0;
			int l=a[i];
			if(l<p)b[i]=0;
			else {
				int t1=l/3, t2=(l-t1)/2, t3=l-t1-t2;
				//cout <<t1<<" "<<t2<<" "<<t3<<endl;;
				if(t1>=p || t2>=p || t3>=p)
				b[i]=1;
			else if(s>0 && sp2(t1,t2,t3,p)==1){b[i]=1; s--;}
			}
			rs+=b[i];
		}
		printf("Case #%d: %d\n",j,rs);
	}
}

int sp2(int t1, int t2, int t3, int p)
{
	int t;
	if(t1<t2)SWAP(t1,t2,t);
	if(t1<t3)SWAP(t1,t3,t);
	if(t2<t3)SWAP(t2,t3,t);
	if(t1>t2)return 0;
	t1=t1+1;
	t2=t2-1;
	if(t1>=p)return 1;
	return 0;
}
