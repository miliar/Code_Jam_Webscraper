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

char wex[1000];
string we,s1,s2;
vector<string> w1,w2;
vector<vector<string> > vs;
int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);
	 
	
	//scanf("%ld",&t);
	cin>>t; 
	for(cas=1;cas<=t;cas++){  
		vs.clear();
		//scanf("%s",&we);
		cin>>n>>m;
		for(i=0;i<n;i++){
			cin>>wex;
			we=wex;
			k=1;
			w1.clear();
			d=we.find("/",k);
			while(d!=string::npos){
				s1=we.substr(k,d-k);
				w1.push_back(s1);
				k=d+1;
				d=we.find("/",k);
			}
			s1=we.substr(k);
			w1.push_back(s1);
			vs.push_back(w1);
		}
		b=0;
		for(i=0;i<m;i++){
			//we.clear();
			cin>>wex;
			
			we=wex;
			k=1;
			w1.clear();
			d=we.find("/",k);
			while(d!=string::npos){
				s1=we.substr(k,d-k);
				w1.push_back(s1);
				k=d+1;
				d=we.find("/",k);
			}
			s1=we.substr(k);
			w1.push_back(s1);

			

			k1=w1.size();
			k=k1;
			for(j=0;j<n;j++){
				k2=vs[j].size();
				for(i1=0;i1<min(k1,k2);i1++){
					if(w1[i1].compare(vs[j][i1])==0){
						if(k1-i1-1<k){
							k=k1-i1-1;
						}
					}
					else
						break;
				}
				
			}
			b+=k;
			vs.push_back(w1);
			n++;
		}
		cout<<"Case #"<<cas<<": "<<b<<endl;
	}



	
		


//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
