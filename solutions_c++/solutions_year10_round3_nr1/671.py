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
		int n;
		fin>>n;
		vi v(n),u(n);
		f(i,n)
			fin>>v[i]>>u[i];
		int c=0;
		f(i,n){
			for(int j=i+1;j<n;j++){
				if((v[i]>v[j] && u[j]>u[i])|| (v[i]<v[j]&& u[i]>u[j]))
					c++;
			}
		}
		fout<<"Case #"<<k+1<<": "<<c<<endl;

		

	}

}

