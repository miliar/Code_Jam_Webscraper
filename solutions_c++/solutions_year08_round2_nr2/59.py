#include <iostream>
#include <vector>
#include <cstdlib>
#include <set>
using namespace std;

vector<int> ps;

void primes() {
	ps.push_back(2);
	for(int i = 3; i <= 1000000; i += 2) {
		for(int j = 3; j <= i / j; ++j)
			if(i % j == 0) goto noprime;
		ps.push_back(i);
		noprime:;
	}
}

vector<int> ec;

int ecfind(int a) {
	if(ec[a] == a) return a;
	else return ec[a] = ecfind(ec[a]);
}

void ecunion(int a, int b) {
	ec[ecfind(a)] = ecfind(b);
}

int main() {
	
	primes();

	int C;
	cin >> C;
	for(int	i = 1; i <= C; ++i) {
		cout << "Case #" << i << ": ";
				
		long long A, B, P;
		cin >> A >> B >> P;
		++B;
		
		ec.clear();
		for(int j = 0; j != (int)(B-A)+(int)ps.size(); ++j)
			ec.push_back(j);
		
		for(long long x = A; x < B; ++x) {
			int pos = (int)x-A+(int)ps.size();
			for(size_t k = 0; k != ps.size(); ++k)
				if(ps[k] >= P && x % ps[k] == 0)
					ecunion(pos, k);
		}
		
		set<int> sol;
		for(long long x = A; x < B; ++x) {
			int pos = (int)x-A+(int)ps.size();
			sol.insert(ecfind(pos));
		}
		
		cout << sol.size() << endl;
	}
	
}
