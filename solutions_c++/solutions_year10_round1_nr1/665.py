#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair

int F,K;

string A[51],B[51];


bool check(char c){
	//horizontal
	for (int i=0; i<F ; i++) {
		for (int j=0; j+K<=F ; j++) {
			bool ok=true;
			for (int k=0; k<K; k++) {
				if(A[i][j+k]!=c){ ok=false; break;}
			}
			if(ok) return true;
		}
	}
	
	//vertical
	for (int j=0; j<F ; j++) {
		for (int i=0; i+K<=F ; i++) {
			bool ok=true;
			for (int k=0; k<K; k++) {
				if(A[i+k][j]!=c){ ok=false; break;}
			}
			if(ok){ return true;}
		}
	}
	
	//diagonal der dec
	for (int i=0; i+K<=F ; i++) {
		for (int j=0; j+K<=F; j++) {
			bool ok=true;
			for (int k=0; k<K ; k++) {
				if(A[i+k][j+k] != c){ok=false; break;}
			}
			if(ok) return true;
		}
	}
	
	
	//diagonal der cre
	for (int i=F-1; i+1>=K ; i--) {
		for (int j=0; j+K<=F; j++) {
			bool ok=true;
			for (int k=0; k<K ; k++) {
				if(A[i-k][j+k] != c){ok=false; break;}
			}
			if(ok) return true;
		}
	}
	
	return false;
}

void printInfo(){
	for (int i=F-1; i>=0; i--) {
		cout<<A[i]<<endl;
	}
}

int main(){
	int kases; cin>>kases; kases++;
	for (int k=1; k<kases; k++) {
		cin>>F>>K;
		for (int i=0; i<F ; i++) {
			string s=""; char a;
			for (int j=0; j<F ; j++) {
				cin>>a; s.PB(a);
			}
			A[i] = s;
		}
		for (int j=0; j<F ; j++) {
			string b = "";
			for (int i=F-1; i>=0 ; i--) {
				b.PB(A[i][j]);
			}
			B[j] = b;
		}
		for (int j=0; j<F ; j++) {
			string a="";
			for (int i=F-1; i>=0; i--) {
				if(B[i][j]!='.') a.PB(B[i][j]);
			}
			while(a.size() < size_t(F) ) a.PB('.');
			for (int i=F-1; i>=0; i--) {
				A[i][j] = a[i];
			}
		}
		
		//printInfo();
		
		bool winR = check('R');
		bool winB = check('B');
		cout<<"Case #"<<k<<": ";
		if(winR && winB) cout<<"Both"<<endl;
		else if(winR) cout<<"Red"<<endl;
		else if(winB) cout<<"Blue"<<endl;
		else cout<<"Neither"<<endl;
		
	}
}