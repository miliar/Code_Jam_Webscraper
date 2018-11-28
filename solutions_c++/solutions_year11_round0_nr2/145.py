#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

int t,n,x,y;
string s;
vector<string> cb,op;
vector<char> l;

int ispair(char a, char b, char c, char d)
{
	if (a==c && b==d) return 1;
	if (a==d && b==c) return 1;
	return 0;
}

void add(char ch)
{
	//printf("add %c\n",ch);
	l.push_back(ch);
	for (int i=0;i<cb.size();i++) if (ispair(cb[i][0],cb[i][1],l[l.size()-2],l[l.size()-1]))
	{
		//printf("i=%d\n",i);
		l.pop_back();
		l.pop_back();
		add(cb[i][2]);
		return;
	}
	for (int i=0;i<=l.size()-1;i++)
		for (int j=0;j<op.size();j++)
			if (ispair(op[j][0],op[j][1],l[i],ch))
			{
				l.clear();
				return;
			}
}

int main()
{
	//freopen("b.in","r",stdin);
	//freopen("b.out","w",stdout);
	cin >> t;
	for (int k=1;k<=t;k++)
	{
		cb.clear();
		op.clear();
		cin >> x;
		while (x--)
		{
			cin >> s;
			cb.push_back(s);
		}
		cin >> x;
		while (x--)
		{
			cin >> s;
			op.push_back(s);
		}
		cin >> s >> s;
		l.clear();
		for (int i=0;i<s.size();i++)
			add(s[i]);
		
		if (l.size()==0)
		{
			printf("Case #%d: []\n",k);
			continue;
		}
		printf("Case #%d: [",k);
		for (int i=0;i<l.size()-1;i++) printf("%c, ",l[i]);
		printf("%c]\n",l[l.size()-1]);
	}
	
	
	return 0;
}
