// GCJ_A.cpp: определяет точку входа для консольного приложения.
//

//#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <string> 
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ter;
	cin >> ter;
	for (int terr = 1; terr <= ter; terr++) {
		int n, b[42], res = 0;
		string a[42];
		string d;
		cin >> n;
		for(int i = 1; i <= n; i++){
			//scanf("%s", &d);
			//a[i] = d;
			cin >> a[i];
		//	scanf("%s", &a[i]);
		}
		for(int i = 1; i <= n; i++){
			b[i] = a[i].find_last_of("1") + 1;
		}
		for(int i = 1; i <= n; i++){
			if (b[i] > i){
				for(int j = i + 1; j <= n; j++){
					if (b[j] <= i){
						res += j - i;
						for(int k = j; k > i; k--){
//							swap(a[k], a[k-1]);
							swap(b[k], b[k-1]);
						}
						break;
					}
				}
			}
		}

		printf("Case #%d: %d\n", terr, res);
	}
	return 0;
}

