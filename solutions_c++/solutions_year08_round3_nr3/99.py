#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <fstream>
#include <sstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main(){
	int N,Test,n,m,X,Y,Z;
	long long A[1000],a[1000];
	unsigned long long d[1000];
	fin>>N;
	for (Test=1;Test<=N;Test++){
		fin>>n>>m>>X>>Y>>Z;
		for (int i=0;i<m;i++){
			fin>>A[i];
		}
		for (long long i=0;i<n;i++){
			a[i]=A[i%m];
			cout<<a[i]<<" ";
			A[i%m]=(X*A[i%m]+Y*(i+1))%Z;
		}
		memset(d,0,sizeof(d));
		d[0]=1;
		for (int i=1;i<n;i++){
			d[i]=1;
			for (int j=0;j<i;j++){
				if (a[j]<a[i]){
					d[i]+=d[j];
					d[i]%=1000000007;
				}
			}
		}
		long long res=0;
		for (int i=0;i<n;i++){
			res+=d[i];
			res%=1000000007;
		}
		fout<<"Case #"<<Test<<": "<<res<<endl;
		cout<<"Case #"<<Test<<": "<<res<<endl;
		cout<<endl;
		
	}
	fout.close();
	return 0;
}