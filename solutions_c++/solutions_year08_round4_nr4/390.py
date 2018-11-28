#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <sstream>
using namespace std;

ifstream fin("D-small-attempt0.in");
//ifstream fin("C-large.in");
ofstream fout("D.txt");

int main(){
	int N;
	fin>>N;
	for (int Test=1;Test<=N;Test++){
		int K;
		fin>>K;
		string str;
		fin>>str;
		int a[5];
		for (int i=0;i<K;i++){
			a[i]=i;
		}
		int result=100000;
		do{
			string nstr="";
			for (int i=0;i<str.size()/K;i++){
				for (int j=0;j<K;j++){
					nstr+=str[i*K+a[j]];
				}
			}
			int res=1;
			for (int i=1;i<nstr.size();i++){
				if (nstr[i]!=nstr[i-1]){
					res++;
				}
			}
			if (res<result) result=res;
		}while (next_permutation(a,a+K));
		fout<<"Case #"<<Test<<": "<<result<<endl;
	}
	fout.close();
	return 0;
}