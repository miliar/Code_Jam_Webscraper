#include<fstream>
#include<iostream>
using namespace std;
int a[20],n,maxim;
//s2,s3 patrick sums
int backtrack(int ord,int s1, int s2, int s3, int np)
{
	if( ord > n ) {
		if( s2 == s3 && s1 > maxim && np != 0 && np != n){
			maxim = s1;
		}
		return 0;
	}
	backtrack(ord + 1, s1 + a[ord], s2, s3 ^ a[ord],np);
	backtrack(ord + 1, s1, s2 ^ a[ord], s3,np+1);
}
int main()
{
	ifstream fin("date.in");
	ofstream fout("date.out");
	int t,i,k;
	fin>>t;
	for(k = 1; k <= t; k++) {
		maxim = -1;
		fin>>n;
		for(i = 1; i <= n; i++) {
			fin>>a[i];
		}
		backtrack(1,0,0,0,0);
		fout<<"Case #"<<k<<": ";
		if(maxim != -1)
			fout<<maxim;
		else
			fout<<"NO";
		fout<<'\n';
	}
}
