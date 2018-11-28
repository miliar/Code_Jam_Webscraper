#include <iostream>
using namespace std;

int main()
{
	int tests;
	int nrofintegers;
	int integers[1000];
	int scrambled;

	cin >> tests;
	for(int i = 1; i<=tests; i++){
		scrambled=0;

		cin >> nrofintegers;
		for(int j=0; j<nrofintegers; j++){
			cin >> integers[j];
		}

		for(int j=0; j<nrofintegers; j++){
			if(integers[j]!=j+1){
				scrambled++;
			}
		}

		cout << "Case #" << i << ": " << scrambled << "\n";
	}
	return 0;
}

