#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	int sq[100][100];
	int k;
	cin>>k;
	for(int i=0; i<k; i++)
	for(int j=0; j<=i; j++)
		cin>>sq[i-j][j];
	for(int i=k-2; i>=0; i--)
	for(int j=0; j<=i; j++)
		cin>>sq[k-1-j][k-1-(i-j)];
//	for(int i=0; i<k; i++){
//	for(int j=0; j<k; j++)
//		cout<<sq[i][j];
//	cout<<endl;
//	}
	int res=4*k;
	for(int x=-2*k; x<4*k-1; x++)
	for(int y=-2*k; y<4*k-1; y++){
		if((x+y)&1)
			continue;
		int good=1;
		for(int i=0; i<k && good; i++)
		for(int j=0; j<k; j++){
			int ip=x-i, jp=y-j;
		//	if(x==0 && y==0){
		//		debug(i);
		//		debug(j);
		//		debug(ip);
		//		debug(jp);
		//	}
			if(0<=ip && ip<k && 0<=jp && jp<k && sq[i][j]!=sq[ip][jp]){
				good=0;
				break;
			}
		}
		for(int i=0; i<k && good; i++)
		for(int j=0; j<k; j++){
			int ip=(x-y)/2+j, jp=(y-x)/2+i;
		//	if(x==0 && y==0){
		//		debug(i);
		//		debug(j);
		//		debug(ip);
		//		debug(jp);
		//	}
			if(0<=ip && ip<k && 0<=jp && jp<k && sq[i][j]!=sq[ip][jp]){
				good=0;
				break;
			}
		}
		for(int i=0; i<k && good; i++)
		for(int j=0; j<k; j++){
			int ip=x-((x-y)/2+j), jp=y-((y-x)/2+i);
		//	if(x==0 && y==0){
		//		debug(i);
		//		debug(j);
		//		debug(ip);
		//		debug(jp);
		//	}
			if(0<=ip && ip<k && 0<=jp && jp<k && sq[i][j]!=sq[ip][jp]){
				good=0;
				break;
			}
		}
		if(good){
			int cost=max(abs(x-(k-1)), abs(y-(k-1)));
			if(res>cost)
				res=cost;
		}
	}
	res=(res+k)*(res+k)-k*k;
	cout<<res<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
