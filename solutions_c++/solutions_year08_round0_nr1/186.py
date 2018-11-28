#include <iostream>
#include <queue>
#include <map>
#include <string>

using namespace std;

struct state
{
	int t;
	vector<int> A;
};

map<string, int> ID;
bool F[101];
string Q[1001];


string getname()
{
	string s = "";
	char ch;
	while ( (ch =getchar()) != '\n')
	{
		s += ch;
	}

	return s;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int k = 0;
	cin>>T;
	while (T--)
	{
		k++;
		ID.clear();
		int i;
		int n;
		int N;
		cin>>N;
		getchar();
		for (i = 0; i < N; i++)
		{
			ID[ getname() ] = i;
		}

		cin>>n;
		getchar();
		for (i = 0; i < n; i++)
		{
			Q[i] = getname();
		}

		i = 0;

		while (i < n && (!ID.count(Q[i]))) i++;

		int ans = 0;
		int loc = ID[ Q[i] ];
		i--;
		while (i < n)
		{
			i++;
			while (i < n && ID[Q[i]] != loc) i++;
			//i--;
			memset(F, 0, sizeof(F));
			int t = 0;
			while ( t < N && i < n)
			{
				if (ID.count(Q[i]))
				if (F[ ID[ Q[i] ] ] == false)
				{
					F[ ID[ Q[i] ] ] = true;
					t++;
					if ( t == N )
					{
						loc = ID[ Q[i] ];
						break;
					}
				}
				i++;
			}
			if (t == N)
			{
				i --;
				
			}
			ans ++;

			
		}

		cout<<"Case #"<<k<<": "<<ans-1<<endl;
	}
	return 0;
}