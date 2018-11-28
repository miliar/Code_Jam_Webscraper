#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

bool join(char b[55][55],int x, int y,char c,int kk,int n){
	int cx=x,cy=y,k=0;
	for (k=0;k<kk;k++){
		if (b[cx][cy]!=c) break;
		if (k==kk-1) return true;
		if (cy+1<n) cy++;
		else break;
	}
	//if (k==kk) {cout << "one";return true;}
	
	cx=x;cy=y;
	for (k=0;k<kk;k++){
		if (b[cx][cy]!=c) break;
		if (k==kk-1) return true;
		if (cx+1<n) cx++;
		else break;
	}
	//if (k==kk) {cout << "two";return true;}
	
	cx=x;cy=y;
	for (k=0;k<kk;k++){
		if (b[cx][cy]!=c) break;
		if (k==kk-1) return true;
		if (cx+1<n && cy+1<n) {cx++;cy++;}
		else break;
	}
	//if (k==kk) {cout << "three";return true;}

	cx=x;cy=y;
	for (k=0;k<kk;k++){
		if (b[cx][cy]!=c) break;
		if (k==kk-1) return true;
		if (cx+1<n && cy-1>=0) {cx++;cy--;}
		else break;
	}
	//if (k==kk) {cout << "four";return true;}

	return false;
}

int main(){

	freopen("a_large.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int cases,n,kk;
	char a[55][55],b[55][55],c;
	
	cin >> cases; 

	for (int casenum=1;casenum<=cases;casenum++){
		cin >> n >> kk;
		//cout << n << " " << k << endl;
		//cout << "qn" << endl;
		for (int i=0;i<n;i++){
			string s;
			cin >> s;
			//cout << s << endl;
			for (int j=0;j<n;j++){
				a[j][n-1-i]=s[j];
				//a[i][j]=s[j];
			}
		}
		
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				b[i][j]='.';

		for (int j=0;j<n;j++){
			string s = "";
			for (int i=0;i<n;i++){
				if (a[i][j]!='.'){
					s = s + a[i][j];
				}
			}
			if (s.size()>0){
				int k=0;
				for (int i=s.size()-1;i>=0;i--){
					b[n-1-k][j] = s[i];
					k++;
				}
			}
		}
		cout << "Case #" << casenum;
		bool red=false;
		bool blue=false;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if (join(b,i,j,'R',kk,n)) red=true;
				/*if (red){
					cout << "stop at ";
					cout << i << j << endl;	
				}*/
				if (join(b,i,j,'B',kk,n)) blue=true;
			}
		}

		//cout << "Case " << casenum << endl;
		if (red && blue) cout << ": Both" << endl;
		else if (red && !blue) cout << ": Red" << endl;
		else if (!red && blue) cout << ": Blue" << endl;
		else cout << ": Neither" << endl;
		/*
		cout << n << "  " << kk << endl;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				cout << b[i][j]; 
			}
			cout << endl;
		}
		*/
	}

	return 0;
}