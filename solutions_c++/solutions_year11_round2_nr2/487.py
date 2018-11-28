//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

//#pragma warning(disable:4786)
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (int)(c).size()
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define LL long long
#define FOR(_name,_A,_B)  for(int _name=_A;_name<=(_B);_name++)

int C,D;
int T;
int P[203],nV[203],cas=1;

bool fun(double Time){


	int i,tmpV[203];
	for(i=0;i<C;i++)
		tmpV[i]=nV[i];

	i=0;
	double pos;

	pos=P[0]-Time;
	tmpV[0]--;
	if(tmpV[i]==0) i++;
	
	while(i<C){
		double t=pos+D;
		if(fabs(P[i]-t)<=Time){
			pos+=D;
		}
		else {
		
			if(t<P[i]){
				pos=P[i]-Time;
			}
			else{
			
				
				 return false;
			}
			/*
			if( fabs((P[i]-Time)-pos)>=D){
				pos=(P[i]-Time);
			}
			else if(fabs((P[i]+Time)-pos)>=D){
				pos=(P[i]+Time);			
			}
			else {
				return false;
			}
			*/
		}

		tmpV[i]--;
		if(tmpV[i]==0)
			i++;
	}

	return true;
}
double bin(double low,double high,int d){

	double mid=(low+high)/2.0;

	if(fabs(high-low)<1e-7|| d>69)
		return mid;
	if(fun(mid)==true)
		return bin(low,mid,d+1);
	return bin(mid,high,d+1);

}
void reset(){}
void process(){	

	double res;
	LL h=1000000;
	h=h*h;
	res=bin(0,h,0);
	printf("Case #%d: %.7lf\n",cas++,res);

}
int main()
{
	freopen("Source/B-large.in","rt",stdin);	
	freopen("Source/out.o","wt",stdout);
	cin>>T;
	while(T--){
	
	
		cin>>C>>D;
		for(int i=0;i<C;i++)
			cin>>P[i]>>nV[i];
		process();
	
	}
	
		
	return 0;
}
