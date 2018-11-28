#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <string>
#include <algorithm>
#include <cctype>
#include <climits>
#include <cassert>

#include<iostream> 

using namespace std; 

#define NN 41
char a[NN][NN];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin >> T;
	int cases=1;
	while(--T>=0){
		int n;
		cin >> n;
		for (int i = 0 ;i < n ;i++){
			for (int j = 0 ;j < n ;j++)
				cin >> a[i][j];
		}
		int op = 0;
		for (int i = 0 ;i < n ;i++){
			bool ok = true;
			for (int k = i+1 ;k < n ;k++){
				if (a[i][k]=='1'){
					ok = false;
					break;	
				}
			}
			if (!ok){
				int j = i+1;
				while (j < n){
					ok = true;
					for (int k = i+1 ;k < n ;k++){
						if (a[j][k]=='1'){
							ok = false;
							break;	
						}
					}
					if (ok)
						break;
					j++;	
				}
				while(j>i){
					char tmp[50];
					memcpy(tmp,a[j],sizeof(a[0]));
					memcpy(a[j],a[j-1],sizeof(a[0]));
					memcpy(a[j-1],tmp,sizeof(a[0]));
					op++;
					j--;
				}
			}
		} 
		cout << "Case #" << cases++ << ": " << op << endl;
	}
	
}
