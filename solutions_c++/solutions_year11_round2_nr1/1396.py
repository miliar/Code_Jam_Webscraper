#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <math.h>
#include <map>
#include <set> 
#include <queue>
#define  rep(i,a,b) for ( int i = a; i<=b; i++ )
const double EPS = 1E-8; 
const double PI  = 3.14159265; 
const int dx[4]={0,1,0,-1};
const int dy[4]={1,0,-1,0};

using namespace std; 

typedef  vector<int> VI; 
typedef  vector<VI>  VV; 
typedef  string      SS; 
typedef  vector<SS> VS; 
typedef  long long   LL;
typedef  map<int,int>MII;
typedef  priority_queue<int> maxpq; 
typedef  priority_queue<int,VI, greater<int>> minpq;
int T; 
vector<SS> A; 
double WP[1000],OWP[1000],OOWP[1000]; 
int N; 
void count_WP(){
	double x=0;double y; 
	rep(i,0,N-1){
		x=0; 
		y=0; 
		rep(j,0,N-1){
			if (A[i][j]=='1') x+=1;  
			if (A[i][j]!='.') y+=1; 
		}
		WP[i]=x/y; 
	}
}
double wp1(int x, int y){
	double i,j;
	i=0;j=0; 
	rep(k,0,N-1){
		if (A[x][k]!='.' && k!=y) {
			j+=1; 
		}
		if (A[x][k]=='1' && k!=y) {
			i+=1;
		}
	}
	return i/j; 
}
void count_OWP(){
	double x,y; 
	rep(i,0,N-1){
		x=0; y=0; 
		rep(j,0,N-1){
			if (A[i][j]!='.') {
				x+=wp1(j,i); 
				y+=1;
			}
		}
		OWP[i]=x/y; 
	}
}
void count_OOWP(){
	double x,y; 
	rep(i,0,N-1){
		x=0; y=0; 
		rep(j,0,N-1){
			if (A[i][j]!='.') {
				x+=OWP[j]; 
				y+=1;
			}
		}
		OOWP[i]=x/y; 
	}
}
void main(){
	freopen("A-large (2).in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>> T; 
	rep(test_number,1,T){
		cin >> N; 
		A.resize(N); 	
		rep(i,0,N-1) cin >> A[i]; 
		memset(WP,0,sizeof(WP)); 
		memset(OWP,0,sizeof(OWP));
		memset(OOWP,0,sizeof(OOWP)); 
		count_WP(); 
		count_OWP(); 
		count_OOWP();

		cout << "Case #"<<test_number<<":"<<endl; 
		rep(i,0,N-1){
			printf("%.12lf\n",WP[i]*0.25+OWP[i]*0.5+OOWP[i]*0.25); 
		}
	}
}