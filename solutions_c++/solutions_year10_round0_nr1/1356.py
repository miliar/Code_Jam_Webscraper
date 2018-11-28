#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<list>
#define f(i,n) for(int i=0;i<n;i++)
#define vi vector<int>
#define vs vector<string>
#define p_b push_back
using namespace std;
//stringstream ss (stringstream::in | stringstream::out);

int main(){
	fstream fin,fout;
	fin.open ("input.txt", fstream::in | fstream::out);
	fout.open ("output.txt", fstream::in | fstream::out);
	int t;
	fin>>t;
	f(k,t){
		int n,K;
		fin>>n>>K;
		int x=(int)pow(2.0,n);
		if(K%x==x-1){
			fout<<"Case #"<<k+1<<": ON"<<endl;
		}
		else 
			fout<<"Case #"<<k+1<<": OFF"<<endl;

	}

}


 