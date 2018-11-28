#include <string>
#include <iostream>
#include <set>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	cin >> T;
	for (int kase=1;kase<=T;++kase)
	{
		set<string> db;
		int N, M;
		cin >> N >> M;
		for (int q=0;q<N;++q)
		{
			string str;
			cin >> str;
			db.insert(str);
		}
		int ret=0;
		for (int q=0;q<M;++q)
		{
			string str;
			cin >> str;
			while (str.length())
			{
				if (db.find(str) != db.end()) break;
				db.insert(str);
				ret++;
				str = str.substr( 0, str.find_last_of("/") );
			}
		}
		cout << "Case #" << kase << ": " << ret << endl;
	}
	return 0;
}