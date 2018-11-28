#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MAX = 505;
const int M = 10000;

char sstd[25] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
char ch[MAX];
int c[MAX];
int lit[MAX];


int lowbit(int t)
{
	return t 
		& (-t);
}

void insert(int i, int val, int n)
{
	while(i < n){
		c[i] += val;
		c[i] %= M;
		i += lowbit(i);
	}
}

int getsum(int i)
{
	int res = 0;
	while(i > 0){
		res += c[i];
		res %= M;
		i -= lowbit(i);
	}
	return res;
}




int go()
{
	int i, j;
	memset(lit, 0, sizeof(lit));
	int lens = strlen(sstd);
	int len = strlen(ch);
	for(i = 0; i < len; i++){
		if(ch[i] == 'w')  lit[i] = 1;
		else  lit[i] = 0;
	}
	//printf("lens = %d\n", len);
	for(i = 1; i < lens; i++){
		memset(c, 0, sizeof(c));
		for(j = 0; j < len; j++){
			//printf("@%d ", lit[j]);
			insert(j + 1, lit[j], len);
			if(ch[j] != sstd[i])  lit[j] = 0;
			else  lit[j] = getsum(j);
		}
	}
	int res = 0;
	for(i = 0; i < len; i++){
		res += lit[i];
		res %= M;
	}
	return res;
}



int main()
{
	int T, cnt = 0;
	freopen("f://C-large.in", "r", stdin);
	freopen("f://C-large.out", "w", stdout);
	scanf("%d\n", &T);
	while(T--){
		cnt++;
		int i, j;
		gets(ch);
		//scanf("%s", ch + 1);
		printf("Case #%d: %04d\n", cnt, go());
	}
}