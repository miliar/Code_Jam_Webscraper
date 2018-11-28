#include <iostream>
#include <list>

using namespace std;

int main() {
	int T, C, D, N;
	int arrC[26][26];
	int arrD[26][26];
	char lst[100];
	int lst_index = 0;
	int alpha[26]; 
	
	string str;

	cin >> T;
	
	for (int i = 0; i < T; i++) {
		lst_index = 0;
		
		for (int j = 0; j < 100; j++)
			lst[j] = 0;		
			
		for (int j = 0; j < 26; j++) 
			alpha[j] = 0;	// if exist, set it 1;
		
		for (int j = 0; j < 26; j++)
			for (int k = 0; k < 26; k++)
				arrC[j][k] = arrD[j][k] = 0;
		
		int res = 0;
		
		cin >> C;
		
		for (int j = 0; j < C; j++) {
			cin >> str;
			arrC[str[0]-'A'][str[1]-'A'] = str[2] - 'A';
			arrC[str[1]-'A'][str[0]-'A'] = str[2] - 'A';
		}
		
		cin >> D;
		
		for (int j = 0; j < D; j++) {
			cin >> str;
			arrD[str[0]-'A'][str[1]-'A'] = 1;
			arrD[str[1]-'A'][str[0]-'A'] = 1;
		}		

/*
		for (int j = 0; j < 24; j++) {
			for (int k = 0; k < 24; k++) {
				cout << arrC[j][k] << "[" << arrD[j][k] << "] ";
			}
			cout << endl;
		}
		cout << endl;
*/

		cin >> N;
		cin >> str;
		
		//lst[0] = str[0];
		//lst_index = 1;
		//alpha[str[0]-'A'] += 1;
		
		
	//	cout << "lst_index: " << lst_index << endl;		
		for (int j = 0; j < N; j++) {
	//	cout << "N[" << N << "] lst_idx: " << lst_index << " str[" << str[j] << "]"<< endl;
			if (lst_index == 0) {	// there is no previous element
				lst[lst_index] = str[j];			
				alpha[str[j]-'A'] += 1;
				lst_index++;
			} else {	// there is a previous element
				// check if 'combine'
				if (arrC[lst[lst_index-1]-'A'][str[j]-'A'] != 0) {	// 'combine' works
			//		cout << "code 14 - N: " << N << endl;
					alpha[lst[lst_index-1]-'A'] -= 1;
			//		cout << "code 15 - N: " << N << endl;
					lst[lst_index-1] = arrC[lst[lst_index-1]-'A'][str[j]-'A'] + 'A';
			//		cout << "code 16 - N: " << N << endl;
					alpha[lst[lst_index-1]-'A'] += 1;
			//		cout << "code 17 - N: " << N << " - aaa[" << lst[lst_index-1]-'A' << "]" << endl;
				} else {	// 'combine' doesn't work
					lst[lst_index] = str[j];
					alpha[lst[lst_index]-'A'] += 1;
					lst_index++;
				}
			//	cout << "code 11 - N: " << N << endl;
				// check if 'opposed'
				for (int k = 0; k < j; k++) {
					if (arrD[lst[k]-'A'][lst[lst_index-1]-'A'] > 0) {	// remove whole element list
						for (int s = 0; s < 100; s++)
							lst[s] = 0;
						for (int s = 0; s < 24; s++) 
							alpha[s] = 0;
						lst_index = 0;
					}					
				}				
			}
/*
			cout << "N: " << N << " [" << j << "] lst:";
			for (int kk = 0; kk < lst_index; kk++) {
				cout << lst[kk] << " ";
			}
			cout << endl;
	*/								
	//		cout << str[j] << " ";
		}
//		cout << endl;		
				
		cout << "Case #" << (i+1) <<": [";
		for (int k = 0; k < lst_index - 1; k++) {
			cout << lst[k] << ", ";
		}
		cout << lst[lst_index-1] << "]" << endl;
	}
		
	return 0;
}
