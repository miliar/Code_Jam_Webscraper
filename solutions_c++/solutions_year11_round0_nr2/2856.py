#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;
int main()
{
	int t,tt,i,c,d,n,k;
	scanf("%d",&t);
	for(tt=1; tt<=t; tt++)
	{
		char s1[4];
		char s2[3];
		string s;
		
		scanf("%d",&c);
		for(i=0; i<c; i++)
			scanf("%s",s1);
			
		scanf("%d",&d);
		for(i=0; i<d; i++)
			scanf("%s",s2);
			
		scanf("%d",&n);
		cin>>s;
		string ss;
		for(i=0; i<n; i++)
		{
			int kk;
			ss+=s[i];
			//cout<<"ss "<<ss<<endl;
			k=ss.size()-1;
			if(k>=1 && c!=0 && ((ss[k-1]==s1[0] && ss[k]==s1[1])||(ss[k-1]==s1[1] && ss[k]==s1[0])))
			{
				ss[ss.size()-2]=s1[2];
				ss.erase(ss.size()-1,1);
			//	cout<<"1 "<<ss<<endl;		
			}
			else	if(d!=0 && ss[k]==s2[0])
			{
				kk=k;
				while(kk>=0 && ss[kk]!=s2[1])
					kk--;
				if(kk>=0)
					ss.clear();
			//	cout<<"2 "<<ss<<endl;		
			}
			else if(d!=0 && ss[k]==s2[1])
			{
				kk=k;
				while(kk>=0 && ss[kk]!=s2[0])
					kk--;
				if(kk>=0)
					ss.clear();
			//	cout<<"3 "<<ss<<endl;		
			}
			
		}
		printf("Case #%d: [",tt);
		for(i=0; i<ss.size(); i++)
		{
			if(i!=ss.size()-1)
			{
				printf("%c, ",ss[i]);
			}
			else
				printf("%c",ss[i]);
		}
		printf("]\n");
	}
	return 0;
}
