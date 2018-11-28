//Candy Splitting

#include <iostream>
#include <algorithm>
using namespace std;

int main ()
{
	int T, N;
	cin >> T;
	int seanPile[T-1];
	
	for(int i=0; i<T; i++){
		// get input
		cin >> N;
		int candy[N-1];
		int xorSum=0;
		seanPile[i] = 0;
		for(int j=0; j<N; j++){
			cin >> candy[j];
			xorSum = xorSum ^ candy[j];
		}
		if(xorSum == 0){
			sort(candy, candy + N);
			for(int j=1; j<N; j++)
				seanPile[i] = seanPile[i] + candy[j];
		}
	}
	for(int i=0; i<T; i++){
		if(seanPile[i] == 0){
			cout << "Case #" << i+1 << ": NO" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << seanPile[i] << endl;
		}
	}
	return 0;
}
