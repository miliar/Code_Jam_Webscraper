#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define li		long long
#define rep(i,to)	for(li i=0;i<((li)to);i++)
#define pb		push_back
#define sz(v)		((li)v.size())

ofstream ofs("output.txt");
ifstream ifs("input.txt");
void print(string str,int num){
	if(str=="OK"){
		ofs<<"Case #"<<num<<": Possible"<<endl;
	}else{
		ofs<<"Case #"<<num<<": Broken"<<endl;
	}
}
int gcd(int a,int b){
	if(a%b==0) return b;
	return gcd(b,a%b);
}
int main(){
	li stage;
	ifs>>stage;
	rep(i,stage){
		li a,b,c;
		ifs>>a>>b>>c;
		if(c==100 || c==0){
			if(b==c) print("OK",i+1);
			else print("FALSE",i+1);
		}else{
			if(100/gcd(100,b)<=a) print("OK",i+1);
			else print("FALSE",i+1);
		}
	}
}
