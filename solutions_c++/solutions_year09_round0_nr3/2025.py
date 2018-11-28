#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

char wel[20];
char Praw[501];
char P[501];
int  LP[19];
int  match;
long unsigned int match2;

void init()
{
	for(int i=0;i<19;i++)
	{
		LP[i]=-1;
	}	
	gets(Praw);
	
	int tcounter = 0;
	for(int k=0;Praw[k]!='\0';k++)
	{
		if( Praw[k]=='w' || Praw[k]=='e' || Praw[k]=='l' || Praw[k]=='c' || Praw[k]=='o' || Praw[k]=='m' || Praw[k]==' ' || Praw[k]=='t' || Praw[k]=='d' || Praw[k]=='j' || Praw[k]=='a')
		{
			P[tcounter] = Praw[k];
			tcounter ++;
		}
	}
	P[tcounter]='\0';
	
	match = 0;
	match2 =0;
}
void solve()
{
	int cc   = 0;
	int esci = 0;
	while(esci==0){
		int sc;
		for(sc=LP[cc]+1; P[sc]!=wel[cc] && P[sc]!='\0'; sc++){}
		if(P[sc]=='\0')
		{
			if(cc==0)
			{
				esci = 1;
			}else
			{
				LP[cc] = LP[cc-1];
				cc --;
			}
		}else
		{
			LP[cc]=sc;
			cc ++;
			if(cc==19){
				match ++;
				if(match==10000)
				{
					match=0;
				}
				cc --;
			}else{
				LP[cc] = sc;
			}
		}
	}

}


/*
 for(int aa=0;aa<19;aa++)
 {
 printf("%c",P[LP[aa]]);
 }
 printf("--");
 for(int aa=0;aa<19;aa++)
 {
 printf("%d,",LP[aa]);
 }
 printf("\n");
*/

int main()
{
	strcpy(wel,"welcome to code jam");
	//	freopen("..\\A.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	//	freopen("..\\A-small-attempt1.in","r",stdin);freopen("..\\A-small-attempt1.out","w",stdout);
	//  freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	
	int testcase;
	scanf("%d\n",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		
		init();
		solve();
		printf("Case #%d: %04d",caseId,match);
		if(caseId+1<=testcase)
		{
			printf("\n");
		}
		
		fflush(stdout);
	}
	return 0;
}

//ENDSOURCECODE_BY_ACRUSH_TOPCODER

