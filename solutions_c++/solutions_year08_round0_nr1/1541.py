#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

int main(void)
{
	int t,no=0,i;
	int s,q;
	map<string,int> engine;
	vector<string> ser_str;
	string str;

	cin >> t;
	while (t--)
	{
		cin >> s;
		for (i=0; i<s; i++)
		{
			cin.clear();
			cin.sync();
			getline(cin,str,'\n');
			engine.insert(make_pair(str,0));
		}

		cin >> q;
		for (i=0; i<q; i++)
		{
			cin.clear();
			cin.sync();
			getline(cin,str,'\n');
			ser_str.push_back(str);
		}

		map<string,int>::iterator iter;
		int cur=0;
		int sw=0;
		bool flag;

		while (cur<ser_str.size())
		{
			for (i=cur; i<ser_str.size(); i++)
			{
				str=ser_str[i];
				iter=engine.find(str);
				if (iter!=engine.end() && iter->second==0)
					iter->second=i+1;

				flag=false;
				for (iter=engine.begin(); iter!=engine.end(); iter++)
				{
					if (iter->second==0)
					{
						flag=true;
						break;
					}
				}
				if (flag==false)
				{
					cur=i;
					break;
				}
			}
			if (i==ser_str.size() && flag==true)
				cur=ser_str.size();
			else if (i!=ser_str.size())
				sw++;
			
			for (iter=engine.begin(); iter!=engine.end(); iter++)
				iter->second=0;
		}

		cout << "Case #" << ++no << ": " << sw << endl;

		ser_str.clear();
		engine.clear();
	}

	return 0;
}