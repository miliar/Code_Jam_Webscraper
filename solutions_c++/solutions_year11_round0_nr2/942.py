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
__int64 n,c,d,opp['Z'+10]['Z'+10],comb['Z'+10]['Z'+10];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	string s,ans;
	for(test=1;test<=T;test++)
	{
		ans="";
		for(int i='A';i<='Z';i++)
			for(int j='A';j<='Z';j++)
				comb[i][j]=opp[i][j]=0;
		cin>>c;
		for(int i=0;i<c;i++)
			cin>>s,comb[s[0]][s[1]]=comb[s[1]][s[0]]=s[2];
		cin>>d;
		for(int i=0;i<d;i++)
			cin>>s,opp[s[0]][s[1]]=opp[s[1]][s[0]]=1;
		cin>>n>>s;
		for(int i=0;i<n;i++)
		{
			if(ans.size()==0)
			{
				ans+=s[i];
				continue;
			}
			char cur=s[i],prev=ans[ans.size()-1];
			if(comb[cur][prev])
			{
				ans.erase(ans.size()-1,1);
				ans+=(char)(comb[cur][prev]);
				continue;
			}
			bool op=false;
			for(int j=0;j<ans.size();j++)
				if(opp[s[i]][ans[j]])
				{
					op=true;
					break;
				}
			if(op)
			{
				ans="";
				continue;
			}
			ans+=cur;
		}
		cout<<"Case #"<<test<<": [";
		for(int i=0;i<ans.size();i++)
		{
			cout<<ans[i];
			if(i<ans.size()-1)
				cout<<", ";
		}
		cout<<"]"<<endl;
	}
	return 0;
}