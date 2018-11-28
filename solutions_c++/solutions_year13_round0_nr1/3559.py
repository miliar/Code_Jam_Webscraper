//Author : Ganindu

#include <vector>
//#include <list>
//#include <map>
//#include <set>
//#include <queue>
//#include <stack>

#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<int,int> intpair;

const double pi=acos(-1.0);

//greatest common divisor of a and b
int gcd(int a,int b) {return (b==0)?a:gcd(b,a%b);}

//least common multiple of a and b
int lcm(int a,int b) {return (a*b)/gcd(a,b);}

//get number of '1's in the binary representation of n
int numOfOnes(int n){return (n==0)?0:(1+numOfOnes(n&(n-1)));}

template<class T> string toString(T o){ostringstream ss; ss<<o; return ss.str();}

//get first n primes
vector<int> getPrimes(int n) { 
	vector<int> v; for(int i=2;v.size()<n;i++){ bool prime = true; 
	for(vector<int>::iterator vi=v.begin(); vi!=v.end() ; vi++){ if(i%(*vi)==0){ prime=false; break; }}
	if(prime) v.push_back(i); } return v; }

//get primes upto n
vector<int> getPrimesUpto(int n) { 
	vector<int> v; for(int i=2;i<=n;i++){ bool prime = true; 
	for(vector<int>::iterator vi=v.begin(); vi!=v.end() ; vi++){ if(i%(*vi)==0){ prime=false; break; }}
	if(prime) v.push_back(i); } return v; }

vector<pair<int,int> > factors(int n) { vector<pair<int,int> > v;
	for (int i=2;i*i<=n;i++) { int p=0; for(;n%i==0;p++,n/=i); if (p>0) v.push_back(make_pair(i,p)); }
	if (n>1) v.push_back(make_pair(n,1)); return v; }

bool isPrime(int n) { if(n<=1)return false; for (int i=2;i*i<=n;i++) if (n%i==0) return false; return true;}

template<class T> void multiplyMatrices(int x, int y, int z, T **a, T **b, T **c) { 
	for(int i=0;i<x;i++) for(int j=0;j<z;j++) c[i][j]=0;
	for(int i=0;i<x;i++) for(int j=0;j<y;j++) for(int k=0;k<y;k++) c[i][k] += a[i][j]*b[j][k]; }

//distance between two cartesian points
double dist(double x1,double y1,double x2,double y2){return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));}

/////////////////////////////////// end of header //////////////////////////////////////////////////////////

void performTestcase();

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int ntc; scanf("%d",&ntc);

	for (int tc=1;tc<=ntc;tc++){
		printf("Case #%d: ",tc);
		performTestcase();
	}
}

void performTestcase(){
	char c[4][4]; bool filled = true;
	int xr[4], yr[4], xc[4], yc[4], xd1=0, xd2=0, yd1=0, yd2=0;
	for(int i=0;i<4;i++) xr[i] = yr[i] = xc[i] = yc[i] = 0;
	
	for(int i=0;i<4;i++) scanf("%*[\n]%c%c%c%c",&c[i][0],&c[i][1],&c[i][2],&c[i][3]);
	
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(c[i][j]=='X'){
				xr[i]++; xc[j]++;
			}
			else if(c[i][j]=='O'){
				yr[i]++; yc[j]++;
			}
			else if(c[i][j]=='T'){
				xr[i]++; xc[j]++; yr[i]++; yc[j]++;
			}
			else filled = false;
		}
		
		if(c[i][i]=='X') xd1++;
		else if(c[i][i]=='O') yd1++;
		else if(c[i][i]=='T'){
			xd1++; yd1++;
		}
		
		if(c[i][3-i]=='X') xd2++;
		else if(c[i][3-i]=='O') yd2++;
		else if(c[i][3-i]=='T'){
			xd2++; yd2++;
		}
	}
	
	for(int i=0;i<4;i++){
		if(xr[i]==4||xc[i]==4){
			printf("X won\n");
			return;
		}
		else if(yr[i]==4||yc[i]==4){
			printf("O won\n");
			return;
		}
	}
	
	if(xd1==4||xd2==4) printf("X won\n");
	else if(yd1==4||yd2==4) printf("O won\n");
	else if(filled) printf("Draw\n");
	else printf("Game has not completed\n");
}