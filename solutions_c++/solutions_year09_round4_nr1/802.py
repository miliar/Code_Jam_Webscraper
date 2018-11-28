// codejam.cpp : Defines the entry point for the console application.
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <hash_set>



using namespace std;

typedef long long int64;
#define For(i,n) for (i=0;i<n;i++) 

int i,j,k,n,m,tests,t,kol;

string s;


string itos(int64 a) {stringstream s; s<<a; return s.str();}
int64 stoi(string a) {stringstream s; s<<a; int64 b; s>>b; return b;}
string dtos (double a){char buf[100]; sprintf(buf,"%.3",a); return string(buf);}
double stod(string a) {stringstream s; s<<a; double b; s>>b; return b;}


int gcd(int a, int b){
	while(true){
		if (a==0) return b;
		if (b==0) return a;
		if (a>b)
			a = a - b*(a/b);
		else
			b = b - a*(b/a);
	}
}

int M[40][40];

bool zero(int i, int k){
	for (int j=k+1; j<n; j++)
		if (M[i][j]==1) return false;
	return true;
}

bool one(int i, int k){
	for (int j=0; j<=k; j++)
		if (M[i][j]==1) return true;
	return false;
}


void swap(int i, int k){
	int j,jj;
	for (jj=k-1;jj>=i;jj--){
		For(j,n){
			int tmp = M[jj][j];
			M[jj][j] = M[jj+1][j];
			M[jj+1][j]=tmp;
		}
	}
}

int main()
{

	ifstream inp("A-large.in");
	ofstream out("A-large.out");

	inp>>tests;
	For(t,tests){
		out<<"Case #"<<t+1<<": ";
		
		int k = 0,ii,jj;
		int res = 0;

		inp>>n;
		char c;
		For(i,n)
			For(j,n){
				inp>>c;
				if (c=='0')
					M[i][j]=0;
				else
					M[i][j]=1;
		}


		vector <int> X;
		For(i,n){
			for (j=n-1; j>=0; j--)
				if (M[i][j]==1) {
					X.push_back(j+1);
					break;
				}
			if (X.size()!=(i+1)) X.push_back(0);
		}


		while (true){
			bool fl = false;
			bool fl2 = false;
			For(i,n){
				if (X[i]>i+1){
					fl2= true;
					for (j=i+1; j<n; j++)
						if (X[j]<=i+1){
							for (k=j;k>i; k--){
								int tmp = X[k];
								X[k]=X[k-1];
								X[k-1]=tmp;
								res++;
							}
							fl=true;
							break;
						}
				}
				if (fl) break;
			}
			if (!fl2) break;
		}

			out<<res<<endl;
	}


return 0;
}

