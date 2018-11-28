/*
 *      ID : pallab81
 *      PROG : snapper.cpp 
 *      LANG : C++ 
 *      DATE : 2010-05-08 
 *      "I have not failed, I have just found 10000 ways that won't work." Thomas Alva Edison
 */


//#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <functional>
#include <ctime>

using namespace std;
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VC vector<char>
#define VVC vector<VC >
#define VB vector<bool>
#define VVB vector<VB >
#define PAIR pair<int,int>
#define VP vector<PAIR >
#define fo(i,st,ed) for(int i = st; i < ed ; ++i)
#define L_P list<PAIR >
#define debug(x,y) if(x<0 || x>=y) { cerr<<x<<" Error in line : "<<__LINE__<<'\n' ; p; continue ; }
#define IO ifstream cin("A-small-attempt1.in") ; ofstream cout("A-small-attempt1.out");
#define CL(x) (double(x))/CLOCKS_PER_SEC
#define mk make_pair
#define f first
#define s second
#define pb push_back
#define SZ(X) (int)(X).size()
#define LN(X) (int)(X).length()


IO

VB light,connection;

inline void print(int n){
	fo(i,0,n){
		light[i]==true ? cout<<"LightOn " : cout<<"LightOff ";
		connection[i] == true ? cout<<"ConnectionOn\n" : cout<<"ConnectionOff\n" ;
	}
return ;
}

inline void update(int n){
	VB previous = connection;
	previous[0]=true;
	
	for(int i=0;i<n;i++){
		if(previous[i]){
			if(light[i]){
				light[i]=false;	
				connection[i+1] = connection[i+1]==true ? false : true ;
			}
			else{
				light[i]=true;
				connection[i+1]=true;
			}
		
		}
		else{
			break;
		}
	}

return ;
}

inline void doRest(int testCase){
	int totalN,totalT;	
	cin>>totalN>>totalT;
	
	light.assign(totalN+5,false);
	connection.assign(totalN+5,false);
	
	for(int i=1;i<=totalT;i++){
		update(totalN);
	}
	connection[0]=true;
	
	int i1 = count(connection.begin(),connection.begin()+totalN,false);
	int i2 = count(light.begin(),light.begin()+totalN,false);
	
	cout<<"Case #"<<testCase<<": ";
	if(i1==0 && i2==0){
		cout<<"ON\n";
	}
	else{
		cout<<"OFF\n";
	}
	
return ;
}

int main(){
	int testCase;
	cin>>testCase;
	for(int i=1;i<=testCase;i++){
		doRest(i);
	}
		
	return 0;	
}
