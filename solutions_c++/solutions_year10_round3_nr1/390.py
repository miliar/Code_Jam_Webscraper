#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int a[1001], b[1001];
int n;

void mysort(){
	int tmp;
	for(int i=0;i<n; i++){
		for(int j=0; j<n-i-1; j++){
			if(a[j] > a[j+1]){
				//swap
				tmp = a[j];
				a[j] = a[j+1];
				a[j+1] = tmp;

				tmp = b[j];
				b[j] = b[j+1];
				b[j+1] = tmp;
			}
		}
	}
	/*
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}*/
}

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;
	fin>>t;
	for(int ti=1; ti<=t; ti++){
		int cnt=0;
		fin>>n;
		for(int ni=0; ni<n; ni++){
			fin>>a[ni]>>b[ni];
		}
		mysort();
		//solve
		for(int i=0;i<n;i++){
			for(int j=0;j<i;j++){
				if(b[i] < b[j]){
					cnt++;
				}
			}
		}
		fout<<"Case #"<<ti<<": "<<cnt<<endl;
	}
}