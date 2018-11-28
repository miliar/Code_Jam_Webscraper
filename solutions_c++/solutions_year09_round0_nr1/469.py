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
#include <ctime> 
using namespace std;
typedef long long ll;


int L,D,N;
char str[5010][17];
char ch;
bool used[17][27];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d", &L, &D, &N);
	for(int i = 0; i < D; i++)
		scanf("%s", str[i]);
	for(int i = 0; i < N; i++)
	{
		memset(used, 0, sizeof used);
		for(int j = 0; j < L; j++)
		{
			ch = getchar();
		    while(ch == ' ' || ch == '\n') ch = getchar();
			if(ch != '(') 
			{
				used[j][ch - 'a'] = true;
			}
			else
			{
				while((ch = getchar()) != ')')
					used[j][ch - 'a'] = true;
			}
		}   
		int res = 0;
		for(int j = 0; j < D; j++)
		{
			bool any = true;
			for(int k = 0; k < L; k++)
			{
				if(!used[k][str[j][k] - 'a'])
				{
					any = false;
					break;
				}
			}
			if(any)
				res++;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}	
}
