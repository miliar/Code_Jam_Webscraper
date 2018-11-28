#include<iostream>
#include<list>
#include<map>
#include<vector>
#include<sstream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	string line;
	getline( cin, line );
	for( int t = 0; t < T; t++ )
	{
		int N;
		cin >> N;
		getline( cin, line );

		list<int> v;
		for( int n = 0; n < N; n++ )
		{
			int temp = 0;
			getline( cin, line );
			for( int i = 0; i < N; i++ )
			{
				if (line[i] == '1')
					temp = i;
			}
			v.push_back(temp);
		}

		long long ans = 0;
		list<int>::iterator it = v.begin();
		for( int n = 0; n < N; n++ )
		{
			if(0)
			{
				cout << "out";
				list<int>::iterator hoge = v.begin();
				for( int j = 0; j < N; j++ )
				{
					cout << *(hoge++) << " ";
				}
				cout << endl;
			}
			if (*it > n)
			{
				list<int>::iterator itr = it;
				itr++;
				for( int i = n+1; i < N; i++ )
				{
					if (*itr <= n)
					{
						it = v.insert( it, *itr );
						v.erase( itr );
						ans += i - n;
						break;
					}

					itr++;
				}
			}
			it++;
		}

		cout << "Case #" << (t+1) << ": " << ans << endl;
	}
}
