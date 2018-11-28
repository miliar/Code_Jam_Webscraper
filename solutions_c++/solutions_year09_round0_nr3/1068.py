#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define all(x) (x).begin(),(x).end()

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	int N;
	string A;
	string B = "welcome to code jam";

	cin >> N;
	getline(cin, A);
	for(int c=1; c<=N; c++)
	{
		getline(cin, A);
		vector< vector<int> > count( (int)A.size(), vector<int>( (int)B.size(), 0 ) );
		int count_one_char = 0;
		for(int i=0; i<(int)A.size(); i++)
		{
			if(A[i] == B[0]) count[i][0] = ++count_one_char;
			else count[i][0] = count_one_char;
		}

		for(int p=1; p<(int)B.size(); p++)
			for(int x=p; x<(int)A.size(); x++)
				for(int i=p; i<=x; i++)
					if(A[i] == B[p])
					{
						count[x][p] += count[i-1][p-1];
						count[x][p] %= 10000;
					}

		cout << "Case #" << c << ": ";
		cout << (int) (count[(int)A.size()-1][(int)B.size()-1] / 1000);
		cout << (int) (count[(int)A.size()-1][(int)B.size()-1]%1000 / 100);
		cout << (int) (count[(int)A.size()-1][(int)B.size()-1]%100 / 10);
		cout << (int) (count[(int)A.size()-1][(int)B.size()-1]%10);
		cout << endl;
	}

	return 0;
}
