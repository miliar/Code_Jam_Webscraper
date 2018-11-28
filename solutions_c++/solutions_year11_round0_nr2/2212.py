#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

vector <char> mc[3], md[3];
char s[100000], str[105], ans[105];
int c, d, n, anssh;

char c_pair(char c1, char c2){
	for (int i = 0;i < c;i++){
		if (((mc[0][i] == c1) && (mc[1][i] == c2)) || 
			((mc[0][i] == c2) && (mc[1][i] == c1))){
				return mc[2][i];
		}
	}
	return '-';
}

bool d_pair(char c1, char c2){
	for (int i = 0;i < d;i++){
		if (((md[0][i] == c1) && (md[1][i] == c2)) || 
			((md[0][i] == c2) && (md[1][i] == c1))){
				return true;
		}
	}
	return false;
}

void game(int sh){
	if (sh == n){
		return ;
	}
	ans[anssh] = str[sh];
	anssh++;
	if (anssh == 1){
		game(sh + 1);
	}else
	{
		if (c_pair(ans[anssh - 1], ans[anssh - 2]) != '-'){
			ans[anssh - 2] = c_pair(ans[anssh - 1], ans[anssh - 2]);
			anssh--;
			game(sh + 1);
		}else
		{
			for (int i = 0;i < anssh - 1;i++){
				if (d_pair(ans[anssh - 1], ans[i])){
					anssh = 0;
					break;
				}
			}
			game(sh + 1);
		}
	}
}

bool isnumber(char _c){
	return ((_c > '0' - 1) && (_c < '9' + 1));
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, j, k, len;
	scanf("%d\n",&test);
	for (t = 0;t < test;t++){
		gets(s);
		for (i = 0;i < 3;i++)
			mc[i].clear();
		for (i = 0;i < 2;i++)
			md[i].clear();
		len = strlen(s);
		i = 0;
		/* read combining pairs */
		c = 0;
		while (isnumber(s[i])){
			c = c * 10 + (s[i] - '0');
			i++;
		}
		for (j = 0;j < c;j++){
			while (s[i] == ' '){
				i++;
			}
			for (k = 0;k < 3;k++){
				mc[k].push_back(s[i + k]);
			}
			i += 3;
		}
		while (s[i] == ' '){
			i++;
		}
		/* read deleting pairs */
		d = 0;
		while (isnumber(s[i])){
			d = d * 10 + (s[i] - '0');
			i++;
		}
		for (j = 0;j < d;j++){
			while (s[i] == ' '){
				i++;
			}
			for (k = 0;k < 2;k++){
				md[k].push_back(s[i + k]);
			}
			i += 2;
		}
		/* read invoking elements */
		while (s[i] == ' '){
			i++;
		}
		n = 0;
		while (isnumber(s[i])){
			n = n * 10 + (s[i] - '0');
			i++;
		}
		while (s[i] == ' '){
			i++;
		}
		for (j = 0;j < n;j++){
			str[j] = s[i + j];
		}
		/* end of the input */
		anssh = 0;
		game(0);
		if (t)
			printf("\n");
		printf("Case #%d: [",t + 1);
		for (i = 0;i < anssh - 1;i++){
			printf("%c, ",ans[i]);
		}
		if (anssh){
			printf("%c",ans[anssh - 1]);
		}
		printf("]");
	}
	return 0;
}