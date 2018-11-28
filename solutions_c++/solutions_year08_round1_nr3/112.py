#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

const char s[29][4] = { "027", "143", "751", "935", "607", "903", "991", "335", "047", "943", "471", "055", "447", "463", "991", "095", "607", "263", "151", "855", "527", "743", "351", "135", "407", "903", "791", "135", "647" };

int Ct, n;

void read_data () {
	cin >> n;
}

void solve () {
	cout << s[n-2] << endl;
}

int main () {
	cin >> Ct;

	for (int t = 0; t < Ct; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
