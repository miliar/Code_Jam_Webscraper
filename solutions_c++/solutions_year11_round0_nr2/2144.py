#include <set>   
#include <deque>   
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
#include <ctime>   
#include <queue>   
#include <map> 
#include <string.h> 
#include <queue> 
using namespace std;


char rec[30][30];
bool flag[30][30];
int main()
{
	freopen("1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,cas,len,j,k;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		memset(flag,0,sizeof(flag));
		memset(rec,0,sizeof(rec));
		char st3[5],st2[5],str[201];
		int n,m;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",st3);
			rec[st3[0]-'A'][st3[1]-'A']=st3[2];
			rec[st3[1]-'A'][st3[0]-'A']=st3[2];
		}
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf("%s",st2);
			flag[st2[0]-'A'][st2[1]-'A']=1;
			flag[st2[1]-'A'][st2[0]-'A']=1;
		}
		scanf("%d",&len);
		scanf("%s",str);
		vector<char>ans;
		ans.push_back(str[0]);
		for(i=1;i<len;i++)
		{
			if(ans.size()==0 || rec [ans[ans.size()-1]-'A'][str[i]-'A'] ==0 )
			{
				ans.push_back(str[i]);
			}
			else
			{
				
				int ec=ans[ans.size()-1]-'A';
				ans.pop_back();
				ans.push_back(rec [ec][str[i]-'A']);
			}
			m=ans.size();
			for(k=0;k<m-1;k++)
			{
				if(flag[ans[m-1]-'A'][ans[k]-'A']==1)
				{
					ans.clear();
					break;
				}
			}
		}
		printf("Case #%d: [",cas);
		for(i=0;i<ans.size();i++)
		{
			if(i==0)
				printf("%c",ans[i]);
			else printf(", %c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}