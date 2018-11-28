#include <iostream>
#include <algorithm>

#include <fstream>


using namespace std;

struct AB {
	int a,b;
	AB() {};
	AB(int aa, int bb):a(aa),b(bb){};
	bool operator < (const AB& sb) {
		return a < sb.a;
	}
};



int main() {
	AB arr[1001];

	ifstream inF;
	inF.open("A-large.in");
	ofstream outF;
	outF.open("A-large.out");
	int T;
	inF >> T;
	for (int tests = 0; tests < T; ++tests)
	{
		int N;
		inF >> N;

		int a,b;
		for(int i = 0;i<N;++i)
		{
			inF >> a >> b;
			arr[i] = AB(a,b);
		}
		
		sort(arr, arr+N);
		int inter = 0;
		for(int i = 0;i<N;++i)
			for(int j = i+1;j<N;++j)
				if (arr[j].b < arr[i].b)
					++inter;
		
		outF << "Case #" << tests+1 << ": " << inter << endl;
	}

	inF.close();
	outF.close();
	return 0;
}