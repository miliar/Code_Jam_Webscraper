#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <map>
#include <sstream>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int nn = 1; nn <= n; nn++){
		string str;
		cin >> str;
		string a = str;
		sort(str.begin(), str.end());
		int f = 0;
		do{
			//cout << str << endl;
			if(str[0] == '0')continue;
			if(f){
				f = 2;
				break;
			}
			if(a == str) f = 1;
		}while(next_permutation(str.begin(), str.end()));
		if(f == 1 || f==0){
			str += '0';
			sort(str.begin(), str.end());
			do{
				//cout << str << endl;
				if(str[0] == '0')continue;
				if(f)break;
				if(a == str) f = 1;
			}while(next_permutation(str.begin(), str.end()));
		}
		
		cout << "Case #" << nn << ": "<< str << endl;
	}
}
