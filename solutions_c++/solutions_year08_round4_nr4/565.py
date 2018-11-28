#include <algorithm>
#include<iostream>
#include<vector>
using namespace std;

using namespace std;

char str[50005];
vector<int> per;
int main() 
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int l,ncase; scanf("%d",&ncase);
	for(l=1;l<=ncase;++l)
	{
		int i,k,len,tmp,answer;
		scanf("%d", &k);
		getchar();
		gets(str);
		per.clear();
		for(i=0; i<k; i++)per.push_back(i+1);
		len = strlen(str);
		answer=0x3FFFFFFF;
		do 
		{
			char ch=str[per[0]-1];
			tmp=1;
			for(i=1;i<len;i++) 
			{
				if(ch==str[((i)/k)*k+per[i%k]-1])continue;
				else 
				{
					ch=str[((i)/k)*k+per[i%k]-1];
					tmp++;
				}
			}
			answer=min(answer,tmp);
		}while (next_permutation(per.begin(), per.end()));
		printf("Case #%d: %d\n",l,answer);
	}

	return 0;
}
