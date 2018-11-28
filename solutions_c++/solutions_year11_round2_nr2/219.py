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
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	  FILE *out;
    out = fopen( "output.txt", "w" );
	
	li STAGE,num;
	ifs>>STAGE;
	rep(stage,STAGE){
		double pos[1000005],dis,p;
		ifs>>num>>dis;
		li n=0;
		rep(i,num){
			li tmp;
			ifs>>p>>tmp;
			rep(j,tmp) pos[n+j]=p;
			n+=tmp;
		}
		double low=0,high=(double)10000000*(double)205;
		double d=100000;
		high=high*d;
		rep(i,200){
			double mid=(low+high)/2.0;
			double now=pos[0]-mid-dis-mid-dis-mid-dis;
			bool flag=false;
			rep(j,n){
				if(now+dis>pos[j]+mid){
					flag=true;
					break;
				}
				now=max(now+dis,pos[j]-mid);
			}
			if(flag) low=mid;
			else high=mid;
		}
    fprintf( out, "Case #%lld: %lf\n",stage+1, low );

	}
}
