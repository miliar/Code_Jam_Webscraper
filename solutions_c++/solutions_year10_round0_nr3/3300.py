#include <vector>
#include <algorithm>
#include <list>
#include <set>
#include <map>
#include <fstream>


using namespace std;

ifstream cin ("input.txt"); ofstream cout ("output.txt");

struct item
{
	int			people;
	int			iterations;
	item (int np = 0, int nit = 0) : people (np) , iterations (nit) {}
};

vector <int>		sm;
map <int , item>	mp;
list <int>			lst;
int					t , n , num_iterations , num_people ;

int sum (vector <int> sm)
{
	int res = 0;
	for (vector <int>::iterator it = sm.begin(); it != sm.end(); ++it)
		res += *it;
	return res;
}

int main ()
{
	cin >> t;
	for (int l = 0; l < t; ++l)
	{
		sm.clear ();
		lst.clear ();
		mp.clear ();

		cin >> num_iterations  >> num_people >> n;
		cout << "Case #" << l + 1 <<": ";
		sm.resize (n);
		for (int i = 0; i < n; ++i)
			cin >> sm[i];

		for (int i = 0; i < n; ++i)
			lst.push_back (i);

		// tests
		if (sum (sm) < num_people)
		{
			cout << sum (sm) * num_iterations << endl;
			continue;
		}

		int people = 0;
		int iterations = 0;
		int diterations , dpeople;
		while (iterations < num_iterations)
		{
			if (mp.find (lst.front()) != mp.end())
			{
				dpeople = people - mp[lst.front()].people;
				diterations = iterations - mp[lst.front()].iterations;
				people += dpeople * (( num_iterations - iterations) / diterations ) ;
				iterations += ((num_iterations - iterations) / diterations) * diterations;
				mp.clear ();
				continue;
			}
			mp.insert (pair <int , item> (lst.front() , item (people , iterations)));
			int tmp = 0;
			while (tmp + sm[lst.front()] <= num_people)
			{
				tmp += sm[lst.front()];
				lst.push_back (lst.front ());
				lst.pop_front ();
			}
			people += tmp;
			iterations++;
		}

		cout << people << endl;


	}

	return 0;
}
