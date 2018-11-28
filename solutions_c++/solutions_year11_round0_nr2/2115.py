#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin>>T;
	int i;
	vector<string> change;
	vector<string> opposite;
	string str;
	for(i = 1; i<=T; i++)
	{
		change.clear();
		opposite.clear();
		str.clear();
		int C, D, N;
		cin>>C;
		int j;
		string temp;
		string temp2;
		for(j = 0; j<C; j++)
		{
			cin>>temp;
			change.push_back(temp);
		}
		cin>>D;
		for(j = 0; j<D; j++)
		{
			cin>>temp;
			opposite.push_back(temp);
		}
		cin>>N;
		cin>>str;
		int k;
		for(j = 1; j<str.size(); j++)
		{
			temp2 = str.substr(j-1, 2);
			temp = temp2;
			reverse(temp.begin(), temp.end());
			for(k = 0; k<change.size(); k++)
			{
				if(change[k].substr(0,2) == temp || change[k].substr(0,2) == temp2)
				{
					str.replace(j-1, 2, change[k].substr(2, 1));
					break;
				}
			}
			int pos = j;
			int m;
			for(k = 0; k<opposite.size(); k++)
			{
				if(str.substr(j,1) == opposite[k].substr(0,1))
				{
					string temp = opposite[k].substr(1,1);
					for(m = j-1; m>=0; m--)
					{
						if(str.substr(m, 1) == temp)
						{
							if(m<pos)
								pos = m;
						}
					}
				}
				if(str.substr(j,1) == opposite[k].substr(1,1))
				{
					string temp = opposite[k].substr(0,1);
					for(m = j-1; m>=0; m--)
					{
						if(str.substr(m,1) == temp)
						{
							if(m<pos)
								pos = m;
						}
					}
				}
			}
			if(pos<j)
			{
				str.erase(0, j+1);
				j = 0;
			}
		}
		cout<<"Case #"<<i<<": "<<"[";
		for(j = 0; j<str.size(); j++)
		{
			if(j == 0)
				cout<<str[j];
			else
				cout<<", "<<str[j];
		}
		cout<<"]"<<endl;
	}
	return 0;
}