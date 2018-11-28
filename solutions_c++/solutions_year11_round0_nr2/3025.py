#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>


using namespace std;


int main()
{
	int t;
	string tmp;
	cin >> t;

	for (int test=1;test<=t;test++)
	{
		map<string,char> m;
		map<char,char> inv;
		int c,d,n;
		cin >> c;
		for (int i=0;i<c;i++)
		{
			cin >> tmp;
			string ind="";
			ind+=tmp[0];
			ind+=tmp[1];
			m[ind]=tmp[2];
		}

		cin >> d;
		for (int i=0;i<d;i++)
		{
			cin >> tmp;
			inv[tmp[0]]=tmp[1];
			inv[tmp[1]]=tmp[0];
		}

		vector<char> list;		
		cin >> n;
		string s;
		cin >> s;

		int j=0;
		
		for (int i=0;i<n;i++)
		{
			list.push_back(s[i]);
			if (list.size()>1)
			{
				string pair="";
				pair+=list[list.size()-2];
				pair+=list[list.size()-1];
				char x=m[pair];
				if (!x)
				{
					pair="";
					pair+=list[list.size()-1];
					pair+=list[list.size()-2];
					x=m[pair];
				}
				if (x)
				{
					list.pop_back();
					list.pop_back();
					list.push_back(x);
				}
				
				else 
				{
					for (int k=0;k<list.size()-1;k++) if (list[k]==inv[s[i]])
					{
						list.clear();
						break;
					}
				}
			}
		}

		string ans="[";
		if (!list.empty()) for (int i=0;i<list.size()-1;i++) 
		{
			ans+=list[i];
			ans+=", ";
		}

		if (list.size()>0)
			ans+=list[list.size()-1];

		ans+="]";

		cout << "Case #" << test << ": " << ans << endl;
		

	}
	//system("pause");
		return 0;
}