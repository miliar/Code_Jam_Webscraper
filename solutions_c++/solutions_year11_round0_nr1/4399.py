#include <iostream>
#include <fstream>
#include <queue>
#include <cmath>
using namespace std;
#define forn(i,s,e) for(int i=s;i<e;i++)
int main(int argc,char* argv[]){
	int T;
	ifstream fin(argv[1],ios::in);
	fin>>T;
	forn(i,0,T){
		std::cout<<"Case #"<<i+1<<": ";
		int N;
		fin>>N;
		queue<int>  O,B,ALL;
		forn(j,0,N){
			char o;int k;
			fin>>o>>k;
			if(o=='O'){O.push(k);ALL.push(0);}
			else if(o=='B'){B.push(k);ALL.push(1);}
		}
		//cout<<"("<<O.size()<<" "<<B.size()<<" "<<ALL.size()<<")";
		int i=1,j=1,t=0,ni=1,nj=1,task=0;
		if(!ALL.empty())task=ALL.front();
		if(!O.empty())ni=O.front();
		if(!B.empty())nj=B.front();
		while(!ALL.empty()){
				//cout<<"\n{"<<task<<" "<<i<<" "<<ni<<" "<<j<<" "<<nj<<" "<<t<<"}";
				if(task==0){
					if(i==ni){
						t++;
						if(j<nj)j++;
						else if(j>nj)j--;
						O.pop();
						ALL.pop();
						if(!O.empty())ni=O.front();
						if(!ALL.empty())task=ALL.front();
						continue;
					}
				}
				else if(task==1){
					if(j==nj){
						t++;
						if(i<ni)i++;
						else if(i>ni)i--;
						B.pop();
						ALL.pop();
						if(!B.empty())nj=B.front();
						if(!ALL.empty())task=ALL.front();
						continue;
					}
				}
				t++;
				if(i<ni)i++;
				else if(i>ni)i--;
				if(j<nj)j++;
				else if(j>nj)j--;
		};
		std::cout<<t<<"\n";
	}
	return 0;
}