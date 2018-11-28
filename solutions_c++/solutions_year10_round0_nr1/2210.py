#include<iostream>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
using namespace std;
int main()
{
 ifstream in("input.txt");
 ofstream out("output.txt");
int T,test;
 in >> T;
 long long res[40];
 res[0]=0;
 res[1]=1;
 for (int i=2;i<31;i++) res[i]=1+2*res[i-1];
 for (test=0;test<T;test++)
 {
	 int N,K;
	 in >> N >> K;
	 if (K%(res[N]+1)==res[N]) 
		 out << "Case #" << test+1 << ": ON";
	 else
		 out << "Case #" << test+1 << ": OFF";
	 if (test+1<T) out << endl;
 }
 return 0;
}