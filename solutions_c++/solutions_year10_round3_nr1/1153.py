#include<iostream>
#include<fstream>
#include<functional>
using namespace std;
#define xin fin
#define xout fout
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("small_out.txt");
	int T,N,a[1003],b[1003],i,j;
	xin>>T;
	int s=0,result=0;
	while(T--)
	{
		s++;
		result=0;
		xin>>N;
		for (i=0;i<N;i++)
			xin>>a[i]>>b[i];
		for (i=0;i<N-1;i++)
			for (j=i+1;j<N;j++)
			{
				if ((a[i]-a[j])*(b[i]-b[j])<0) result++; 
			}
			xout<<"Case #"<<s<<": "<<result<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}