#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <valarray>
#include <bitset>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
#define LOOP(i,a,n) for(i=(a);i<(n);++i)
#define Loop(i,n) LOOP(i,0,(n))
#define RLOOP(i,a,n) for(i=(a);i>(n);--i)

int nTestCase, testCase;
char mat[40][41];
char row[41];
long ans;
int n;

bool isThisRowOk(int j, int i){
	for(int k=i+1; k<n; k++){
		if(mat[j][k] == '1')
			return false;
	}
	return true;
}


int main(){
	int i, j;
	cin >> nTestCase;
	//getline(cin, str);
	for(testCase=0; testCase<nTestCase; ++testCase){
		cin >> n;
		Loop(i, n){
			scanf("%s", mat[i]);
		}
		ans = 0;
		Loop(i, n-1){
			LOOP(j, i, n){
				if(isThisRowOk(j, i)){
					strcpy(row, mat[j]);
					while(j>i){
						strcpy(mat[j], mat[j-1]);
						ans++;
						j--;
					}
					break;
				}
			}
		}
		cout << "Case #" << testCase+1 << ": " << ans << endl;
	}

	return 0;
}
