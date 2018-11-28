#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#pragma comment(linker, "/STACK:167767260")
typedef long long ll;
const int INF = 1000000000;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define FORN(i,a,b) for(i=a;i>=b;i--)
#define pb push_back 
#define mp make_pair
using namespace std;
int tes,o,i,j,n,m,D,uns,ii,jj,p,q,k;
char c;
int a[501][501];
double xx,yy,s1,s2;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tes;
	FOR(o,1,tes)
	{
		scanf("%d %d %d",&n,&m,&D);

		FOR(i,1,n)
			FOR(j,1,m){cin>>c;a[i][j]=int(c)-48;}

		int nn=min(n,m);

		uns=-1;

		FORN(k,nn,3)
		{
			FOR(i,1,n-k+1)
				FOR(j,1,m-k+1)
			    {
					xx=0;s1=0;s2=0;
					yy=0;
					ii=i+k-1;
					jj=j+k-1;

					//cout<<i<<" "<<j<<" "<<ii<<" "<<jj<<endl;

					FOR(p,i,ii)
						FOR(q,j,jj)
						if((p==i && q==j)||(p==ii && q==jj)||(p==i && q==jj)||(p==ii && q==j)){}else
						{
							xx+=p*a[p][q];
							yy+=q*a[p][q];
							s1+=a[p][q];
							s2+=a[p][q];
						}
					

			//cout<<xx<<" "<<yy<<endl;
			if(2*xx==s1*(i+ii) && 2*yy==s1*(j+jj))
			{uns=k;}
			    }
		    
			 if(uns!=-1)break;

			
		}

		if(uns==-1)printf("Case #%d: IMPOSSIBLE\n",o);else
		printf("Case #%d: %d\n",o,uns);
	}
}