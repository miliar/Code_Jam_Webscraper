#include "stdafx.h"
#include <iostream>
#include <cstdlib>
using namespace std;

const int MAX = 100;
char a[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 
	'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
char c[MAX];

int main(){
	freopen("test.txt", "r", stdin);
	freopen("result.txt", "w", stdout);
	int n, i;

	cin>>n;
	getchar();
	for(i = 1; i <= n; i++){
		gets(c);
		for(int j = 0; j < strlen(c); j++){
			if(islower(c[j])){
				c[j] = a[c[j] - 'a'];
			}
		}
		cout<<"Case #"<<i<<": "<<c<<endl;
	}

	return 0;
}
