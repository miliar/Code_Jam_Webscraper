#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<queue>

using namespace std;

#define MP make_pair
#define PB push_back
#define FT first
#define SD second


int test;
long long n,m,a,b,c,d,x0,y0;
long long x,y;
long long tab[3][3];
long long ile=0LL;
int ca=0;

int main(){
	scanf("%d",&test);
	while(test--){
		ca++;
		ile=0LL;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&a,&b,&c,&d,&x0,&y0,&m);
		x=x0;
		y=y0;
		for(int i=0;i<3;i++){
			for(int j=0;j<3;j++){
				tab[i][j]=0;
			}
		}
		for(int i=0;i<n;i++){
			//printf("%lld %lld\n",x,y);
			tab[x%3][y%3]++;
			x=(a*x+b) % m;
			y=(c*y+d) % m;
		}
		ile+=tab[0][0]*(tab[0][0]-1LL)*(tab[0][0]-2LL)/6LL;
		ile+=tab[0][1]*(tab[0][1]-1LL)*(tab[0][1]-2LL)/6LL;
		ile+=tab[0][2]*(tab[0][2]-1LL)*(tab[0][2]-2LL)/6LL;
		ile+=tab[1][0]*(tab[1][0]-1LL)*(tab[1][0]-2LL)/6LL;
		ile+=tab[1][1]*(tab[1][1]-1LL)*(tab[1][1]-2LL)/6LL;
		ile+=tab[1][2]*(tab[1][2]-1LL)*(tab[1][2]-2LL)/6LL;
		ile+=tab[2][0]*(tab[2][0]-1LL)*(tab[2][0]-2LL)/6LL;
		ile+=tab[2][1]*(tab[2][1]-1LL)*(tab[2][1]-2LL)/6LL;
		ile+=tab[2][2]*(tab[2][2]-1LL)*(tab[2][2]-2LL)/6LL;
		ile+=tab[0][1]*tab[0][2]*tab[0][0];
		ile+=tab[1][1]*tab[1][2]*tab[1][0];
		ile+=tab[2][1]*tab[2][2]*tab[2][0];
		ile+=tab[1][0]*tab[2][0]*tab[0][0];
		ile+=tab[1][1]*tab[2][1]*tab[0][1];
		ile+=tab[1][2]*tab[2][2]*tab[0][2];
		ile+=tab[1][1]*tab[2][2]*tab[0][0];
		ile+=tab[1][1]*tab[2][0]*tab[0][2];
		ile+=tab[1][0]*tab[2][1]*tab[0][2];
		ile+=tab[1][0]*tab[2][2]*tab[0][1];
		ile+=tab[1][2]*tab[2][0]*tab[0][1];
		ile+=tab[1][2]*tab[2][1]*tab[0][0];
		printf("Case #%d: %lld\n",ca,ile);
	}
	return 0;
}

