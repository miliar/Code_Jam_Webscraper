#include <iostream>
#include <string>
#include <vector>

using namespace std;
struct bor
{
	string name;
	vector <int> child;
};
bor ver[1000000];
long gy;
long add_string(const string & q,long y)
{
     long j;
     for(j=0;j<ver[y].child.size();j++)
     {
			if(ver[ver[y].child[j]].name == q)
				{
					y = ver[y].child[j];
					return y;
				}
	 }
	 ver[gy].name = q;
	 ver[y].child.push_back(gy);
	 ver[gy].child.clear();
	 gy++;
	 return gy-1;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	string t,s;
	int tt,ti,i,j,f,n,m,y;
	cin >> tt;
	for(ti=0;ti<tt;ti++)
	{
		cin >> n >> m;
		ver[0].name = "";
		ver[0].child.clear();
		gy = 1;
		for(i=0;i<n;i++)
		{
			cin >> s;
			j = 1;
			t.clear();
			y = 0;
			while(j < s.length())
			{
				while(s[j] != '/' && j < s.length()) {t+=s[j];j++;}j++;
				y = add_string(t,y);t.clear();//cout << t << endl;
			}
		}
		f = gy;
		for(i=0;i<m;i++)
		{
			cin >> s;
			j = 1;
			t.clear();
			y = 0;
			while(j < s.length())
			{
				while(s[j] != '/' && j < s.length()) {t+=s[j];j++;}j++;
				y = add_string(t,y);t.clear();//cout << t << endl;
			}
		}
		cout << "Case #" << ti+1 << ": " << gy-f << endl;
	}
	return 0;
}
