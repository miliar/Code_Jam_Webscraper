
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <map>  
#include <string>
#include <vector> 
#include <list> 
#include <iostream>  
#include <sstream> 
#include <queue>
#include <algorithm>
#include <stack>

using namespace std;  
 

long i,k,i2,i1,k1,k0,j,m,n,i3,j10,j2,j3,i4; 
long cas,k2,z,np,np2,t; 
long a,b,c,d,a1,b1,pi,tp[4],dx,dy;
pair<long,long> p1,p2,p0;

long s,s1,s2,d2,d3,d1,pmax;
vector <pair<long, pair<long,long> > > vb;
vector<long> vx,vx2,vk,vk1,vk2;
vector<pair<long,long> > vp,vp0;
vector<vector<long> > vd,vg;
vector<pair<long,long> > vpx,vpx2;
pair<pair<long,long>,pair<long,long> > pp1,pp2;
vector<pair<pair<long,long>,pair<long,long> > > vpp;
long r,a2,a3,t1,t2;

vector<pair<double,double> > vpd;
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
#define INF 		INT_MAX
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))
#define REP(a,x)	for(int a=0;a<x;a++)
#define REP1(a,x)	for(int a=1;a<=x;a++)
#define MP 		make_pair
string we,wex;
vector<string> vn,vn2;

stack<long> stos;
long ta[1010];
pair<char,char> pc1,pc2;
vector<vector<pair<char,char> > >vvc1,vvc2;
vector<pair<char,char> > vc1,vc2;

long czek(void){
	long i,a1,a2;

	a1=0;
	a2=0;
	for(i=0;i<n;i++){
		if(ta[i]==0)
			a2^=vx[i];
		else
			a1^=vx[i];
	}
	if(a1==a2)
		return 1;
	return 0;
}
long roz(void){
	long i,a1,a2;

	a1=0;
	a2=0;
	for(i=0;i<n;i++){
		if(ta[i]==0)
			a2+=vx[i];
		else
			a1+=vx[i];
	}
	if(a1>a2)
		return a1;
	return a2;
}
void dalej(long z){
	long i;
	if(z>n/2)
		return;
	for(i=0;i<n;i++){
		if(ta[i]=0){
			ta[i]=1;
			if(czek()){
				d=roz();
				if(d>b)
					b=d;
			}
			dalej(z+1);
			ta[i]=0;
		}
	}
} 

int main() {  
	freopen( "c:\\wojtek\\uva\\uva\\debug\\C1.in", "rt", stdin); 
	//	long czas=clock(); 
	//pi=2*acos(0.0);
	//vp0.clear();
	//vp0=pd0();  
	 
 
	cin>>t;
	for(cas=1;cas<=t;cas++){
		
		CL(ta,0);
		cin>>n;
		vx.clear();
		a=0;
		b=0;
		for(i=0;i<n;i++){
			cin>>k;
			vx.push_back(k);
			a+=k;
		}
		SORT(vx);
		if(czek())
			b=a-vx[0];

		

		cout<<"Case #"<<cas<<": ";
		if(b==0)
			cout<<"NO"<<endl;
		else
			cout<<b<<endl;
		

	}
	
	
		
	
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

	
	//printf("%.6lf\n",px);
		
	return 0;

} 
