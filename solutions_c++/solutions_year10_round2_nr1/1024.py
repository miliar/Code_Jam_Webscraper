#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
#include<deque>
#include<map>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int n,m;
		cin >> n >> m;
		vector<string> dir;
		for(int j=0;j<n;j++)
		{
			string s;;
			cin >> s;
			dir.push_back(s);
		}
		vector<string> ns;
		for(int j=0;j<m;j++)
		{
			string s;
			cin >> s;
			ns.push_back(s);
		}
		int mkdir =0;
		for(int j=0;j<m;j++)
		{
			string s = ns[j];
			string prt;
				prt.push_back('/');
				for(int k=1;k<s.length();k++)
				{
					char c = s[k];
					if(c == '/')
					{	bool is = false;
						for(int l=0;l<dir.size();l++)
						{
							if(dir[l] == prt)
								 is = true;
						}
						if(is == false)
						{
							dir.push_back(prt);
							mkdir += 1;
						}
					}
					prt.push_back(c);
				}
				bool is = false;
				for(int l = 0 ; l < dir.size();l++)
				{
					if(dir[l] == prt)
						is = true;
				}
				if(is == false)
				{
					dir.push_back(prt);
					mkdir += 1;
				}
			}
		cout << "Case #"<<i<<": "<<mkdir<<endl;
	}
return 0;
}
