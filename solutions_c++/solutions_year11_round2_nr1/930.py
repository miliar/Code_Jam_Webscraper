#include <cstdio>
#include <cstring>

int N;
char st[200];
char arg[200][200];
int count[200];
double wp[200],owp[200],oowp[200];

void solve(){
	memset( wp , 0 , sizeof( wp ));
	memset( owp, 0 , sizeof( owp));
	memset( oowp, 0 , sizeof( oowp));
	scanf("%d",&N);
	gets(st);
	for( int i = 0; i < N ; ++i ){
		gets(arg[i]);
	}
	for( int i = 0 ; i < N ; ++i ){
		count[i] = 0;
		wp[i] = 0;
		for( int j = 0 ; j < N ; ++j ){
			if( arg[i][j] == '.' ) continue;
			count[i]++;
			if( arg[i][j] == '1' ) wp[i]++;
		}
		wp[i] /= count[i];
	}
	for( int i = 0 ; i < N ; ++i ){
		owp[i] = 0;
		for( int j = 0 ; j < N ; ++j ){
			if( arg[i][j] == '.' ) continue;
			if( arg[i][j] == '1' ){
				owp[i] += wp[j]*count[j] / (count[j] - 1);
			}else owp[i] += (wp[j]*count[j]-1)/(count[j]-1);
		}
		owp[i] /= count[i];
	}
	for( int i = 0 ; i < N ; ++i ){
		oowp[i] = 0;
		for( int j = 0 ; j < N ; ++j ){
			if( arg[i][j] == '.' ) continue;
			oowp[i] += owp[j];
		}
		oowp[i] /= count[i];
	}
	for( int i = 0 ; i < N ; ++i ){
		double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i];
		//printf("%f %f %f\n",wp[i],owp[i],oowp[i]);
		printf("%.10f\n",rpi);
	}
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for( int i = 1; i <= T ; ++i ){
		printf("Case #%d:\n",i);
		solve();
	}
}