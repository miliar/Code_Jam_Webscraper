#include <iostream>
#include <cstring>

using namespace std;

const size_t LL = 501;
const size_t Str_Len = 19;
const int Mod = 10000;
char const Str[] = "welcome to code jam";

	
int solve(char s[])
{
	unsigned int re[LL][19];
	memset(re,0,sizeof(re));
	int len = strlen(s);
	for (int i = 1 ;i <= len ;i++){
		if (s[i-1] == Str[0]){
			re[i][0] = re[i-1][0] + 1;
		}else{
			re[i][0] = re[i-1][0];
		}
		re[i][0] %= Mod;
	//	cout << i << ",0->" << re[i][0] << endl;
		for (int j = 1 ;j < Str_Len ;j++){
			if (Str[j] == s[i-1]){
				re[i][j] = re[i-1][j-1]+re[i-1][j];
			}else{
				re[i][j] = re[i-1][j];
			}
			re[i][j] %= Mod;
		//	cout << i << "," << j << "->" << re[i][j] << endl;
		}
	}
	return re[len][18];
}
int main()
{
//	freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	int n;
	scanf("%d\n",&n);
	char s[LL];
	for (int i = 0 ;i < n ;i++){
		int start = 0;
		char ch;
		while ((ch=getchar())!='\n'){
			s[start++] = ch;
		}
		s[start++] = 0;
		printf("Case #%d: %04d\n",i+1,solve(s));
	}
}
