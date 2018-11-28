//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long
#define CLR(x) memset(x,0,sizeof x)
#define SET(x,y) memset(x,y,sizeof x)


#define mx 1100

char g[200][200];
double w[200],ow[200],oow[200];
int cn[200],mt[200];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.OUT","w",stdout);
	int i,j,k,n,I,T;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n;
		for(i=0;i<n;i++) {
			cin>>g[i];
			w[i]=ow[i]=oow[i]=0;
			cn[i]=mt[i]=0;
		}
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				if(i!=j && g[i][j]=='1') cn[i]++;
				if(g[i][j]!='.') mt[i]++;
			}
			w[i]=double(cn[i])/(mt[i]);
		}
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) if(i!=j && g[i][j]!='.') {
				if(g[i][j]=='1') {
					ow[i]+=double(cn[j])/(mt[j]-1);
				}
				else {
					ow[i]+=double(cn[j]-1)/(mt[j]-1);
				}
			}
			ow[i]/=(mt[i]);
		}
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) if(i!=j && g[i][j]!='.') {
				oow[i]+=ow[j];
			}
			oow[i]/=(mt[i]);
		}
		cout<<"Case #"<<I<<":\n";
		for(i=0;i<n;i++) {
			//cout<<i<<' '<<cn[i]<<' '<<mt[i]<<' '<<w[i]<<' '<<ow[i]<<' '<<oow[i]<<'\n';
			printf("%.9lf\n",0.25 * w[i] + 0.50 * ow[i] + 0.25 * oow[i]);
		}
	}
	return 0;
}

