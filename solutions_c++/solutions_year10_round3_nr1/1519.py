#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
unsigned int getindex(vector<unsigned int> X, unsigned int item)
{
	unsigned int min, max, mid;
	min = 0;
	max = X.size() - 1;
	while(min <= max) {
		mid = (min + max) / 2;
		if (X[min] == item)
			return min;
		if (X[max] == item)
			return max;
		if( X[mid] == item)
			return mid;
		else if (X[mid] < item) {
			min = mid + 1;
		}	
		else {
			max = mid - 1;
		}	
	}
}
int main()
{
	unsigned int C, N;
	unsigned int *A, *B;	
	cin >> C;
	for (int j = 0; j < C; j++) {
		cin >> N;
		A = new unsigned int[N];
		B = new unsigned int[N];
		for (int i = 0; i < N; i++) {
			cin >> A[i];
			cin >> B[i];
		}
		vector<unsigned int> Ai(A, A + N);
		vector<unsigned int> Bi(B, B + N);
		vector<unsigned int> SortedA, SortedB;
		SortedB = Bi;
		SortedA = Ai;
		sort(SortedA.begin(), SortedA.end());
		sort(SortedB.begin(), SortedB.end());
		unsigned int Aindex,Bindex,intersections = 0;
		for(int i = 0; i < N; i++) {
			Aindex = getindex(SortedA, Ai[i]);
			Bindex = getindex(SortedB, Bi[i]);
			if (Bindex > Aindex)
				intersections += (Bindex - Aindex);
		}

		cout << "Case #" << j + 1 << ": ";
		cout << intersections << "\n";
		delete[] A;
		delete[] B;
	}

	return 0;
}
