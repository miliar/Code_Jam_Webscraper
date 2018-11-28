#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;
int test;
int s;
int n;
int cnt;
int f[1001];
int x;
int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	cin >>test;
	while (test--){
		s=0;
		cnt++;
		cin>>n;
		x=0;
		int min = 2147483647;
		for (int i=0;i<n;i++){
			cin>>f[i];
			s+=f[i];
			x = x xor f[i];
			if (f[i]<min)
				min = f[i];
		}
		if (x==0)
			cout<<"Case #"<<cnt<<": "<<s-min<<endl;
		else
			cout<<"Case #"<<cnt<<": "<<"NO"<<endl;
	}
}