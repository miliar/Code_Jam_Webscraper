#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
	size_t ss;
	cin >> ss;

	for(size_t s = 1; s <= ss; s++)
	{
		string n;
		cin >> n;

		string res = n;

		next_permutation(res.begin(), res.end());
		if(strcmp(n.c_str(), res.c_str()) >= 0)
		{
			res.append(1, '0');
			//cerr << n << "::" << res << " :> " << endl;
			sort(res.begin(), res.end());
			char t = res[0];
			size_t ind = res.find_first_not_of('0');
			res[0] = res[ind];
			res[ind] = t;

		}

		cout << "Case #" << s << ": " << res << endl;
	}
	return 0;
}
