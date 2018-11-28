#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <map>
#include <stack>

#define fi first
#define se second
#define mp make_pair
#define ll long long
#define pii pair <int, int>
#define vi vector <int>
#define REP(a,b) for(int a = 0; a < b; ++a)
#define FORU(a,b,c) for(int a = b; a <= c; ++a)
#define FORD(a,b,c) for(int a = b; a >= c; ganti[2] =ganti[2] =a)
#define MOD 1000000000
#define MODLL 1000000000LL
#define INF 2123123123
#define pb push_back
using namespace std;

int main()
{
	int T;
	char ganti[27], st[105];
	
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	
	ganti[0] = 'y';  ganti[1] = 'h';
	ganti[2] = 'e';	 ganti[3] = 's';
	ganti[4] = 'o';	 ganti[5] = 'c';
	ganti[6] = 'v';	 ganti[7] = 'x';
	ganti[8] = 'd';	 ganti[9] = 'u';
	ganti[10] = 'i'; ganti[11] = 'g';
	ganti[12] = 'l'; ganti[13] = 'b';
	ganti[14] = 'k'; ganti[15] = 'r';
	ganti[16] = 'z'; ganti[17] = 't';
	ganti[18] = 'n'; ganti[19] = 'w';
	ganti[20] = 'j'; ganti[21] = 'p';
	ganti[22] = 'f'; ganti[23] = 'm';
	ganti[24] = 'a'; ganti[25] = 'q';
	
	scanf("%d", &T);
	gets(st);
	
	FORU(tc, 1, T) {
		gets(st);
		
		printf("Case #%d: ", tc);
		
		for (int i = 0; st[i] != '\0'; ++i)
			if (st[i] != ' ')
				printf("%c", ganti[st[i]-'a']);
			else
				printf(" ");
		
		printf("\n");
	}
	
	return 0;
}
