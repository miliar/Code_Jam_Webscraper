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
		if(str.length() == 1){
			cout << "Case #" << nn << ": "<< 1 << endl;
			continue;
		}
		string str2 = str;
		sort(str.begin(), str.end());
		map<char, int> data;
		int nnn=0;
		for(int i = 0; i < str2.length(); i++){
			if(i==0){
				data[str2[i]] = 1;
			}
			else{
				if(data.find(str2[i]) == data.end()){
					data[str2[i]] = nnn;
					nnn++;
					if(nnn == 1) nnn++;
				}
			}
		}
		if(nnn < 2)nnn = 2;
		//cout << data['0'] << endl;
		int sum=0;
		for(int i = 0; i < str2.length(); i++){
			sum += data[str2[i]]*(double)pow((double)nnn, (double)str2.length()-1-i);
			//cout << sum << endl;
		}
		cout << "Case #" << nn << ": "<< sum << endl;
	}
}
