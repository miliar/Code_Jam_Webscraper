#include <iostream>
#include <stdlib.h>

using namespace std;

main(){
	int T;
	cin >> T;
	int count = 0;
	while(count < T){
		count++;
		int A, B, m, numC = 0;
		cin >> A >> B;
		for(int i = A; i < B; i++){
			int n = i;
			string tempN;
			while(n != 0){
				tempN += n % 10 + '0';
				n /= 10;
			}
			string temp = tempN;
			for(int j = 0; j < temp.size(); j++){
				tempN[j] = temp[temp.size()-1-j];
			}
			for(int j = 1; j < tempN.size(); j++){
				string tempM;
				for(int k = j; k < tempN.size(); k++){
					tempM += tempN[k];
				}
				for(int k = 0; k < j; k++){
					tempM += tempN[k];
				}
				m = atoi(&tempM[0]);
				n = atoi(&tempN[0]);
				if(m > n && m <= B)	{numC++;}
			}
		}
		cout << "Case #" << count << ": " << numC << endl;
	}
	return 0;
}
		
			
			
			
