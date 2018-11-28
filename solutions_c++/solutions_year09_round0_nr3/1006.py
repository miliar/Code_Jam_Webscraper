#include<stdio.h>
#include<string>

using namespace std;

string target = "welcome to code jam";
char str[1009];
int mod = 10000;
int memo[509][30];

int play( int pos, int org){
	if(org == target.size()) return 1;
	if(str[pos] == 0) return 0;

	int &ret = memo[pos][org];
	if(ret != -1) return ret;
	int cur;

	ret = play( pos+1, org);
	if( target[org]==str[pos]){
		cur = play( pos+1, org+1);
		ret = (ret + cur) % mod;
	}

	return ret;
}
int main(){
	int N, x, ret;

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d", &N);
	gets(str);
	for( x= 1; x<=N; ++x){
		gets(str);

		memset( memo, -1,sizeof(memo));
		ret = play(0, 0);
		

		printf("Case #%d: %04d\n", x, ret%mod);
	}

	return 0;
}