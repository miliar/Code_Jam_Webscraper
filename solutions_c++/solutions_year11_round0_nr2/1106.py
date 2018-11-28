#include <iostream>

#define ABCSIZE 26
#define MAXSIZE 200

using namespace std;

int main(){
	int iCases, nCases;
	cin >> nCases;
	
	int i,j,t,n,k;
	char str[MAXSIZE];
	int presents[ABCSIZE];
	bool opposed[ABCSIZE][ABCSIZE];
	int formPairs[ABCSIZE][ABCSIZE];			
	int elements[MAXSIZE];
	for (iCases=1; iCases <= nCases; iCases++){
		for (i=0; i<ABCSIZE; i++){
			presents[i]=0;
			for (j=0; j<ABCSIZE; j++){
				opposed[i][j]=false;
				formPairs[i][j]=-1;
			}
		}
		
		// Pair input
		cin >> t;
		for (i=0; i<t; i++){
			cin >> str;
			formPairs[str[0]-'A'][str[1]-'A']=str[2]-'A';
			formPairs[str[1]-'A'][str[0]-'A']=str[2]-'A';
		}
		
		// Opposed input
		cin >> t;
		for (i=0; i<t; i++){
			cin >> str;
			opposed[str[0]-'A'][str[1]-'A']=true;
			opposed[str[1]-'A'][str[0]-'A']=true;
		}
		
		//Combination
		cin >> n;
		cin >> str;

		k=0;
		for (i=0; i<n; i++){
			elements[k]=str[i]-'A';
			presents[elements[k]]++;
			
			// check for pair
			while (k>0 and formPairs[elements[k-1]][elements[k]]!=-1){
				presents[elements[k]]--;
				presents[elements[k-1]]--;
				elements[k-1]=formPairs[elements[k-1]][elements[k]];
				presents[elements[k-1]]++;
				k--;
			}
			
			// check for opposeds
			for (j=0; j<ABCSIZE; j++){
				if (presents[j]<=0)
					continue;
				if (opposed[j][elements[k]]==false)
					continue;
					
				k=-1;		// With the k++, we obtain k=0
				for (j=0; j<ABCSIZE; j++)
					presents[j]=0;
				break;
			}
			k++;
			
			#ifdef DEBUG
				cout << "[";
				for (j=0; j<k; j++){
					if (j>0)
						cout << ", ";
					cout << char('A'+elements[j]);
				}
				cout << "]" << endl;
			#endif
		}
		
		cout << "Case #" << iCases << ": ";
		cout << "[";
		for (i=0; i<k; i++){
			if (i>0)
				cout << ", ";
			cout << char('A'+elements[i]);
		}
		cout << "]" << endl;
	}
	return 0;
}
