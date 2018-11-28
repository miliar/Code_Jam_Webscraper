#include <cstdio>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

bool mark[2000];
int f[2000];
int test;
int sum;
int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	cin>>test;
	for (int i=0;i<test;i++){
		int n;
		cin>>n;
		sum = 0;
		for (int j=1;j<=n;j++){
			cin>>f[j];
			if (f[j]!=j)
				sum++;
		}
		cout<< "Case #"<<i+1<<": "<<sum<<".000000"<<endl;
		
	}
}