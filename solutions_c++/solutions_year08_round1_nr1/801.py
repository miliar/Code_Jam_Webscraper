#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <bitset>
#include <stack>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>

#define ALL(c) c.begin(),c.end()
#define pb push_back
#define For_iter(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end();++BB)

using namespace std;
int a[1000];
int b[1000];
int main()
{
     ifstream fin;
     ofstream fout;
     fin.open("A-small-attempt0.in");
     fout.open("result");
     int n;
     fin>>n;
     for(int i=0;i<n;i++){
	 	int k;
	 	fin>>k;
	 	for(int j=0;j<k;j++){
			fin>>a[j];
		}
		for(int j=0;j<k;j++){
			fin>>b[j];
		}
		for(int j=0;j<k;j++){
			int minA=j,minB=j;
			for(int p=j;p<k;p++){
				if(a[p]<a[minA]){
					minA=p;
				}
				if(b[p]<b[minB]){
					minB=p;
				}
			}
			int tempA,tempB;
			tempA=a[j];
			a[j]=a[minA];
			a[minA]=tempA;
			tempB=b[j];
			b[j]=b[minB];
			b[minB]=tempB;
		}
		int result=0;
		for(int j=0;j<k;j++){
			result+=a[j]*b[k-1-j];
		}
		fout<<"Case #"<<i+1<<": "<<result<<endl;
		cout<<result<<endl;
		for(int j=0;j<k;j++){
			cout<<a[j]<<' ';
		}
		cout<<endl;
		for(int j=0;j<k;j++){
			cout<<b[j]<<' ';
		}
		cout<<endl;

	 }
     if(!fin) cout<<"Cannot open!"<<endl;
     system("PAUSE");
     return 0; 
}
