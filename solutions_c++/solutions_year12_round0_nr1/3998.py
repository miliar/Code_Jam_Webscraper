# include <iostream>
# include <cstdio>
# include <string>
using namespace std;

int main()
{
	string s[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string s1[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
	
	int i, T, j;
	char a[250];
	
	for (j = 0; j < 3; ++j)
		for (i = 0; i < (signed)s[j].length(); ++i)
			a[(int)s[j][i]] = s1[j][i];
	
	a['z'] = 'q';
	a['q'] = 'z';
	
	j = 1;
	cin >> T;
	while (T--)
	{
		scanf("\n");
		getline(cin, s[0]);
		cout << "Case #" << j << ": ";
		
		for (i = 0; i < (signed)s[0].length(); ++i)
			cout << a[(int)s[0][i]];
		
		cout << "\n";
		++j;
	}
	
	return 0;
}
