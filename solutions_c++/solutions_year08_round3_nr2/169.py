#include <fstream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

string line;
vector<ll> op;
ll N, D, ans;

ll calc()
{
	ll ret=0, t=line[0]-'0', znak = 1;
	for (ll i=1; i<D; i++)
		if (op[i-1] == 0) t = t*10 + (line[i]-'0'); else
			if (op[i-1] == 1) {
				if (znak == 1) ret += t; else ret -= t;
				t = line[i] - '0';
				znak = 1;
			} else {
				if (znak == 1) ret += t; else ret -= t;
				t = line[i] - '0';
				znak = 2;
			}
	if (znak == 1) ret += t; else ret -= t;
	return ret;
}

bool ugly(ll n)
{
	if (n<0) n=-n;
	return (n == 0 || n%2 == 0 || n%3 == 0 || n%5 == 0 || n%7 == 0);
}

void Solve(ll pl)
{
	if (pl == D-1){
		ll value = calc();
		if (ugly(value)) ans++;
	} else
		for (ll i=0; i<3; i++){
			op[pl] = i;
			Solve(pl+1);
		}
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	in >> N;
	getline(in, line);
	for (ll i=0; i<N; i++){
		ans = 0;
		op.clear();
		line = "";
		getline(in, line);

		D = line.length();
		for (ll j=0; j<D-1; j++) op.push_back(0);
		if (D == 1){
			if (ugly(line[0]-'0')) ans++;
		} else Solve(0);
		out << "Case #" << i+1 << ": " << ans << endl;
	}

	in.close();
	out.close();
}