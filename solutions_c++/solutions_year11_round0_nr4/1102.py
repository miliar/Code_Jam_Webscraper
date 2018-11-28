#include <iostream>
#include <cstdio>

#define MAXN 1000

using namespace std;

/*
The strategy is to find all the cycles and then calculate a number of moves for each cycle, which is precisely the size of the cycle
*/
int main(){
	int iCases, nCases;
	cin >> nCases;
	
	int i, j, n;
	for (iCases=1; iCases <= nCases; iCases++){
		cin >> n;
		int array[n];
		bool chosen[n];
		double moves=0;
		
		for (i=0; i<n; i++){
			cin >> array[i];
			chosen[i]=false;
		}
		
		int size=0;
		for (i=0; i<n; i++){
			if (chosen[i])
				continue;
			
			size=0;
			j=i;
			do{
				j=array[j]-1;
				chosen[j]=true;
				size++;
			}while(j!=i);
			moves+=(size>1?size:0);
		}
				
		cout << "Case #" << iCases << ": ";
		cout << int(moves);
		cout << ".000000";
		cout << endl;
	}
	return 0;
}