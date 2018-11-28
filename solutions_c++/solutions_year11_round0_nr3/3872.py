#include<STDLIB.H>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<cmath>
#include<time.h>
#include<set>
#include<algorithm>
#include<fstream>
using namespace std;

int mas[100000];

int main(){
ofstream file("D:\\1.txt");
int t,n;
cin >> t;
for (int test=0; test<t; test++){
	cin >> n;
	for (int i=0; i<n; i++)
		cin >> mas[i];
	int c=0;
	for (int i=0; i<n; i++)
		c=c^mas[i];
	if (c!=0){
		file<< "Case #" << test+1 << ": " << "NO" << endl;
		continue;
	}
	long long sum=0;
	long long min=999999999999;
	for (int i=0; i<n; i++){
		sum+=mas[i];
		if(min>mas[i]) min=mas[i];
	}
	file << "Case #" << test+1 << ": "<< sum-min << endl;
}
file.close();
return 0;
}
