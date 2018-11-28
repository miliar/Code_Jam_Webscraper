#include <iostream>
#include <math.h>
#include <string>
#include <set>
using namespace std;
#define MAX(a, b) (((a)<(b))?(b):(a))
char A[101][101];
int n;
double W[101];
double OW[101];
double OOW[101];
void solve(int c){
	for(int i=0;i<n;++i){
		W[i]=0;
		int cnt=0;
		for(int j=0;j<n;++j){
			if(A[i][j]=='1'){
				W[i]++;
				++cnt;
			}else if(A[i][j]=='0'){
				++cnt;
			}
		}
		if(cnt!=0){
			W[i]/=double(cnt);
		}
	}
	////
	for(int i=0;i<n;++i){
		OW[i]=0;
		int cnt=0;
		for(int j=0;j<n;++j)if((i!=j) && (A[i][j]!='.')){
			double wp=0;
			int cnt2=0;
			for(int k=0;k<n;++k)if((k!=j) && (k!=i) && (A[j][k]!='.')){
				++cnt2;
				if(A[j][k]=='1'){
					wp+=1;
				}
			}
			if(cnt2!=0){
				wp/=double(cnt2);
			}
			OW[i]+=wp;
			++cnt;
		}
		if(cnt!=0){
			OW[i]/=double(cnt);
		}
	}
	///
	for(int i=0;i<n;++i){
		OOW[i]=0;
		int cnt=0;
		for(int j=0;j<n;++j)if((i!=j) && (A[i][j]!='.')){
			OOW[i]+=OW[j];
			++cnt;
		}
		if(cnt!=0){
			OOW[i]/=double(cnt);
		}
	}
	/////
	cout<<"Case #"<<c<<": "<<endl;
	for(int i=0;i<n;++i){
		cout.precision(12);
		cout<<0.25*W[i]+0.5*OW[i]+0.25*OOW[i]<<endl;
	}
}


int main(int argc, char *argv){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		cin>>n;
		string nextString;
		for(int i=0;i<n;++i){
			cin>>nextString;
			for(int j=0;j<n;++j){
				A[i][j]=nextString[j];
			}
		}
		solve(c+1);
	}
	return 0;
}
