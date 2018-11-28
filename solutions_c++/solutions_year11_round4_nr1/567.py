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
	ifstream ifs;
	ofstream ofs;
	ifs.open("input.txt");
	ofs.open("output.txt");
	FILE *fp;
	FILE *f;
	f=fopen("input.txt","r");
	fp=fopen("output.txt","w");
	
	li t;
//	ifs>>t;
	fscanf(f,"%lld",&t);
	rep(stage,t){
		double len,walk,run,time;
		li n;
		double sum=0;
//		ifs>>len>>walk>>run>>time>>n;
		fscanf(f,"%lf%lf%lf%lf%lld",&len,&walk,&run,&time,&n);
//		cout<<stage<<":"<<len<<" "<<walk<<" "<<run<<" "<<time<<" "<<n<<endl;
		vector<pair<double,double> > q;
		rep(i,n){
			double start,end,speed;
//			ifs>>start>>end>>speed;
			fscanf(f,"%lf%lf%lf",&start,&end,&speed);
			q.pb(make_pair(speed,end-start));
			sum+=end-start;
		}
		q.pb(make_pair(0,len-sum));
		sort(q.begin(),q.end());
		double res=0;
		rep(i,sz(q)){
			if(time>q[i].second/(run+q[i].first)){
				time-=q[i].second/(run+q[i].first);
				res+=q[i].second/(run+q[i].first);
			}else{
				q[i].second-=(run+q[i].first)*time;
				res+=time;
				time=0;
				res+=q[i].second/(q[i].first+walk);
			}
		}
		fprintf(fp,"Case #%lld: %.20lf\n",stage+1,res);
	}
	ifs.close();
	ofs.close();
}
