#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;





long long int dot(vector<long long int>& ap,  vector<long long int>& an, list<long long int>& bp, list<long long int>& bn)
{
	long long int sum = 0;


	for (int i=0; i < an.size(); i++) {

		long long int n;
		if (bp.size()) {
			n = bp.back();
			bp.pop_back();
		} else {
			n = bn.back();
			bn.pop_back();
		}

		sum += (an[i] * n);
	}


	for (int i=ap.size() - 1; i >= 0; i--) {

		long long int n;
		if (bn.size()) {
			n = bn.front();
			bn.pop_front();
		} else {
			n = bp.front();
			bp.pop_front();
		}

		sum += (ap[i] * n);
	}



	return sum;
}




//-----------------------------------------------------------------------------
int main(int argc, char* argv[])
{

	int iter;
	int len;
	long long int n;

	vector<long long int> ap, an;
	list<long long int> bp, bn;


	cin >> iter;

	for (int i=0; i < iter; i++) {
		cin >> len;
		ap.clear();
		an.clear();
		bp.clear();
		bn.clear();

		for (int j=0; j < len; j++) {
			cin >> n;
			if (n <= 0) {
				an.push_back(n);
			} else {
				ap.push_back(n);
			}

		}


		for (int j=0; j < len; j++) {
			cin >> n;
			if (n <= 0) {
				bn.push_back(n);
			} else {
				bp.push_back(n);
			}
		}


		sort(ap.begin(), ap.end());
		sort(an.begin(), an.end());

		bp.sort();
		bn.sort();


		cout << "Case #" << (i + 1) << ": " << dot(ap, an, bp, bn) << endl;
	}





	return 0;
}
