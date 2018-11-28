#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<list>
#include<string>
#include<cstring>

using namespace std;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) (int)(x).size()
#define SORT(x) sort((x).begin(),(x).end())
#define CLEAR(tab) memset(tab, 0, sizeof(tab))

/*
const int MAX_BUF_SIZE = 16384;
char BUFOR[MAX_BUF_SIZE];
int BUF_SIZE, BUF_POS;
char ZZZ;
#define GET(ZZZ){ZZZ='a';if(BUF_POS<BUF_SIZE)ZZZ=BUFOR[BUF_POS++];\
else if(!feof(stdin)){BUF_SIZE=fread(BUFOR,1,MAX_BUF_SIZE,stdin);\
ZZZ=BUFOR[0];BUF_POS=1;}}
#define GETINT(WW){do{GET(ZZZ);}while(!isdigit(ZZZ));WW=ZZZ-'0';\
while(1){GET(ZZZ);if(!isdigit(ZZZ))break;WW=WW*10+(ZZZ-'0');}}
*/
//FAST IO

typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MXN = 110;

int a[MXN];
int n;
int xx;

int s[MXN], ss;
char zmien[MXN][MXN];
int jest[300];

char x1[MXN], x2[MXN];

int c, d, l;

void test() {
	scanf("%d", &c);
	for(int i = 0; i < c; i++) {
		char a[3];
		for(int j = 0; j < 3; j++) {
			char z;
			while(1) {
				z = getchar();
				if(isalpha(z))
					break;
			}
			a[j] = z;
		}
		zmien[a[0]][a[1]] = a[2];
		//cout<<a[0]<<" "<<a[1]<<" "<<a[2]<<endl;
	}
	scanf("%d", &d);
	for(int i = 0; i < d; i++) {
		char a[2];
		for(int j = 0; j < 2; j++) {
			char z;
			while(1) {
				z = getchar();
				if(isalpha(z))
					break;
			}
			a[j] = z;
		}
		x1[i] = a[0];
		x2[i] = a[1];
		//cout<<a[0]<<" "<<a[1]<<endl;
	}
	scanf("%d ", &l);
	//cout<<c<<" "<<d<<" "<<l<<endl;
	char a[MXN];
	scanf("%s", a);
	//cout<<a<<endl;
	jest[a[0]]++;
	s[ss++] = a[0];
	for(int i = 1; i < l; i++) {
		bool dec = 1;
		if(ss && zmien[s[ss - 1]][a[i]]) {
			jest[s[ss - 1]] -= 1;
			s[ss - 1] = zmien[s[ss - 1]][a[i]];
			dec = 0;
			jest[s[ss - 1]]++;
		}
		else if(ss && zmien[a[i]][s[ss - 1]]) {
			jest[s[ss - 1]]-= 1;
			s[ss - 1] = zmien[a[i]][s[ss - 1]];
			dec = 0;
			jest[s[ss - 1]]++;
		}
		if(ss && dec) {
			for(int j = 0; j < d; j++)
				if(a[i] == x2[j] && jest[x1[j]]) {
					ss = 0;
					CLEAR(jest);
					dec = 0;
					break;
				}
				else if(a[i] == x1[j] && jest[x2[j]]) {
					ss = 0;
					CLEAR(jest);
					dec = 0;
					break;
				}
		}
		if(dec) {
			s[ss++] = a[i];
			jest[a[i]]++;
		}
	}

	printf("Case #%d: \[", xx);
	for(int i = 0; i < ss; i++) {
		printf("%c", s[i]);
		if(i < ss - 1)
			printf(", ");
	}
	printf("\]\n");
	ss = 0;
	for(int i = 'A'; i <= 'Z'; i++)
	for(int j = 'A'; j <= 'Z'; j++)
		zmien[i][j] = 0;
	CLEAR(jest);
}

int main() {
	int te;
	scanf("%d", &te);
	for(xx = 1; xx <= te; xx++)
		test();
	return 0;
}

