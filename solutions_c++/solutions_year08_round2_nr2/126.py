#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int K=1000000;
bool p[K+10];
bool p2[K];
vector<int> pr;

int main() {
	memset(p2, 0, sizeof(p2));
	pr.push_back(2);
	for (int i=3; i< K; i+= 2) {
		if (p2[i] == 0) {
			pr.push_back(i);
			long long v=i;
			v*=i;
			while (v < K) {
				p2[v] = 1;
				v += i;
			}
		}
	}
	ifstream inp("b.in");
	ofstream out("b.out");
	int N;
	inp >> N;
	for (int test=1;test<=N;test++) {
		out << "Case #" << test << ": ";

		memset(p, 0, sizeof(p));
		long long A, B, P;
		inp >> A >> B >> P;
		long long sum = 0, first = -1;
		for (int i=0; i< pr.size(); i++) {
			if (pr[i] >= P && ((A-1)/pr[i]+1)*pr[i] <= B) {
				if (first == -1) {
					sum++;
					first = i;
				} else {
					bool ok=false;
					for (int k=first; k<i; k++) {
						long long v=pr[k]*pr[i];
						if (((A-1)/v+1)*v <= B) {
							ok=true;
							break;
						}
					}
					if (!ok) sum++;
				}
				long long k = ((A-1)/pr[i]+1)*pr[i];
				while (k <= B) {
					p[k-A] = 1;
					k += pr[i];
				}
			}
		}
		for (long long  i=A; i<= B; i++) {
			if (p[i-A] == 0) {
				sum++;
			}
		}
		out << sum;
		out << endl;
	}
}

