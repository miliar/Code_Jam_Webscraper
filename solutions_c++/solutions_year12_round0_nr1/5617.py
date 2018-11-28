#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
using namespace std;

string a[3000], b[3];
char mp[255];
int main()
{            
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	a[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	a[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	a[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	b[0] = "our language is impossible to understand";
	b[1] = "there are twenty six factorial possibilities";
	b[2] = "so it is okay if you want to just give up";
	int n = 3;
	for(int i = 'a'; i <= 'z'; ++i)
	{
		bool found = false;	
		for(int j = 0; j < n && !found; ++j)
			for(int jj = 0; jj < a[j].size() && !found; ++jj)
				if(a[j][jj] == i)
				{
					found = true;
					mp[i] = b[j][jj];
				}
	}
	mp['z'] = 'q';
	mp['q'] = 'z'; 	
	mp[' '] = ' ';
	cin >> n;
	string str;
	getline(cin, str);
	for(int i = 0; i < n; ++i)
	{
		getline(cin, str);
		cout << "Case #" << i + 1 << ": ";
		for(int j = 0; j < str.size(); ++j)
			cout << mp[str[j]];
		cout << endl;
	}
	return 0;
}                 