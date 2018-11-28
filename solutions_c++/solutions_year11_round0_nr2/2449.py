#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string>

using namespace std;

int change[26][26];
int bad_elems[26][26];


vector<char> magic_list;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Bs.out","w",stdout);
	int T;
	cin>>T;
	for(int test = 1; test <= T; ++test)
	{
		magic_list.clear();

		for (int i = 0; i< 26; ++i)
			for (int j=0; j< 26; ++j)
			{
				change[i][j]=bad_elems[i][j] = 0;
			}

		int n;
		cin >> n;
		for (int i=0; i < n; ++i)
		{
			string s;
			cin >> s;
			
			change[ s[0] - 'A' ][ s[1] - 'A' ] = s[2];
			change[ s[1] - 'A' ][ s[0] - 'A' ] = s[2];
		}
		cin >> n;
		for (int i=0; i < n; ++i)
		{
			string s;
			cin >> s;

			bad_elems[ s[0] - 'A' ][ s[1] - 'A' ] = 1;
			bad_elems[ s[1] - 'A' ][ s[0] - 'A' ] = 1; 
		}

		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			char c;
			int flag  = 0;
			cin >> c;
			while ( !isalpha(c) )
				cin>>c;
			if (magic_list.empty())
			{
				magic_list.push_back(c);
				continue;
			}
			if ( change[c - 'A'][magic_list [magic_list.size() - 1] - 'A' ] > 0 )
			{
				magic_list [magic_list.size() - 1] = change[c - 'A'][magic_list [magic_list.size() - 1] - 'A' ];
			}
			else 
			{
				for(int j = 0; j < magic_list.size(); ++j)
					if (bad_elems [c - 'A'][magic_list [j] - 'A'] > 0)
					{
						magic_list.clear();
						flag = 1;
						break;
					}
				if (!flag)
					magic_list.push_back(c);

			}
	

		}

		cout << "Case #"<<test<<": [";

		for (int i = 0; i < (int)magic_list.size() - 1 ; ++i)
			cout << magic_list[i]<<", ";
		
		if (!magic_list.empty())
			cout<< magic_list [magic_list.size() - 1 ];

		cout<< "]";

		cout<<endl;
	}
	fclose(stdout);
	return 0;
}