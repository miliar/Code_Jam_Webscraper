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

char arr[55][55];

int main()
{
    freopen ("A.in","r",stdin);
    freopen ("A.out","w",stdout);
    
    int i,j,k=0,T;
    
    scanf("%d",&T);
    while(T--)
    {
		int R,C;
		k++;
		scanf("%d %d",&R,&C);
		fo(i,R)scanf("%s",arr[i]);
		
		fo(i,R-1)
		{
			fo(j,C-1)
			{
				if(arr[i][j]=='#' && arr[i+1][j+1]=='#' && arr[i+1][j]=='#' && arr[i][j+1]=='#')
				{
					arr[i][j]='/'; arr[i+1][j+1]='/'; arr[i+1][j]='\\'; arr[i][j+1]='\\';
				}
			}
		}
		int f=0;
		fo(i,R)
		{
			fo(j,C)if(arr[i][j]=='#')f=1;
		}
		if(f)
		{
			printf("Case #%d:\nImpossible\n",k);
		}
		else
		{
			printf("Case #%d:\n",k);
			fo(i,R)printf("%s\n",arr[i]);
		}
	}
}


































