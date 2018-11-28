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

const int MXN = 1010;

int a[MXN];
int n;
int xx;

void test() {
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	sort(a, a + n);
	int x = a[0];
	int sum = 0;
	for(int i = 1; i < n; i++) {
		x ^= a[i];
		sum += a[i];
	}
	printf("Case #%d: ", xx);
	if(x)
		printf("NO\n");
	else
		printf("%d\n", sum);
}

int main() {
	int te;
	scanf("%d", &te);
	for(xx = 1; xx <= te; xx++)
		test();
	return 0;
}

