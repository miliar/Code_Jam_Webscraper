#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int m,n,tt,c,d,r;
char ch[1000];
char str[10];
int mp[30][30];
int mp1[30][30];
int  f[30];
struct buttom
{
	char c;
	int node;
	int next;
};
int hash(char s)
{
	return s-'A'+1;
}
char _hash(int t)
{
	return t+'A'-1;
}
buttom b[300];
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{		
		memset(mp,0,sizeof(mp));
		memset(mp1,0,sizeof(mp1));
		cin>>c;
		for (int i=1;i<=c;++i)
		{
			cin>>str;
			mp1[hash(str[0])][hash(str[1])]=hash(str[2]);
			mp1[hash(str[1])][hash(str[0])]=hash(str[2]);
		}
		cin>>d;
		for (int i=1;i<=d;++i)
		{
			cin>>str;
			mp[hash(str[0])][hash(str[1])]=-1;
			mp[hash(str[1])][hash(str[0])]=-1;
		}
		cin >> n >> ch;
		memset(f,0,sizeof(f));
		vector<char> ans;
		int t1,t2;
		char t3;
		for (int i=0;i<n;++i)
		{
			ans.push_back(ch[i]);
			f[hash(ans[ans.size()-1])]++;
			if (ans.size()>=2)
			{
				t1=hash(ans[ans.size()-1]);
				t2=hash(ans[ans.size()-2]);
				if (mp1[t1][t2]>0)
				{
					ans.resize(ans.size()-2);
					ans.push_back(_hash(mp1[t1][t2]));
					f[t1]--;
					f[t2]--;
					f[mp1[t1][t2]]++;
					continue;
				}
				for (int j=1;j<30;++j)
				{
					if (f[j]>0 && mp[t1][j]==-1)
					{
						ans.clear();
						memset(f,0,sizeof(f));
						break;
					}
				}
			}			
		}
		
		printf("Case #%d: [",kk);
		if (ans.size()==0)
		{
			cout<<"]"<<endl;			
		}
		else if (ans.size()==1)
		{
			cout<<ans[ans.size()-1]<<"]"<<endl;
		}
		else
		{
			for (int i=0;i<ans.size()-1;++i)
			{
				cout<<ans[i]<<", ";
			}

			cout<<ans[ans.size()-1]<<"]"<<endl;
		}		
	}	
	return 0;	
}