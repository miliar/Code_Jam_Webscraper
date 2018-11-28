#include <iostream>
using namespace std;

int main ()
{
	int T, C, D, N;
	char str1[4];
	char str2[3];
	char str3[101];

	char result [101];
	int pair[26][26];
	int reverse[26][26];
	char uniques[8];

	
	cin >> T;
	for (int t=0; t<T; t++){
		for (int i=0; i<26; i++) {
			for (int j=0; j<26; j++) {
				pair[i][j]=-1;
				reverse[i][j]=-1;
			}
		}

		cin >> C;
		for (int c= 0; c<C; c++) {
			cin >> str1;
			int firstChar = str1[0]-'A';
			int secondChar = str1[1]-'A';
			int thirdChar = str1[2];
			pair[firstChar][secondChar] = pair[secondChar][firstChar] = thirdChar;
		}
		
		cin >> D;
		for (int d= 0; d<D; d++) {
			cin >> str2;
			int firstChar = str2[0]-'A';
			int secondChar = str2[1]-'A';
			reverse[firstChar][secondChar] = reverse[secondChar][firstChar] = 1;
		}

		cin >> N;

		cin >> str3;
		int resultIndex = 0;
		int firstChar;
		int secondChar;
		int uniqueIndex = 0;
		int uniqueFlag;
		for (int n= 0; n<N; n++) {
			result[resultIndex++] = str3[n];
			if (resultIndex > 1) {
				firstChar = result[resultIndex-1]-'A';
				secondChar = result[resultIndex-2]-'A';
				if (pair[firstChar][secondChar] != -1) {
					//cout << pair[firstChar][secondChar] <<endl;
					result[resultIndex-2] = (char) pair[firstChar][secondChar];
					resultIndex -= 1;
					continue;
				}
				uniqueFlag = 1;
				for (int u=0; u<uniqueIndex; u++) {
					if (result[resultIndex-2] == uniques[u]) {
						uniqueFlag = 0;
						break;
					}
				}
				if (uniqueFlag == 1)
					uniques[uniqueIndex++] = result[resultIndex-2];
				for(int u=0; u<uniqueIndex; u++) {
					secondChar = uniques[u]-'A';
					if (reverse[firstChar][secondChar] == 1) {
						resultIndex = 0;
						uniqueIndex = 0;
					}
				}

			}
			
		}
		
		cout << "Case #" << t+1 << ": [";
		for (int n= 0; n<resultIndex; n++) {
			cout << result[n];
			if (n<resultIndex-1) 
				cout << ", ";
		}
		cout << "]" <<endl;
	}
}
