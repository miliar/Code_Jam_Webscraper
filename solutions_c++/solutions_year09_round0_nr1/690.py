// Marcin Wrochna
// g++ -O2
// IDE: geany
#include <cstdio>
#include <cstring>

using namespace std;

#define REP(x,n) for(int x=0; x<(int)(n); ++x)

const int A='z'-'a'+1;
char words[5000][16];
bool pattern[16][A];
char buf[(A+2)*15+1];

int main()
{
	int L,D,N;
	scanf("%d %d %d\n",&L,&D,&N);
	REP(d,D) scanf("%s\n", words[d]);
	REP(n,N)
	{
		scanf("%s\n", buf);
		memset(pattern, false, sizeof(pattern));
		bool inside=false;
		for(int i=0, l=0; buf[i]; i++)
		{
			if(buf[i]=='(') inside=true;
			else if(buf[i]==')')
			{
				l++;
				inside=false;
			}
			else
			{
				pattern[l][buf[i]-'a']=true;
				if(!inside) l++;
			}
		}	
		
		int result = 0;
		REP(d,D)
		{
			bool match = true;
			for(int i=0; words[d][i]; i++)
			{
				if(!pattern[i][words[d][i]-'a'])
				{
					match=false;
					break;
				}
			}
			if(match) result++;
		}
		printf("Case #%d: %d\n", n+1, result);
	}

	return 0;
}
