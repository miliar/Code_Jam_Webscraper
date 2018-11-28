#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cmath>
using namespace std;
int a,b,n;
char combo[26][26];
char opp[28][2];
int used[26];
char to(char c)
{
	return c-'A';
}
bool test1(char c1,char c2)
{
	return combo[c1][c2];
}
bool test2(char c1)
{
	for (int i=0;i<b;i++)
	{
		if (opp[i][0]==c1&&used[opp[i][1]]||
			opp[i][1]==c1&&used[opp[i][0]])
			return 1;
	}
	return 0;
}

int main()
{

	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{
		memset(used,0,sizeof(used));
		memset(combo,0,sizeof(combo));
		memset(opp,0,sizeof(opp));
		cin>>a;
		for (int i=0;i<a;i++)
		{
			char f,t,val;
			cin>>f>>t>>val;
			f=to(f);
			t=to(t);
			val=to(val);
			combo[f][t]=combo[t][f]=val;
		}
		cin>>b;
		for (int i=0;i<b;i++)
		{
			char f,t;
			cin>>f>>t;
			f=to(f);
			t=to(t);
			opp[i][0]=f;
			opp[i][1]=t;
		}
		cin >>n;
		vector<char> res;
		for (int i=0;i<n;i++)
		{
			char c;
			cin>>c;
			c=to(c);
			if (res.empty())
			{
				res.push_back(c);
				used[c]++;
			}
			else
			{
				char c2=c;
				char c1=res.back();
				bool ok1,ok2;
				bool destr=0;
				while ((ok1=test1(c1,c2))||(ok2=test2(c2)))
				{
					if (ok1)
					{
						used[c1]--;
						res.pop_back();
						c2=combo[c1][c2];
						if (res.empty())
							break;
						c1=res.back();
						continue;
					}
					if (ok2)
					{
						memset(used,0,sizeof(used));
						destr=1;
						res.clear();
						break;
					}
				}
				if (!destr)
				{
					used[c2]++;
					res.push_back(c2);
				}
			}
		}
		cout<<"Case #"<<curt<<": ";
		if (res.empty())
		{
			cout<<"[]";
		}
		else
		{
			cout<<"[";
			for (int i=0;i<res.size()-1;i++)
			{
				cout<<char(res[i]+'A')<<", ";
			}
			cout<<char(res.back()+'A')<<"]";
		}
		cout<<endl;
	}

	


	 

	return 0;
}