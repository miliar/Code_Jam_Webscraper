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

int arr[10005];

int main()
{
    freopen ("C.in","r",stdin);
    freopen ("C.out","w",stdout);
    
    int i,j,k=0,T;
    
    scanf("%d",&T);
    while(T--)
    {
		k++;
		int N,L,H;
		scanf("%d %d %d",&N,&L,&H);
		fo(i,N)
		{
			scanf("%d",&arr[i]);
		}
		int f=0;
		for(int i=L;i<=H;i++)
		{
			int x=0;
			fo(j,N)
			{
				if(arr[j]%i==0 || i%arr[j]==0)x++;
			}
			if(x==N)
			{
				printf("Case #%d: %d\n",k,i);
				f=1;
				break;
			}
		}
		if(!f)
		{
			printf("Case #%d: NO\n",k);
		}
	}
}


































