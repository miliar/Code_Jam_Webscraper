#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
int T,c,d,n,pairs[30][2],opp[30];
int a,b;
string str,ans;

bool flag;
	int taken[30];
void reduce() // ans
{
	if(ans.size()<2)
		return;

	a = ans[ans.size()-1]-'A';
	b = ans[ans.size()-2]-'A';

	if(pairs[a][0]!=b)
		return;

	taken[int(ans[ans.size()-1]-'A')]--;
	taken[int(ans[ans.size()-2]-'A')]--;
	taken[pairs[a][1]]++;
	ans.erase(ans.size()-1,1);
	ans[ans.size()-1]=char('A'+pairs[a][1]);
	flag=true;
	reduce();
}

int main()
{
	char x,y,z;

	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	cin>>T;
	for(int t=0;t<T;t++)
	{
		cin>>c;
		memset(pairs,-1,sizeof(pairs));
		for(int i=0;i<c;i++)
		{
			cin>>x>>y>>z;
			pairs[x-'A'][0]=int(y-'A');
			pairs[x-'A'][1]=pairs[y-'A'][1]=int(z-'A');
			pairs[y-'A'][0]=int(x-'A');
		}
		cin>>d;
		memset(opp,-1,sizeof(opp));
		for(int i=0;i<d;i++)
		{
			cin>>x>>y;
			opp[x-'A']=int(y-'A');
			opp[y-'A']=int(x-'A');
		}

		memset(taken,0,sizeof(taken));
		cin>>n>>str;
		ans=str[0];
		taken[int(str[0]-'A')]++;
		for(int i=1;i<n;i++)
		{
			ans+=str[i];
			taken[int(str[i]-'A')]++;
			flag=false;
			reduce();
			if(flag)
				continue;

			if(opp[int(str[i]-'A')]!=-1 && (taken[opp[int(str[i]-'A')]]!=0))
			{
				for(int ba=0;ba<ans.size();ba++)
					taken[int(ans[ba]-'A')]--;

				ans.clear();
			}
		}

		cout<<"Case #"<<t+1<<": [";
		for(int i=0;i<ans.size();i++)
		{
			if(i!=0)
				cout<<", ";
			cout<<ans[i];
		}
		cout<<"]\n";
	}
	return 0;
}