#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
//#include <ctime>
//#include <fstream>
using namespace std;

#define INF 1000000000
#define PI acos(-1.0)
#define MP make_pair
const double EPS=1e-8;

int a[10][10];

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	cin>>tt;
	for (int T=1; T<=tt; T++){
		
		int n,m,d;
		cin>>n>>m>>d;

		for (int i=0; i<n; i++){
			for (int j=0; j<m; j++){
				char c;
				cin>>c;
				a[i][j]=c-'0';
			}
		}

		int res=0;

		for (int k=3; k<=min(n,m); k++){

			double X=0,Y=0;

			for (int ln=0; ln<=n-k; ln++){
				for (int lm=0; lm<=m-k; lm++){

					int S=0;

					X=Y=0;

					for (int i=0; i<k; i++){
						for (int j=0; j<k; j++){
							X+=(a[i+ln][j+lm]+d)*(i);
							Y+=(a[i+ln][j+lm]+d)*(j);

							S+=a[i+ln][j+lm]+d;
						}
					}

					X-=(d+a[ln][lm])*0;
					X-=(d+a[ln][lm+k-1])*0;
					X-=(d+a[ln+k-1][lm])*(k-1);
					X-=(d+a[ln+k-1][lm+k-1])*(k-1);

					Y-=(d+a[ln][lm])*0;
					Y-=(d+a[ln][lm+k-1])*(k-1);
					Y-=(d+a[ln+k-1][lm])*0;
					Y-=(d+a[ln+k-1][lm+k-1])*(k-1);

					S-=(d+a[ln][lm]);
					S-=(d+a[ln][lm+k-1]);
					S-=(d+a[ln+k-1][lm]);
					S-=(d+a[ln+k-1][lm+k-1]);

					X/=(double)S;
					Y/=(double)S;

					X*=2.0;
					Y*=2.0;
					if (fabs(X-(k-1))<EPS && fabs(Y-(k-1))<EPS) res=k;

				}
			}
		}

		cout<<"Case #"<<T<<": ";
		if (res==0) cout<<"IMPOSSIBLE"<<endl;
		else cout<<res<<endl;

	}


} 