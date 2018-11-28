#include <cstdio>
#include <vector>
using namespace std;

vector <int> g[2], m, who;
char s[10000];
int n, l, r, posl, posr, ans;

void game(int sh){
	if (sh == n){
		return ;
	}
	if (who[sh] == 0){
		while (posl != g[0][l]){
			if (posl < g[0][l]){
				posl++;
			}else
			{
				posl--;
			}
			if (posr != g[1][r]){
				if (posr < g[1][r]){
					posr++;
				}else
				{
					posr--;
				}
			}
			ans++;
		}
		if (posr != g[1][r]){
			if (posr < g[1][r]){
				posr++;
			}else
			{
				posr--;
			}
		}
		ans++;
		l++;
		game(sh + 1);
	}else
	{
		while (posr != g[1][r]){
			if (posr < g[1][r]){
				posr++;
			}else
			{
				posr--;
			}
			if (posl != g[0][l]){
				if (posl < g[0][l]){
					posl++;
				}else
				{
					posl--;
				}
			}
			ans++;
		}
		if (posl != g[0][l]){
			if (posl < g[0][l]){
				posl++;
			}else
			{
				posl--;
			}
		}
		ans++;
		r++;
		game(sh + 1);
	}
}

bool isnumber(char c){
	return ((c > '0' - 1) && (c < '9' + 1));
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, j, len, cur, ch;
	scanf("%d\n",&test);
	for (t = 0;t < test;t++){
		gets(s);
		m.clear();who.clear();g[0].clear();g[1].clear();
		len = strlen(s);
		i = 0;
		n = 0;
		while (isnumber(s[i])){
			n = n * 10 + (s[i] - '0');
			i++;
		}
		for (j = 0;j < n;j++){
			while (s[i] == ' '){
				i++;
			}
			if (s[i] == 'B'){
				cur = 0;
			}else
			{
				cur = 1;
			}
			i++;
			while (s[i] == ' '){
				i++;
			}
			ch = 0;
			while ((isnumber(s[i])) && (i < len)){
				ch = ch * 10 + (s[i] - '0');
				i++;
			}
			who.push_back(cur);
			m.push_back(ch);
			g[cur].push_back(ch);
		}
		g[0].push_back(0);g[1].push_back(0);
		l = 0;r = 0;
		posl = 1;posr = 1;
		ans = 0;
		game(0);
		if (t)
			printf("\n");
		printf("Case #%d: %d",t + 1,ans);
	}
	return 0;
}