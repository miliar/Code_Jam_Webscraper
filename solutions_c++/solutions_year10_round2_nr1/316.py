#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

vector<string> split(string s)
{
	int pnt = 1;
	int i;
	vector<string> res;
	res.clear();
	for (i=2;i<s.length();i++) if (s[i] == '/')
	{
		res.push_back(s.substr(pnt,i - pnt));
		pnt = i + 1;
	}
	res.push_back(s.substr(pnt,s.length() - pnt));
	return res;
}

/*void handin(string buf)
{
	vector<string> s = split(buf);
	int i,j;
	string now;
	bool flag;
	vector<tree_type> r = &data;
	tree_type newnode;
	newnode.child.clear();
	for (i=0;i<s.size();i++)
	{
		now = s[i];
		r = data;
		flag = false;
		for (j=0;j<r.size();j++) if (r[j].name == now)
		{
			flag = true;
			r = r[j].child;
			break;
		}
		if (!flag)
		{
			r.push_back(newnode);
			r[r.size() - 1].name = now;
			r[r.size() - 1].child.clear();
			r = r[r.size() - 1].child;
		}
	}
}

void read_data()
{
	cin >> n >> m;
	int i;
	string buf;
	for (i=1;i<=n;i++)
	{
		cin >> buf;
		handin(buf);
	}
}

int check(string buf)
{
	vector<string> s = split(buf);
	int i,j;
	vector<tree_type> r = &data;
	string now;
	bool flag;
	int ans = 0;
	tree_type newnode;
	for (i=0;i<s.size();i++)
	{
		now = s[i];
		flag = false;
		for (j=0;j<r.size();j++) if (r[j].name == now)
		{
			r = r[j].child;
			flag = true;
		}
		if (!flag)
		{
			ans++;
			r.push_back(newnode);
			r[r.size() - 1].name = now;
			r[r.size() - 1].child.clear();
			r = r[r.size() - 1].child;
		}
	}
	return ans;
}

int work_ans()
{
	string buf;
	int i,res = 0;
	for (i=1;i<=m;i++)
	{
		cin >> buf;
		res += check(buf);
	}
	return res;
}
*/

int n,m;
vector<string> data[500];
int total;

void read_data()
{
	cin >> n >> m;
	total = 0;
	int i;
	string buf;
	for (i=1;i<=n;i++)
	{
		total++;
		cin >> buf;
		data[total] = split(buf);
	}
}

int check(vector<string> s,vector<string> t)
{
	int l = min(s.size(),t.size());
	int i;
	for (i=0;i<l;i++) if (s[i] != t[i]) return i;
	return l;
}

int work_ans()
{
	int i,j;
	int ans = 0;
	string buf;
	vector<string> s;
	int temp;
	for (i=1;i<=m;i++)
	{
		total++;
		cin >> buf;
		s = split(buf);
		temp = 0;
		for (j=1;j<total;j++) temp = max(temp,check(s,data[j]));
		ans += s.size() - temp;
		data[total] = s;
	}
	return ans;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int ans,t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		read_data();
		ans = work_ans();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
