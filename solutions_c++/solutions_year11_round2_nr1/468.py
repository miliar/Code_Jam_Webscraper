#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#pragma comment(linker, "/STACK:167767260")
typedef long long ll;
const int INF = 1000000000;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define pb push_back 
#define mp make_pair
using namespace std;
int tes,o,i,j,n,l,k1[101],k2[101];
char a[101][101];
double wp[101],owp[101],oowp[101],ss,uns[101];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	cin>>tes;
	FOR(o,1,tes)
	{
		cin>>n;
		FOR(i,1,n)
			FOR(j,1,n)
			cin>>a[i][j];

		FOR(i,1,n)
		{
			wp[i]=0;
			k1[i]=0;k2[i]=0;
			FOR(j,1,n)if(a[i][j]=='1'){k1[i]++;k2[i]++;}else if(a[i][j]=='0')k1[i]++;

			//cout<<k1[i]<<" "<<k2[i]<<endl;

			wp[i]=double(k2[i])/double(k1[i]);
		}

		FOR(i,1,n)
		{
			owp[i]=0;
			ss=0;
			l=0;
			FOR(j,1,n)
				if(a[i][j]!='.')
				{
					l++;
					if(a[i][j]=='1')
					{
						ss+=double(k2[j])/double(k1[j]-1);
					}else
					{
						ss+=double(k2[j]-1)/double(k1[j]-1);
					}
				}
			owp[i]=ss/double(l);
		}

		FOR(i,1,n)
		{
			oowp[i]=0;
			ss=0;
			l=0;
			FOR(j,1,n)
				if(a[i][j]!='.')
				{
					ss+=owp[j];l++;
				}
			oowp[i]=ss/double(l);
		}
        // RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
		FOR(i,1,n)
			uns[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];

		cout<<"Case #"<<o<<":"<<endl;
		FOR(i,1,n)printf("%.6f\n",uns[i]);
	}
}