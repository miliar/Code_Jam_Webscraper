#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 
#include <map>  
#include <string>
#include <vector> 
#include <iostream>  
#include <sstream> 
#include <queue>
#include <algorithm>

using namespace std; 
 
long i,k,i2,i1,r,k1,j,m,l,n,i3,j10,j2,j3,a1,a2,a3; 
long cas,s,c,a,b,k2,d,z,t,ng;
vector<pair <long,pair<long,long> > > tc;
vector<pair<long,long> > ta,tb;
pair <long,long> p1,p2,p3;
pair<long,pair <long,long> > px;
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))

int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);
	 
	
	scanf("%ld",&t);
	//cin>>t; 
	for(cas=1;cas<=t;cas++){  
		
		scanf("%ld",&n);
		ta.clear();
		tb.clear();
		tc.clear();
		for(i=0;i<n;i++){
			scanf("%ld%ld",&a,&b);
			p1.first=a;
			p1.second=i;
			ta.push_back(p1);
			p2.first=b;
			p2.second=i;
			tb.push_back(p2);

			p3.first=a;
			p3.second=b;
			px.first=a;
			px.second=p2;
			tc.push_back(px);
		}
		SORT(tc);
		d=0;
		ta.clear();
		for(i=0;i<n;i++){
			p1.second=i;
			
			px=tc[i];
			p2=px.second;
			p1.first=p2.first;
			ta.push_back(p1);
		}
		SORT(ta);
		for(i=0;i<n;i++){
			p1=ta[i];
			if(p1.second>i)
				d+=p1.second-i;
		}




		printf("Case #%ld: %ld\n",cas,d);
		//cout<<"Case #"<<cas<<": "<<b<<endl;
	}



	
		


//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
