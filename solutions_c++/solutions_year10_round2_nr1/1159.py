/*
   compile with:
   g++ x.cpp -o x -lgmp -lgmpxx
*/
#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <deque>
#include <queue>
#include <map>

#include <gmpxx.h> /* The GNU Multiple Precision Arithmetic Library: gmplib.org */

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef mpz_class bint;

int case_number;
#define gout case_number++, cout<<"Case #"<<case_number<<": "

bool exists(string s, vector<vector<string> >* dirs, int level){
	if(dirs->size() <= level){
		dirs->push_back(vector<string>());
		return false;
	}
	foreach(i, (*dirs)[level])
		if((*i)==s) return true;
	return false;
}

void main2(){
	int i,N,M;
	string s,t;
	vector<vector<string> > dirs;

	cin>>N;
	cin>>M;

	vector<string> VN;
	REP(i,N){
		cin>>s;
		VN.push_back(s+'/');
	}
	vector<string> VM;
	REP(i,M){
		cin>>s;
		VM.push_back(s+'/');
	}

	foreach(i,VN){
		int level=0;
		s="";
		foreach(j,*i){
			if(*j=='/') { 
				if(s!=""){
					if(!exists(s,&dirs,level))
						dirs[level].push_back(s);
					level++;
				}
			}
			s+=*j;
		}
	}
	int retn=0;
	foreach(i,VM){
		int level=0;
		s="";
		bool good = true;
		foreach(j,*i){
			if(*j=='/') { 
				if(s!=""){
					if(!good){
						//cout<<"adding "<<s<<" at "<<level<<endl;
						retn++;
						if(dirs.size() <= level) dirs.push_back(vector<string>());
						dirs[level].push_back(s);
					} else {
						if(!exists(s,&dirs,level)){
						//cout<<"adding "<<s<<" at "<<level<<endl;
							retn++;
							good=false;
							dirs[level].push_back(s);
						}
					}
					level++;
				}
			} 
			s+=*j;
		}
	}
	gout<<retn<<endl;
}

int main(){
	int num_tests,i;
	cin>>num_tests;
	REP(i,num_tests) 
		main2();
	return 0;
}
