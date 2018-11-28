#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <string>

using namespace std;

#define VI			vector<int>
#define VVI			vector<VI>

#define MCC			map<char,char>

int main(){
	ifstream cin("input.txt");
	ofstream cout("c.txt");
	int T;
	cin >> T;
	for(int cnt=1 ; cnt<=T ; cnt++){
		int A,B;
		int ans = 0;

		cin >> A >> B;
		int Mul = 10000000;
		while(A/Mul == 0)
			Mul /= 10;

		for(int n=A ; n<=B ; n++){
			map<int,int> done;
			for(int mul1=10,mul2=Mul ; n/mul1 ; mul1*=10,mul2/=10){
				int m = n/mul1 + ((n%mul1)*mul2);
				if(n<m && m<=B && !done[m]){
					ans++;
					done[m] = 1;
				}
			}
		}

		cout <<"Case #"<<cnt<<": "<< ans << endl;
	}
}