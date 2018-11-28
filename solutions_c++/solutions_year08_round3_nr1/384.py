#include<iostream>
#include<fstream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in;
    in.open(argv[1], ifstream::in);
	ofstream out;
	out.open(argv[2], ofstream::out);
	int ci, cc;

	in >> cc;
	for(ci = 0; ci < cc; ci++){
		int p, k, l;
		in >> p >> k >>l;
		if(p*k < l) {
			cout << "Case #" << ci+1 << ": " << "Impossible" << endl;
			continue;
		}
		vector<long long> m;
		for(int i=0; i<l; i++) {
			long long t;
			in >> t;
			m.push_back(t);
		}
		sort(m.begin(), m.end(), greater<long long>());
		long long ans = 0;
		for(int i=0; i<l; i++) {
			ans += m[i] * ((i / k) + 1);
		}
		out << "Case #" << ci+1 << ": " << ans << endl;
	}
    return 0;
}
