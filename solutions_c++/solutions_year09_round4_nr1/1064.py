#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("a.in");
//#define cin fin

string data[40];
int raw[40];
char temp;

int main(){
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++){
		int n;
		cin>>n;
		for(int i = 0; i < n; i ++){
			cin>>data[i];
		}
		for(int i = 0; i < n; i ++){
			raw[i]=n;
			for(int j = n-1; j >= 0; j --){
				raw[i]--;
				if(data[i][j]=='1'){
					break;
				}
			}
		}
		int steps;
		steps = 0;
		for(int i = 0; i < n; i ++){
			for(int j = i; j < n; j ++){
				if(raw[j] <= i){
					while(j>i){
						int temp = raw[j];
						raw[j] = raw[j-1];
						raw[j-1] = temp;
						steps ++;
						j--;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n", t, steps);
	}
	return 0;
}
