//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, to) for(int i = 0; i<to; ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
typedef long long ll;
typedef pair<ll, ll> pii;

int sum, x, men, N, a,t;
char line[111][111];
pii wp[111][111];
//pii owp[111];
//pii oowp[111];
long double owp[111], oowp[111];

/*void simple(pii &zlomok){
	ll g = __gcd(zlomok.first, zlomok.second);
	if (g==0) return;
	zlomok.first/=g;
	zlomok.second/=g;
	
}

pii sum(pii z1, pii z2){
	pii z;
	z.first = z1.first*s2.second+z2.first*z2.second
	
}*/

int main(){
	scanf("%d", &t);
	For(T,t){
		scanf("%d", &N);
		For(i, N) scanf("%s",line[i]);
		For(i, N){
			int c = 0;
			int sum = 0;
			For(j, N){
				if (line[i][j]=='.') continue;
				c++;
				sum+=(line[i][j]=='1');
			}
			wp[i][i].first = sum;
			wp[i][i].second = c;
			For(j, N){
				if (line[i][j]=='.') continue;
				wp[i][j].first = sum-(line[i][j]=='1');
				wp[i][j].second = c-1;
			}
		}
		For(i, N){
			long double sum = 0.0;
			int c = 0;
			For(j, N){
				if (line[i][j]=='.') continue;
				c++;
				sum+=(long double)(wp[j][i].first)/(long double)(wp[j][i].second);
			}
			owp[i] = sum/c;
		}
		For(i, N){
			long double sum = 0.0;
			int c = 0;
			For(j, N){
				if (line[i][j]=='.') continue;
				c++;
				sum+=owp[j];
			}
			oowp[i] = sum/c;
		}
				
		printf("Case #%d:\n",T+1);
		For(i,N){
			printf("%.11Lf\n", (long double)(wp[i][i].first)/wp[i][i].second*0.25 + owp[i]*0.5 + oowp[i]*0.25);
		}
	}
	
}