#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#define MAX_N 5005
#define MAX_L 17
using namespace std;
char word[MAX_N][MAX_L];
char tar[30*MAX_L];
int f[MAX_L][MAX_N];
vector<char> div_w[MAX_L];
int flag[MAX_L][30];
int L, D, n;
int solve()
{
	memset(flag,0,sizeof(flag));
	for(int i = 0; i < L; i++ ){
		for(int j = 0; j < div_w[i].size();j++){
			flag[i][div_w[i][j]-'a'] = 1;
		}
	}	
	for(int i = 0; i < L; i++){
		for(int j = 0; j < D; j++){
			f[i][j] = 0;
		}		
	}
	for(int i = 0; i < D; i++){
		f[0][i] = flag[0][word[i][0]-'a'];	
	}
	for(int i = 1; i < L; i++ ){
		for(int j = 0; j < D; j++ ){
			if(f[i-1][j] && flag[i][word[j][i]-'a'])f[i][j] = 1;
		}
	}
	int ans = 0;
	for(int i = 0; i < D; i++){
		if(f[L-1][i]){
			ans++;
		}
	}
	return ans;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d", &L, &D, &n);
	for(int i=0; i < D; i++){
		scanf("%s",word[i]);
	}
	for(int i=1; i <= n; i++){
		scanf("%s", tar);
		for(int j = 0; j < L; j++)div_w[j].clear();
		int len=strlen(tar);
		int k=0;
		for(int j=0; j < len;j++){
			if(tar[j] <= 'z' && tar[j] >= 'a' ){
				div_w[k++].push_back(tar[j]);
				continue;
			}else{
				j++;
				for(; j < len && tar[j] <= 'z' && tar[j] >= 'a'; j++)
				{
					div_w[k].push_back(tar[j]);
				} 
				k++;
			}
		}
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
