#include<vector>
#include<iostream>
#include<fstream>
#include<algorithm>

using namespace std;

struct bag
{
	int sum_p, sum;
	bag():sum_p(0), sum(0){}
	void put(int x)
	{
		sum += x;
		sum_p ^= x;
	}
};

int main(int argc, char *argv[])
{
	ifstream ifs(argv[1]);
	int T;
	ifs >> T;
	for(int i=0;i<T;i++){
		int N;
		ifs >> N;
		vector<int> C(N);
		for(int j=0; j<N; j++)
			ifs >> C[j];
		sort(C.begin(), C.end());//to extract minimum one

		bag S, P;
		P.put(C[0]);
		for(size_t j = 1; j < C.size(); j++)
			S.put(C[j]);

		if((P.sum_p ^ S.sum_p) != 0)
			cout << "Case #" << i+1 << ": " << "NO" << endl;
		else
			cout << "Case #" << i+1 << ": " << S.sum << endl;
	}
	return 0;
}