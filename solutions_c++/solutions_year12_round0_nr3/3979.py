#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int sortFunction( const void *a, const void *b)
{	
	return (*((int*)a) < *((int*)b))? -1 : (*((int*)a) == *((int*)b))? 0 : 1;
}

int main(void)
{	
	int T;	
	cin >> T;

	for (int a=0; a < T; a++)
	{
		int low = 0;
		int high = 0;

		cin >> low;
		cin >> high;

		int digits[10];
		int helparray[20];

		int totalPairs = 0;

		for (int i = low; i <= high; i++) {			
			int num = i;
			int pos = 0;
			while (num > 0) {
				digits[pos] = num % 10;
				num = num / 10;
				pos++;
			}			
	
			int k = 0;
			for (int j=0; j <pos; j++) {			
				helparray[k] = digits[j];
				helparray[k+pos] = digits[j];
				k++;
			}			

			int usedNummers[20];
			int usedNummersCount = 0;
			for (int j=0; j < pos; j++) {
				int m = 0;
				int mul = 1;				
				for (int k=0; k < pos; k++) {
					m += mul * helparray[k+j];
					mul *= 10;
				}
				bool exists = false;
				for (int k=0; k < usedNummersCount; k++) {
					if (usedNummers[k] == m) exists = true;
				}
				if (exists) continue;				
				usedNummers[usedNummersCount++] = m;
				if ((i < m) && (m <= high)) totalPairs++;
			}

		}	
		cout << "Case #" << (a+1) << ": " << totalPairs;		
		cout <<"\n";
		
	}
}

