#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int K;
	int A, B;
	cin >> K;
	vector<double> p;
	vector<int> n;
	double d;
	double t = 1;
	for (int data = 1; data <= K; data++) {
		t = 1;
		cin >> A >> B;
		for (int i = 0; i < A; i++) {
			cin >> d;
			p.push_back(t * (1-d));
			t *= d;
		}
		p.push_back(t);
		
		double min = B + 2;
		
		for (int i = 0; i < B; i++) {
			for (int j = 0; j < p.size(); j++) {
				if (i + j + 1 >= p.size())
					n.push_back(B-A+1+2*i);
				else
					n.push_back(B-A+2*i+1+B+1);
			}
			double total = 0;
			for (int j = 0; j < n.size(); j++) {
				total += p.at(j) * n.at(j);
			}
			if (total < min)
				min = total;
			n.clear();
		}
		cout << fixed;
		cout << setprecision(6);
		cout << "Case #" << data << ": " << min << endl;
		p.clear();
	}
}
