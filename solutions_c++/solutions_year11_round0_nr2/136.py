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

	int t;
	ifs>>t;
	rep(stage,t){
		int c,d,len;
		string str,_base="QWERASDF";
		map<char,int> base;
		rep(i,sz(_base)) base[_base[i]]=i;
		char combine[10][10];
		bool opp[10][10];
		rep(i,10)rep(j,10) opp[i][j]=false;
		rep(i,10)rep(j,10) combine[i][j]='*';
		ifs>>c;
		rep(i,c){
			ifs>>str;
			combine[base[str[0]]][base[str[1]]]=str[2];
			combine[base[str[1]]][base[str[0]]]=str[2];
		}
		ifs>>d;
		rep(i,d){
			ifs>>str;
			opp[base[str[0]]][base[str[1]]]=true;
			opp[base[str[1]]][base[str[0]]]=true;
		}
		ifs>>len;
		ifs>>str;
		string res="";
		bool contain[8];
		rep(i,8) contain[i]=false;
		#define back(a) a[sz(a)-1]
		rep(i,sz(str)){
			if(sz(res)==0){
				res.pb(str[i]);
			}else{
				if(base.find(back(res))!=base.end() && base.find(str[i])!=base.end() &&
					combine[base[back(res)]][base[str[i]]]!='*'){
					back(res)=combine[base[back(res)]][base[str[i]]];
				}else{
					bool flag=false;
					if(base.find(back(res))!=base.end()){
						contain[base[back(res)]]=true;
					}
					res.pb(str[i]);
					rep(j,8)if(contain[j] && opp[j][base[str[i]]]){
						flag=true;
					}
					if(flag){
						rep(j,8) contain[j]=false;
						res.clear();
					}
				}
			}
		}
		ofs<<"Case #"<<stage+1<<": [";
		rep(i,sz(res)){
			if(i!=0) ofs<<", "<<res[i];
			else ofs<<res[i];
		}
		ofs<<"]"<<endl;
	}
}
