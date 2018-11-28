#include <stdio.h>
#include <string>
#include <iostream>
#include <string.h>
#define Eo(x) { cerr << #x << " = " << x << endl;}
using namespace std;
int mas[1000][1000];
int main(){
	int n;
	string q = "welcome to code jam";
//	string q = "abc";
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&n);
	string s;
	for ( int t = 0; t < n; t++){
		getline(cin, s);
		int l = s.size();
		int m = q.size();
		memset(mas,0,sizeof(mas));
		mas[0][0] = 1;
		for ( int i = 0; i < l; i++)
			for ( int j = 0; j <= m ; j++)
			if (mas[i][j]){
				mas[i + 1][j] = (mas[i + 1][j] + mas[i][j]) % 1000;
				if (j < m && s[i] == q[j]){
				mas[i + 1][j + 1] = (mas[i + 1][j + 1] + mas[i][j]) % 1000;
				}
			}
		cout << "Case #" << t + 1 << ": "<< mas[l][m]/ 1000 << (mas[l][m] % 1000) /100 << (mas[l][m] % 100) /10 << (mas[l][m] % 10) << endl;

	}
	return 0;
}
