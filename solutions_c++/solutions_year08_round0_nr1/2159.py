#include <iostream>
#include <string>
#include <vector>
using namespace std;

int proc(vector <string> s, vector <string> q)
{
	bool hs=false;
	int m[100],ch=0,mx=0;
	int pos=0;
	while (pos<q.size())
	{
		for (int i=0;i<s.size();i++)
		{
			for (int j=pos;(j<q.size() && (!hs));j++)
				if (s[i]==q[j]) {hs=true;mx=max(mx,j);}
			if (!hs) return ch;
			hs=false;
		}
		pos = mx;
		ch++;
	}
	return ch;
}

int main()
{
	string x;
	int n,k,r=0,l;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> n;
	for (int r=0;r<n;r++)
	{
		vector <string> s,q;
		cin >> k;
		getline(cin, x);
		for (int i=0;i<k;i++)
			{getline(cin, x);  s.push_back(x);}
		cin >> l;
		getline(cin, x);
		for (int i=0;i<l;i++)
			{getline(cin, x); q.push_back(x);}
		cout << "Case #" << r+1 << ": " << proc(s,q) << endl;
	}	
	return 0;
}
