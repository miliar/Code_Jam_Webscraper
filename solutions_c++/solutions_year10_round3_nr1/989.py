#include <fstream>
#include <vector>

using namespace std;
ifstream cin ("input.txt"); ofstream cout ("output.txt");



vector <pair <int , int> >		sm;
int								T;
int								res;


int f (pair <int , int> a, pair <int , int> b)
{
	if ((a.first - b.first) * (a.second - b.second) < 0) return 1; else return 0;
}

int n;
int main ()
{
	cin >> T;
	for (int l = 0; l < T; ++l)
	{
		res = 0;
		sm.clear ();
		cin >> n;
		int a , b;
		for (int i = 0; i < n; ++i)
		{
			cin >> a >> b;
			sm.push_back ( pair <int , int> (a , b));
		}

		for (int i = 0 ; i < n; ++i)
			for (int j = i + 1; j < n; ++j)
				if (f (sm[i] , sm[j])) ++ res;
		
		cout << "Case #" << l + 1 << ": ";
		cout << res << endl;

	}
	return 0;
}