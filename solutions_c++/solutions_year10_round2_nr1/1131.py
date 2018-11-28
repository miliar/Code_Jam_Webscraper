#include<string>
#include<vector>
#include<iostream>
#include<set>
#include<fstream>

using namespace std;

int main()
{
	int T;
	string filename = "A-large (1)";
	ifstream cin;
	cin.open( filename + ".in" );
	
	ofstream cout;
	cout.open( filename + ".out.txt" );
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		int N,M;
		cin >> N >> M;
		vector<string> mp(M);
		set<string> np;
		np.insert("");
		cin.ignore();
		for(int n = 0; n < N; n++)
		{
			string temp;
			cin >> temp;
			np.insert(temp);
		}
		for(int m = 0; m < M; m++)
		{
			cin >> mp[m];
		}

		int ret = 0;
		for(int m = 0; m < M; m++)
		{
			for( string::size_type i = 0; ; i = mp[m].find("/", i+1) )
			{
				string temp;
				if(i != string::npos)
				{
					temp = mp[m].substr(0,i);
				}
				else
				{
					temp = mp[m];
				}
				if(np.find(temp) == np.end())
				{
					ret++;
					np.insert(temp);
				}
				if(i == string::npos)
					break;
			}
		}
		cout << "Case #" << t+1 << ": " << ret << endl;
	}
}
