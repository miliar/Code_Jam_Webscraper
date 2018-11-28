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

int main(){
	ofstream ofs;
	ofs.open("output.txt");
	ifstream ifs;
	ifs.open("input.txt");
	li t;
	ifs>>t;
	rep(stage,t){
		li bit=0,sum=0,mini=10000000,n,tmp;
		ifs>>n;
		rep(i,n){
			ifs>>tmp;
			sum+=tmp;
			bit^=tmp;
			mini=min(tmp,mini);
		}
		if(bit==0){
			ofs<<"Case #"<<stage+1<<": "<<sum-mini<<endl;
		}else{
			ofs<<"Case #"<<stage+1<<": NO"<<endl;
		}
	}
}
