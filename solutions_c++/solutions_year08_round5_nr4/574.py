#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<queue>

using namespace std;

typedef long long LL;

#define FT first
#define SD second
#define MP make_pair
#define PB push_back

int T;
int ca;
int h,w,nr;
int b[110][110];
bool k[110][110];
int r[20][2];

int main(){
	scanf("%d",&T);
	ca=0;
	while(T--){
		ca++;
		scanf("%d %d %d",&h,&w,&nr);
		for(int i=0;i<nr;i++){
			scanf("%d %d",&r[i][0],&r[i][1]);
			k[r[i][0]+1][r[i][1]+1]=1;
		}
		b[2][2]=1;
		for(int i=0;i<h;i++){
			for(int j=1;j<w;j++){
				b[i+2][j+2]=0;
				if(k[i+2][j+2]) continue;
				b[i+2][j+2]+=b[i+1][j];
				b[i+2][j+2]+=b[i][j+1];
				b[i+2][j+2]%=10007;
			}
		}
		printf("Case #%d: %d\n",ca,b[h+1][w+1]);
		for(int i=0;i<nr;i++){
			k[r[i][0]+1][r[i][1]+1]=0;
		}
	}
	return 0;
}

