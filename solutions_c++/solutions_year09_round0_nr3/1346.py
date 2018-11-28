#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#define FOR(a, b, c) for(int a=b; a<=c; a++)

using namespace std;

string goal = " welcome to code jam";
const int G = 19;
int L;
string str;
const int MaxL = 5000;
int Dy[MaxL + 1][G + 1];
int ans;


void process(void){
	FOR(i, 1, L){
		if(goal[1] == str[i]){
			Dy[i][1] = 1;
		}
		FOR(j, 2, G){
			if(goal[j] == str[i]){
				int ret = 0;
				FOR(k, 1, i - 1){
					ret += Dy[k][j - 1];
					ret %= 10000;
				}
				Dy[i][j] = ret;
			}
		}
		ans += Dy[i][G];
		ans %= 10000;
	}
}

int main(void){
	int N;
	cin >> N;
	FOR(i, 1, N){
		getline(cin, str);
		if(str.size() == 0){
			getline(cin, str);
		}
		L = str.size();
		memset(Dy , 0 , sizeof(Dy));
		str = " " + str;
		ans=0;
		process();
		char output[1000];
		sprintf(output, "Case #%d: %04d" , i, ans);
		cout << output << endl;
	}
	return 0;
}
