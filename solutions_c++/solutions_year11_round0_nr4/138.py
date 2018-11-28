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
	li t,n,tmp;
	ifs>>t;
	rep(stage,t){
		ifs>>n;
		li res=n;
		rep(i,n){
			ifs>>tmp;
			if(i==tmp-1) res--;
		}
		ofs<<"Case #"<<stage+1<<": "<<res<<endl;
	}
}
