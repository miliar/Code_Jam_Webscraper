#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#include<string>
using namespace std;

const int maxn = 10000 + 10;
const int maxm = 100 + 5;

string w[maxn];
vector<int> app[maxn][26];
int n,m;

set<string> hash[26];
string list,tmp;
int main()
{
	int T,TT=0;

	int ans,ansi,cur;
	for( cin>>T;T;T-- )
	{
		cout << "Case #"<<++TT<<":";
		
		cin >> n >> m;
		for( int i = 0;i<n;i++ )
		{
			cin>>w[i];
			for( int j = 0;j<26;j++ ) app[i][j].clear();
			for( int j = 0;j<w[i].size();j++ )
				app[i][ w[i][j]-'a' ].push_back(j);
		}

		while( m-- )
		{
			cin>>list;
			for( int i = 0;i<26;i++ ) hash[i].clear();

			for( int i = 0;i<n;i++ )
			{
				tmp = w[i];
				for( int k = 25;k>=0;k-- ) if( !app[i][ list[k]-'a' ].empty() )
				{
					for( vector<int>::iterator it = app[i][ list[k]-'a' ].begin();it!=app[i][ list[k]-'a' ].end();++it )
						tmp[ *it ] = '_';
					hash[k].insert(tmp);
				}
			}

			ans = -1;
			for( int i = 0;i<n;i++ )
			{
				cur = 0;
				tmp = w[i];
				for( int j = 0;j<tmp.size();j++ ) tmp[j]='_';

				for( int j = 0;j<26;j++ ) if( hash[j].find(tmp)!=hash[j].end() )
				{
					//make guess
					if( app[i][ list[j]-'a' ].empty() ) cur++;
					for( vector<int>::iterator it = app[i][ list[j]-'a' ].begin();it!=app[i][ list[j]-'a' ].end();++it )
						tmp[ *it ] = list[j];
				}

				if( cur > ans )
				{
					ans = cur;
					ansi = i;
				}
			}


			cout << " " << w[ansi];
		}



		cout << endl;
	}
	return 0;
}
