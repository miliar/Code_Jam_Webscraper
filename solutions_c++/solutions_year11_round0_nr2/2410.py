#include <iostream>
#include <cmath>
#include <string>
#include <vector>


using namespace std;

void solve()
{
	int c,d,n;

	string s;
	char ch;

	vector<char> v;
	vector<string> rep;
	vector<string> del;

	cin>>c;
	for(int i=0;i<c;i++)
	{
		cin>>s;
		rep.push_back(s);
	}

	cin>>d;
	for(int i=0;i<d;i++)
	{
		cin>>s;
		del.push_back(s);
	}

	cin>>n;
	bool done;
	for(int f=0;f<n;f++)
	{
		done=false;
		cin>>ch;
		v.push_back(ch);
		{
			if(v.size()>1)
			{
				for(int i=0;i<c;i++)
				{
					if((v[v.size()-1]==rep[i][0]&&v[v.size()-2]==rep[i][1])||(v[v.size()-2]==rep[i][0]&&v[v.size()-1]==rep[i][1]))
					{
						v.pop_back();
						v.pop_back();
						v.push_back(rep[i][2]);
						done=true;
						break;
					}
				}
				if(!done)
				{
					for(int i=0;i<d;i++)
					{
						if(v[v.size()-1]==del[i][0])
						{
							for(int j=0;j<v.size()-1;j++)
							{
								if(v[j]==del[i][1])
								{
									v.clear();
									done=true;
								}
								if(done)
									break;
							}
						}
						if(done)
							break;
						if(v[v.size()-1]==del[i][1])
						{
							for(int j=0;j<v.size()-1;j++)
							{
								if(v[j]==del[i][0])
								{
									v.clear();
									done=true;
								}
								if(done)
									break;
							}
						}
						if(done)
							break;
					}
				}
			}
		}
	}

	cout<<'[';
	if(v.size()!=0)
		cout<<v[0];
	for(int i=1;i<v.size();i++)
	{
		cout<<", "<<v[i];
	}
	cout<<']';
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}