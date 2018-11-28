/*
	http://code.google.com/codejam/contest/1460488/dashboard#s=p2
*/
#include <iostream>
#include <string.h>
#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main()
{
	int T, A, B;
	
	// lower, current, target, upper
	char strL[20];
	char strN[20];
	char strM[20];
	char strU[20];
	
	vector<int> vt;
	vector<int>::iterator it;
		
	cin >> T;
	for (int i = 0; i < T; i++) {
		int res = 0;
		cin >> A;
		cin >> B;
		
		sprintf(strL, "%d", A);
		sprintf(strU, "%d", B);
		
		int len = strlen(strL);
		
		// j is n && strC[k] is m
		for (int j = A; j <= B; j++) {
			sprintf(strN, "%d", j);
			sprintf(strM, "%d%d", j, j);		
			//printf("len[%d] %s %s %s %s\n", len, strL, strN, strM, strU);
			
			vt.clear();
			
			
			for (int k = 1; k < len; k++) {
				bool isGTE = false;
				bool isLTE = false; 
				bool ordered = false;	// n < m

				for (int m = 0; m < len; m++) {		
					if (ordered == true || strN[m] <= strM[k+m]) {
						if (strN[m] < strM[k+m]) { // n < m
							ordered = true;		
						} 			
					} else {	// n >= m
						break;	
					}
										
					if (isGTE == true || strL[m] <= strM[k+m]) {
						if (strL[m] < strM[k+m]) {
							isGTE = true;	// A < m
						}
					} else {	// A > m
						break;
					}				
					
					if (isLTE == true || strM[k+m] <= strU[m]) {
						if (strM[k+m] < strU[m] || (strM[k+m] == strU[m] && m == len - 1)) {
							isLTE = true; // m <= B	
						}
					} else {	// m > B
						break;	
					}
					
					if (ordered == true && isGTE == true && isLTE == true) {
						char tmp[10];
						strncpy(tmp, strM+k, len);
						tmp[len] = 0;
						
						int val = atoi(tmp);
						it = find (vt.begin(), vt.end(), val);
						if (it == vt.end()) {
							vt.push_back(val);
							res++;
						}
												
						//printf("[%04d]=>len[%d] k[%d] m[%d] %s n[%s] m[%s] %s comb[%s] \n", res, len, k, m, strL, strN, tmp, strU, strM);
						//printf("%s %s\n", strN, tmp);
						break;
					}
				}	
			}		
			
		}			
		
		cout << "Case #" << (i+1) << ": " << res << endl;		
	}	

	return 0;	
}