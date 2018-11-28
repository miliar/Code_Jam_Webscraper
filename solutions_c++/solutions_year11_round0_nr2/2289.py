#include<iostream>
#include<vector>
#include <algorithm>
#include <stack>
#include <string>
#include <map>

using namespace std;

string reverse(string s)
{
	string s2 = s;
	reverse(s2.begin(),s2.end());
	return s2;
}

bool check_r(map<string,bool>rmap, string t)
{
	for(int i = 0; i < t.length(); i++)
	{
		for(int j = 0; j < t.length(); j++)
		{
			if(i==j)
				continue;
			if(rmap[t.substr(i,1)+t[j]] || rmap[reverse(t.substr(i,1)+t[j])])
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	int tests;
	cin >> tests;
	for(int j = 0; j < tests; j++)
	{
		string ans = "";
		stack<char> mystack;
		map<string,char> cmap;
		map<string,bool> rmap;
		int C,D,N;
		string combine,reject,entry;
		cin >> C;
		for(int i = 0; i <C; i++)
		{
			cin >> combine;
			cmap[combine.substr(0,2)] = combine[2];
		}
		cin >> D;
		for(int i = 0; i <D ; i++)
		{
			cin >> reject;
			rmap[reject] = true;
		}
		cin >> N >> entry;
		cerr << C << " " << D << endl;
		//cerr << "ERR2" << endl;
		for(int i = N-1; i >= 0; i--)
		{
			//cerr << "ERR3: " << i << endl;
			mystack.push(entry[i]);
		}
		//cerr << "ERR1" << endl;
		while(!mystack.empty())
		{
			char tmp1 = mystack.top();
			char tmp2;
			mystack.pop();
			//cerr << "ERR4" << endl;
			if(!mystack.empty())
				tmp2 = mystack.top();
			else
			{
				ans+=tmp1;
				break;
			}
			char tmp3, tmp4;
			string t;
			if(tmp1)
				t += tmp1;
			if(tmp2)
				t += tmp2;

			tmp3 = cmap[t];
			tmp4 = cmap[reverse(t)];
			if(tmp3)
			{
				mystack.pop();
				mystack.push(tmp3);
				continue;
			}
			else if(tmp4)
			{
				mystack.pop();
				mystack.push(tmp4);
				continue;
			}
			else if(check_r(rmap,ans+tmp1+tmp2))
			{
				mystack.pop();
				cerr << ans + tmp1 + tmp2 << endl;
				ans = "";
				cerr << "CHECKED" << endl;
				continue;
			}
			ans+=tmp1;
			cerr << t << " " << ans << endl;
		}
		cout << "Case #" << j+1 << ": [";
		if(ans.length())
			cout << ans[0];
		for(int i = 1; i < ans.length(); i++)
		{
			cout << ", " << ans[i];
		}
		cout << "]" << endl; 
	}
}