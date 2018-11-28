#include<cstdio>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<queue>

#define FOR(i,a,b) for(int i=(int)(a); i<(int)(b); ++i)

using namespace std;

const int lMax = 15;
const int dMax = 5000;
const int nMax = 500;

bool canUseLet[nMax][lMax][26];
char tabD[dMax][lMax+2];

char getNextChar()
{
	while(true)
	{
		char c;
		scanf("%c",&c);
		if(c<='z' && c>='a')
			return c;
		if(c=='(' || c==')')
			return c;
	}
}

void testcase(int testNr) {
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	
	FOR(i,0,D)
		scanf("%s", tabD+i);
		
	FOR(i,0,N) {
		FOR(j,0,L) {
			FOR(k,0,26)
				canUseLet[i][j][k] = false;
			char c = getNextChar();
			if(c=='(')
			{
				while(true)
				{
					c = getNextChar();
					if(c==')')
						break;
					else
						canUseLet[i][j][c-'a'] = true;
				}
			}
			else
				canUseLet[i][j][c-'a'] = true;
		}
		int res = 0;
		FOR(k,0,D)
		{
			bool isOk = true;
			FOR(j,0,L) if(!canUseLet[i][j][tabD[k][j]-'a']) {
				isOk = false;
				break;
			}
			if(isOk)
				res++;
		}
		printf("Case #%d: %d\n",i+1,res);
	}
}

int main() {
	testcase(0);
}
