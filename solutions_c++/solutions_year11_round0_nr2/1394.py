#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#define NONE '\0'
#define MAX_N 128
#define BASE_NUM 8
using namespace std;
int T, C, D, N;
char word[MAX_N];
char combine[26][26];
bool opposed[26][26];
int appeared[26];
int s;
char list[MAX_N];
void print(){
	printf("[");
	for(int i=0;i<s;++i){
		printf("%c%s", list[i], i == s-1 ? "": ", ");
	}
	printf("]");
}
void solve(){
	char last = word[0], curr;
	memset(appeared, 0, sizeof(appeared));
	list[0] = last;
	s = 1;
	appeared[last-'A'] = 1;
	for(int i=1;i<N;++i){
		bool cleared = false;
		curr = word[i];
		if(last != '?' && combine[last-'A'][curr-'A'] != NONE){
			--s;
			curr = combine[last-'A'][curr-'A'];
			appeared[last-'A'] -= 1;
		}
		appeared[curr-'A'] += 1;
		for(int j=0;j<26;++j){
			for(int k=j;k<26;++k){
				if(appeared[j] > 0 && appeared[k] > 0 && opposed[j][k]){
					cleared = true;
				}
			}
		}
		if(cleared){
			s = 0;
			memset(appeared, 0, sizeof(appeared));
			last = '?';
		}
		else{
			list[s] = curr;
			s = s + 1;
			last = curr;
		}
	}
}
int main(){
	char str[16];
	int c1, c2;
	scanf("%d", &T);
	for(int t=1;t<=T;++t){
		memset(combine, NONE, sizeof(combine));
		memset(opposed, 0, sizeof(opposed));

		scanf("%d", &C);
		for(int i=0;i<C;++i){
			scanf("%s", str);
			c1 = str[0] - 'A'; c2 = str[1] - 'A';
			combine[c1][c2] = combine[c2][c1] = str[2]; 
		}
		scanf("%d", &D);
		for(int i=0;i<D;++i){
			scanf("%s", str);
			c1 = str[0] - 'A'; c2 = str[1] - 'A';
			opposed[c1][c2] = opposed[c2][c1] = true;
		}
		scanf("%d%s", &N, word);

		solve();
		printf("Case #%d: ", t);
		print();
		printf("\n");
	}
	return 0;
}
