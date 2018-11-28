#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <map>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);

	int case_nr, T;
	string tmp;

	getline(cin, tmp);
	T = atoi(tmp.c_str());;

	for (case_nr=1; case_nr<=T; case_nr++) {
		getline(cin, tmp);

		map <char, int> cyfry;
		int lastdigit = 0;
		for (int i=0; i<tmp.size(); i++)
		{
			if (cyfry.find(tmp[i]) == cyfry.end())
			{
				int val = lastdigit >= 2 ? lastdigit : 1 - lastdigit;
				cyfry.insert(make_pair(tmp[i], val));
				tmp[i] = val;
				lastdigit++;
			} else
				tmp[i] = cyfry[tmp[i]];
		}


		int base = lastdigit;
		if (base < 2)
			base = 2;

		long long res=0;

		for (int i=0; i<tmp.size(); i++)
		{
			res*=base;
			res += tmp[i];
		}
		
		cout << "Case #" << case_nr << ": " << res << "\n";
	}
}
