
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
long a1,b1,pi,tp[4],dx,dy;
pair<long,long> p1,p2,p0;

long s,s1,s2,d2,d3,d1,pmax;
vector <pair<long, pair<long,long> > > vb0;
vector<double> vx,vx2,vk,vk1,vk2;
vector<double> va,vb;
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
string we,we2;
vector<string> vn,vn2;
stack<long> stos;
long ta[110][110];
long a,b,c,d;


int main() {  
	freopen( "c:\\wojtek\\uva\\uva\\debug\\a0.in", "rt", stdin); 
	//	long czas=clock(); 
	//pi=2*acos(0.0);
	//vp0.clear();
	//vp0=pd0(); 
	
 
	cin>>t;
	for(cas=1;cas<=t;cas++){

		cin>>r>>c;
		vn.clear();
		
		for(i=0;i<r;i++){
			cin>>we;
			vn.push_back(we);
		}
		z=1;
		for(i=0;i<r-1;i++){
			for(j=0;j<c-1;j++){

			
				if(vn[i][j]=='#'){
					if(vn[i][j+1]=='#'&&vn[i+1][j]=='#'&&vn[i+1][j+1]=='#'){
						vn[i][j]='/';
						vn[i+1][j+1]='/';
						vn[i][j+1]='\\';
						vn[i+1][j]='\\';
					}
					else {
						z=0;
						break;
					}

				}
				
			}
			if(vn[i][c-1]=='#'){
				z=0;
				break;
			}
			if(z==0)
				break;
		}
		i=r-1;
		for(j=0;j<c;j++){
			if(vn[i][j]=='#'){
				z=0;
				break;
			}
		}
		


		cout<<"Case #"<<cas<<": "<<endl;
		if(z==0)
			cout<<"Impossible"<<endl;
		else {
			for(i=0;i<r;i++){
				
				cout<<vn[i]<<endl;
			}
		}
	}
	
	 
		
	
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

	
	//printf("%.6lf\n",px);
		
	return 0;

} 
