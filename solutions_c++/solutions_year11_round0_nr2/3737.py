#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

char C[33][33],O[33];
int vis[105];
char s[105];

int main()
{
    freopen ("B.in","r",stdin);
    freopen ("B.out","w",stdout);
    
    int i,j,k=0,T;
    
    scanf("%d",&T);
    
    char c[5];
    
    while(T--)
    {
		k++;
		string ret="";
		
		fo(i,33){O[i]='#';fo(j,33)C[i][j]='#';}
		memset(vis,0,sizeof vis);
		
		int CC,DD,N;
		scanf("%d",&CC);
		fo(i,CC)
		{
			scanf("%s",c);
			C[c[0]-'A'][c[1]-'A']=c[2];
			C[c[1]-'A'][c[0]-'A']=c[2];
		}
		scanf("%d",&DD);
		
		fo(i,DD)
		{
			scanf("%s",c);
			O[c[0]-'A']=c[1];
			O[c[1]-'A']=c[0];
		}
		
		scanf("%d",&N);
		
		scanf("%s",s);
		
		fo(i,N)
		{
			ret+=s[i];
			
			int M=ret.sz;
			
			if(M>=2)
			{
				if(C[ret[M-1]-'A'][ret[M-2]-'A']!='#')
				{
					//printf("\ndone1 %s %c\n",ret.c_str(),C[ret[M-1]-'A'][ret[M-2]-'A']);
					char g=C[ret[M-1]-'A'][ret[M-2]-'A'];
					vis[ret[M-2]-'A']--;
					
					ret=ret.substr(0,M-2);
					ret+=g;
					//printf("\ndone1 %s\n",ret.c_str());
				}
				else if(O[ret[M-1]-'A']!='#' && vis[O[ret[M-1]-'A']-'A'])
				{//printf("\ndone2 %s\n",ret.c_str());
					fo(j,30)vis[j]=0;
					ret="";
				}
				else
				{//printf("\ndone3\n");
					vis[s[i]-'A']++;
				}
			}
			else
			{
				vis[s[i]-'A']++;
			}
			//printf("\n* %s *\n",ret.c_str());
		}
		printf("Case #%d: [",k);
		fo(i,(int)ret.sz-1)printf("%c, ",ret[i]);
		if((int)ret.sz)printf("%c",ret[ret.sz-1]);
		printf("]\n");
	}
}


































