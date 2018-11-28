
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
long ta[5010];
pair<char,char> pc1,pc2;
vector<vector<pair<char,char> > >vvc1,vvc2;
vector<pair<char,char> > vc1,vc2;


int main() {  
	freopen( "c:\\wojtek\\uva\\uva\\debug\\B2.in", "rt", stdin); 
	//	long czas=clock(); 
	//pi=2*acos(0.0);
	//vp0.clear();
	//vp0=pd0(); 
	
 
	cin>>t;
	for(cas=1;cas<=t;cas++){
		vvc1.clear();
		vvc2.clear();
		vc1.clear();
		for(i=0;i<26;i++){
			vvc1.push_back(vc1);
			vvc2.push_back(vc1);
		}
		
		cin>>c;
		
		for(i=0;i<c;i++){
			cin>>we;
			vvc1[we[0]-'A'].push_back(MP(we[1],we[2]));
			vvc1[we[1]-'A'].push_back(MP(we[0],we[2]));
		}
		cin>>d;
		for(i=0;i<d;i++){
			cin>>we;
			vvc2[we[0]-'A'].push_back(MP(we[1],'A'));
			vvc2[we[1]-'A'].push_back(MP(we[0],'A'));
		}
		cin>>n>>we;
		wex.clear();
		wex+=we[0];
		for(i=1;i<n;i++){
			k1=wex.size();
			z=1;
			if(k1>0){
				k1--;
				//wex+=we[i];
				k=vvc1[we[i]-'A'].size();
				z=1;
				for(j=0;j<k;j++){
					if(vvc1[we[i]-'A'][j].first==wex[k1]){
						wex.erase(wex.end()-1);
						wex+=vvc1[we[i]-'A'][j].second;
						z=0;
						break;
					}
				}
				if(z==1){
					k=vvc2[we[i]-'A'].size();
					k1=wex.size();
					for(j=0;j<k;j++){
						for(i1=0;i1<k1;i1++){
							if(vvc2[we[i]-'A'][j].first==wex[i1]){
								wex.clear();
								
								z=0;
								break;
							}
						}
						if(z==0)
							break;
					}
				}
			}
			if(z==1)
				wex+=we[i];

		}

	


		cout<<"Case #"<<cas<<": [";
		k=wex.size();
		if(k>0){ 
			cout<<wex[0];
			for(i=1;i<k;i++){
				cout<<", "<<wex[i];
			}
		}
		cout<<"]"<<endl;

	}
	
	
		
	
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

	
	//printf("%.6lf\n",px);
		
	return 0;

} 
