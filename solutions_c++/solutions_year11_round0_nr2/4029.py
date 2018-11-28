#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <ctime>
#include <sstream>
#include <stack>
#include <queue>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for (i=0;i<(n);i++)
#define FOR(i,l,h) for (i=(l);i<=(h);i++)
#define FORD(i,h,l) for(i=(h);i>=(l);i--)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long int LLI;
typedef pair<int,int> PII;



int main()
{
	int n, c, d, t;
	map<string, string> opposite;
	map<string, string> result;
	map<string, string> combine;

	cin >> t;
	int qqq = 0;
	REP(qqq, t)
	{
		opposite.clear();
		result.clear();
		combine.clear();

		//cout << endl << endl << endl;
		//cout << "q " << qqq <<  " t " << t << endl;

		cin >> c;

		string s;

		int i = 0;
		REP(i, c)
		{
		//cout << "i " << i <<  " c " << c << endl;
			cin >> s;
			string a, b, z;
			a = s[0];
			b = s[1];
			z = s[2];
			combine[a] = b;
			combine[b] = a;

			result[a+b] = z;
			result[b+a] = z;
		}

		cin >> d;

		i = 0;
		REP(i, d)
		{
		//cout << "i " << i <<  " d " << d << endl;
			cin >> s;
			string a, b;
			a = s[0];
			b = s[1];

			opposite[a] = b;
			opposite[b] = a;
		}


		cin >> n;
		vector<string> stack;

		i = 0;
			string all;
			cin >> all;
		REP(i, n)
		{
		//cout << "i " << i <<  " n " << n << endl;


			int j = 0;
			//REP(j, all.length())
			//{
		//cout << "i " << i <<  " all " << all.length() << endl;
		//cout << "this is all " << all << endl;
				string next;
				next = all[i];
				//cout << "Reading in: " << next << endl;

				if (stack.empty())
				{
					//cout << "dong empty" <<endl;
					stack.insert(stack.begin(), next);
					continue;
				}

				string prev;
				prev = stack[0];
				//cout << "The count " << stack.size();
				//cout << "Next and prev are " << next << " " << prev << endl;

				if (combine[next] == prev)
				{
					//cout << "dong combine with " << result[next+prev] << endl;
					stack[0] = result[next+prev];
					continue;
				}

				int kz =0;
				bool broken = false;
				string trollingjamie = opposite[next];
				REP(kz, stack.size())
				{
					prev = stack[kz];
					if (trollingjamie == prev)
					{
						//cout << "dong opposite" << endl;
						//cout << "for " << next << " and " << prev << endl;
						stack.clear();
						broken = true;
						break;

					}

				}
				if (!broken)
					stack.insert(stack.begin(), next);

			//}
			
		}
		cout << "Case #" << qqq+1 << ": ";
			int countr = stack.size();
			if (countr == 0)
				cout << "[]" << endl;
			else if (countr == 1)
				cout << "[" << stack[0] << "]" << endl;
			else
			{
				cout << "[" << stack[stack.size()-1];
				for (int j = stack.size()-2;j>=0;j--)
					cout << ", " << stack[j];
				cout << "]" << endl;
			}
	}
		

	return 0;
}
