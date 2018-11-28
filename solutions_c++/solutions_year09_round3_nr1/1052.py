#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <iostream>
using namespace std;

 __int64 ans;

int main()
{
	char line[10240]={0};
	__int64 value[10240]={0};
	int casenum;
//	freopen("A-small-attempt4.in", "r", stdin);
//	freopen("A-large.in", "r", stdin);
//	freopen("out2.p", "w", stdout);
//	freopen("out.p", "w", stdout);
	scanf("%d", &casenum);
	for(int i=1;i<=casenum; ++i)
	{
		scanf("%s", line);
		map<char, int>mp;
		int len = strlen(line);
		int ltv = 0;
		ans = 1;
		mp[line[0]] = 2;
		value[0] = 1;
		for(int j=1; j<len; ++j)
		{
			if(mp[line[j]])
			{
				value[j] = mp[line[j]]-1;
			}
			else
			{
				value[j] = ltv;
				if (ltv == 0) ltv = 2;
				else ltv++;
				mp[line[j]] = value[j]+1;
			}
		}
		__int64 base = ltv;
		if (base < 2)base = 2;

		for(int k=1; k<len; ++k){
		//	printf("test%d\n", value[k]);
			ans = (__int64)(ans * base); 
//			printf("test%I64d\n", ans);
			ans += value[k];
		}
//		if(len==1)printf("Case #%d: 0\n", i);
//		cout<<"Case #";
//		cout<<i;
//		cout<<ans;
//		cout<<endl;
		printf("Case #%d: %I64d\n", i, ans);
	} 
	return 0;
}
