
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
#define vi vector<int>
#define vvi vector<vector<int> >
#define vii vector<pair<int,int> >
#define vvii vector<vector<pair<int,int> > >
#define pii pair<int,int>
#define vs vector<string>

int i,k,j,n,r,c,i1,m,s,g,b0; 
int cas,a,b,z,w,d,h,t;
int amin,amax,bmin,bmax;

vii vp;
vvii vz; 
pii p1,p2;
 
string we,we1,we2,wex;
vi vk,va,vb;
vs tt;


int main() { 
	freopen( "c:\\wojtek\\uva\\uva\\debug\\tal0.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);

	//d=1000000007;
	
	
	cin>>t;


	for(cas=1;cas<=t;cas++){
		tt.clear();
		a=0;
		for(i=0;i<4;i++){
			cin>>we;
			tt.push_back(we);
		}

		for(i=0;i<4;i++){
			z=1;
			for(j=0;j<4;j++){
				if(tt[i][j]!='X'&&tt[i][j]!='T'){
					z=0;
					break;
				}
			}
			if(z==1){
				a=1;
				break;
			}
			z=1;
			for(j=0;j<4;j++){
				if(tt[i][j]!='O'&&tt[i][j]!='T'){
					z=0;
					break;
				}
			}
			if(z==1){
				a=2;
				break;
			}
				

		}
		if(a==0){
			for(j=0;j<4;j++){
				z=1;
				for(i=0;i<4;i++){
					if(tt[i][j]!='X'&&tt[i][j]!='T'){
						z=0;
						break;
					}
				}
				if(z==1){
					a=1;
					break;
				}
				z=1;
				for(i=0;i<4;i++){
					if(tt[i][j]!='O'&&tt[i][j]!='T'){
						z=0;
						break;
					}
				}
				if(z==1){
					a=2;
					break;
				}

				
			}
		}
		if(a==0){

			//for(j=0;j<4;j++){
				z=1;
				for(i=0;i<4;i++){
					if(tt[i][i]!='X'&&tt[i][i]!='T'){
						z=0;
						break;
					}
				}
				if(z==1){
					a=1;
				//	break;
				}
				z=1;
				for(i=0;i<4;i++){
					if(tt[i][i]!='O'&&tt[i][i]!='T'){
						z=0;
						break;
					}
				}
				if(z==1){
					a=2;
				//	break;
				}
				
			//}
				z=1;
				for(i=0;i<4;i++){
					if(tt[i][3-i]!='X'&&tt[i][3-i]!='T'){
						z=0;
						break;
					}
				}
				if(z==1){
					a=1;
				//	break;
				}
				z=1;
				for(i=0;i<4;i++){
					if(tt[i][3-i]!='O'&&tt[i][3-i]!='T'){
						z=0;
						break;
					}
				}
				if(z==1){
					a=2;
				//	break;
				}
		}

		if(a==0){
			for(i=0;i<4;i++){
				for(j=0;j<4;j++){
					if(tt[i][j]=='.')
						a=3;
				}
			}
		}
		if(a==0)
			cout<<"Case #"<<cas<<": "<<"Draw"<<endl;
		else if(a==1)
			cout<<"Case #"<<cas<<": "<<"X won"<<endl;
		else if(a==2)
			cout<<"Case #"<<cas<<": "<<"O won"<<endl;
		else
			cout<<"Case #"<<cas<<": "<<"Game has not completed"<<endl;


 



	
	}

	
		
//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
