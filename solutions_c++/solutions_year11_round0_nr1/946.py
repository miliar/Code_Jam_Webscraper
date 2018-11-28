#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
int T,test;
__int64 ans,n,pos1,pos2,k,f1,f2,cur;
char c;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;

	for(test=1;test<=T;test++)
	{
		f1=f2=ans=0;
		pos1=pos2=1;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>c>>k;
			if(c=='O')
			{
				cur=abs(k-pos1);
				if(cur>=f1)
					ans+=cur-f1+1,f2+=cur-f1+1,f1=0;
				else
					f1=0,ans++,f2++;
				pos1=k;
			}
			else
			{
				cur=abs(k-pos2);
				if(cur>=f2)
					ans+=cur-f2+1,f1+=cur-f2+1,f2=0;
				else
					f2=0,ans++,f1++;
				pos2=k;
			}
		}
		
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}