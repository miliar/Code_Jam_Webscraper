// codejam.cpp : 定义控制台应用程序的入口点。
//


#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
#include <iomanip>
using namespace std;

long double p[100000];
long double correct[100000];

int main(){
	ifstream in;
	in.open("in");
	ofstream out;
	out.open("out");
	int t;
	in>>t;
	for(int l=0;l<t;l++){
		long double result=10000000;
		int a,b;
		in>>a>>b;
		for(int i=1;i<=a;i++) in>>p[i];
		correct[0]=1;
		for(int i=1;i<=a;i++){
			correct[i]=correct[i-1]*p[i];
		}
		double avg=correct[a]*(b-a+1)+(1-correct[a])*(b-a+2+b);
		if(avg<result) result=avg;
		avg=(2+b);
		if(avg<result) result=avg;
		for(int i=1;i<a-1;i++){
			avg=correct[a-i]*(b-a+i+i+1)+(1-correct[a-i])*(b-a+i+i+2+b);
			if(avg<result) result=avg;
		}
		out<<fixed<<setprecision(6);
		out<<"Case #"<<l+1<<": "<<result<<endl;
	}
	in.close();
	out.close();
	return 0;
}