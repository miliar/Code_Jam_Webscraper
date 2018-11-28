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

using namespace std; 
 
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
#define INF 		INT_MAX
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))
#define REP(a,x)	for(int a=0;a<x;a++)
#define REP1(a,x)	for(int a=1;a<=x;a++)
#define MP 		make_pair

typedef long long 	ll;
typedef vector<int> 	vi;
typedef pair<int,int> 	pii;
typedef vector<pair<int,int> >	vpii;

long amax,i,k,i2,i1,r,k1,j,m,l,n,i3,j10,j2,j3,a1,a2,a3; 
long cas,c,a,k2,z,t,ng,b,p,s;
pair<long,long> p2;
long ta[20000],td[20000],tb[20000],tc[20000],tg[20000];
vector<pair<long,long> > vp;
vector<long> va,vk1,vk2,vk3;
vector<vector<int> > vb;
vi vk,vh,vr;
double pi,dx,ax;


int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	//	int czas=clock(); 
	pi=2*acos(0.0);
	 
	
	//scanf("%ld",&t);
	cin>>t; 
	for(cas=1;cas<=t;cas++){  
		
		cin>>n>>s>>p;


		a1=0;
		a2=0;
		a=p;
		b=p;
		if(p-1>0)
			a+=2*(p-1);
		if(p-2>0)
			b+=2*(p-2);
		for(i=0;i<n;i++){ 
			cin>>k;
			if(k>=a)
				a1++;
			else if(k>=b)
				a2++;
		}
		a1+=min(s,a2);
		cout<<"Case #"<<cas<<": "<<a1<<endl;

		
		
	}

		

//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
