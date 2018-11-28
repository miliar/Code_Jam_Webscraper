#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isugly(long long int n)
{
	return (!(n%2) || !(n%3) || !(n%5) || !(n%7));
}


int main()
{
	int N, N2=0;
	scanf("%d\n",&N);
	while (N--) {
		char strnum[50];
		scanf("%s",strnum);
		//cerr << strnum << endl;
		int D = strlen(strnum);
		long long int ans = 0;
		if (D >= 2) {
			int op[D-1];
			for (int i=0; i<D-1; i++) {
				op[i] = 0;
			}
			while (true) {
			//	cerr << '.';
				long long int num = 0;
				char A[50];
				A[0] = '\0';
				int opn = 1;
				int id = 0;
				while (true) {
					A[0] = '\0';
					strncat(A,strnum+id,1);
					int i;
					for (i=id; i<D-1; i++) {
						if (op[i]==0) {
							strncat(A,strnum+i+1,1);
						} else {
							break;
						}
					}
				//	cerr << i << endl;
					switch (opn) {
						case 1:
							num += atoll(A);
							break;
						case 2:
							num -= atoll(A);
							break;
					}
					id = i+1;
					if (i==D-1) {
						break;
					} else {
						opn = op[i];
					}
				}
				if (isugly(num)) ans++;
				////
				op[D-2]++;
				int k = D-2;
				while (k>0 && op[k]==3) {
					op[k] = 0;
					k--;
					op[k]++;
				}
				if (op[0]==3) {
					break;
				}
			}
		} else {
			int n = atoi(strnum);
			if (isugly(n)) ans++;
		}


		printf("Case #%d: ",++N2);
		cout << ans << endl;
	}
	return 0;
}

