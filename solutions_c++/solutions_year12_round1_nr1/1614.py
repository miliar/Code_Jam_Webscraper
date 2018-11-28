#pragma comment(linker, "/STACK:268435456")

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <map>
#include <bitset>
#include <math.h>
#include <stdio.h>
#include <limits.h>
#include <stack>

using namespace std;

ofstream myout("A-small-attempt0 (1).out");
ifstream myin("A-small-attempt0 (1).in");

void main2(){
	double p[100001],sol[100001];
	double temp = 1,prev = 1,next;
	int a,b;
	myin >> a >> b;
	for(int i=0 ; i<a ; i++){
		myin >> p[i];
		sol[i+1] = (1-p[i])*temp;
		temp*=p[i];
	}
	sol[0]=temp;
	double max = b+2;
	temp = (b-a+1)*sol[0] + (2*b-a+2)*(1-sol[0]);
	if(temp < max) max = temp;
	for(int i=1 ; i<a ; i++){
		if(p[a-i-1]!=1){
			temp = sol[a-i]/(1-p[a-i-1]) * p[a-i-1];
			temp = (2*i+(b-a+1))*temp + (2*i+2*b-a+2)*(1-temp);
		}
		else{
			temp = (2*i+2*b-a+2);
		}
		if(temp < max) max = temp;
		
	}
	temp = a+b+1;
	if(temp < max) temp = max;
	//myout.precision(6);
	myout << max;
}

//Multiple test cases
int main(){
	int t;
	myin >> t;
	myout.precision(6);
	//myout.setf(
	myout.setf(ios::fixed,ios::floatfield);
	for(int i=1 ; i<=t ; i++){
		myout << "Case #" << i << ": ";
		main2();
		myout << endl;
	}
}