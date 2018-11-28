#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

typedef vector< long > veclong;

long product(veclong a, veclong b)
{
	long sum = 0;

	for(int i = 0; i < (int) a.size(); i++) {
		sum += a.at(i) * b.at(i);
	}

	return sum;
}

long min_product(veclong a, veclong b)
{
	/*
	long min = product(a, b);

	sort(a.begin(), a.end());
	do {
		sort(b.begin(), b.end());
		do {
			long result = product(a, b);
			if(result < min) {
				min = result;
			}
		} while(next_permutation(b.begin(), b.end()));
	} while(next_permutation(a.begin(), a.end()));
	*/

	sort(a.begin(), a.end());
	reverse(a.begin(), a.end());
	sort(b.begin(), b.end());

	return product(a, b);
}

int main(int argc, char *argv[])
{
	int ncases;
	cin>>ncases;

	for(int i = 0; i < ncases; i++) {
		int nsize;
		cin>>nsize;

		veclong a(nsize), b(nsize);

		for(int j = 0; j < nsize; j++) {
			cin>>a.at(j);
		}

		for(int j = 0; j < nsize; j++) {
			cin>>b.at(j);
		}

		cout<<"Case #"<<i + 1<<": "<<min_product(a, b)<<endl;
	}

	return 0;
}

