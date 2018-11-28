#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int N;
int ans[501][20];
char wel[20]={"welcome to code jam"};
string str;

int main(){
	cin>>N;
	getline(cin,str);
	for(int nCase=1;nCase<=N;nCase++){
		getline(cin,str);
//		memset(ans, 0, sizeof ans);
		ans[0][0] = 1;
		
		for(int i=0;i<str.length();i++){
			ans[i+1][0] = 1;
			for(int j=0;j<19;j++){
				ans[i+1][j+1] = ans[i][j+1];
				if(str[i]==wel[j]) ans[i+1][j+1] += ans[i][j];
				ans[i+1][j+1] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", nCase, ans[str.length()][19]);
	}

    return 0;
}

