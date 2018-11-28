#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

const char MAGIC[]="welcome to code jam";
const int MOD=10000;
int wys[22][555];
char S[555];
int L;
int main(){
	int T,tests=0;
	scanf("%d",&T),gets(S);
	while(T--){
		gets(S),L=strlen(S);
		memset(wys,0,sizeof(wys));
		wys[0][0]=1;
		for(int i=0;i<19;i++)
			for(int j=0;j<L;j++)if(wys[i][j])
				for(int k=j;k<L;k++)if(MAGIC[i]==S[k])
					(wys[i+1][k+1]+=wys[i][j])%=MOD;
		int cnt=0;
		for(int i=0;i<=L;i++)
			(cnt+=wys[19][i])%=MOD;
		printf("Case #%d: %04d\n",++tests,cnt);
	}
}
