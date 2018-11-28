#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstring>
#include <numeric>
#include <utility>
using namespace std;

string test (vector <string> b, int K){
	int dx[]={1, 1, 0, -1, -1, -1, 0, 1};
	int dy[]={0, 1, 1, 1, 0, -1, -1, -1};
	int best[8];
	int blue=0,red=0;
	for (int i=0;i<8;i++) best[i]=0;
	int n = b.size();
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			if (b[i][j]=='.') continue;
			for (int k=0;k<8;k++){
				for (int s=0;s<8;s++) best[s]=0;
				for (int l=1;;l++){
					if (i+l*dx[k]>=n || i+l*dx[k]<0 || j + l*dy[k] >=n || j + l*dy[k]<0) break;
					if (b[i + l*dx[k]][j + l*dy[k]] != b[i][j]) break;
					best[k]=l;
				}
			
			int max = 0;
			for (int s=0;s<4;s++){
				if (best[s]+best[s+4]+1>max) max = best[s]+best[s+4]+1;
			}
			if (max >= K) {
				if (b[i][j]=='B') blue=1; else red=1;
			}}
		}
	}
	if (blue==1&&red==1) return "Both";
	if (blue==1&&red==0) return "Blue";
	if (blue==0&&red==1) return "Red";
	else return "Neither";
}
			
				
	
int main () {
	
	fstream filestr;
	ofstream outstr;
	int cases,res;
	int n,K;
	filestr.open("/Users/HOOI/Downloads/A-large.in");
	outstr.open("/Users/HOOI/Documents/XCode/CodeJam/OUTPUT.txt");
	filestr >> cases;
	string tempstr;
	vector<string> b,c;
	for (int cs=1;cs<=cases;cs++){
		res=0;
		b.clear();
		c.clear();
		filestr >> n >> K; 
		for (int i=0;i<n;i++){ filestr >> tempstr; b.push_back(tempstr); cout << tempstr << endl;}
		for (int i=0;i<n;i++)
			c.push_back(b[i]);
		
		for (int i=0;i<n;i++){
			int droppos=n-1;
			for (int j=n-1;j>=0;j--){
				if (c[i][j]=='.') continue;
				c[i][droppos]=c[i][j];
				if (j!=droppos) c[i][j]='.';
				droppos--;
			}
		}
		for (int i=0;i<n;i++) cout << c[i] << endl;
		outstr << "Case #"<<cs<<": "<<test(c,K)<<endl;
		cout << "Case #"<<cs<<": "<<test(c,K)<<endl;
	}
	filestr.close();
	outstr.close();
	return 0;
}