#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

//istream& fin = cin;
//ifstream fin ("A-sample.txt");
ifstream fin ("A-small-attempt2.in");
ofstream fout ("A-small-attempt2.out");
//ifstream fin ("A-large.in");
//ofstream fout ("A-large.out");
//ostream& fout = cout;

int dat[10000][2];
int n,d;
bool rs;

void DFS(int pos,int pt,int len){
	if((pt+len)>=d){
		rs=true;
		return;
	}
	int maxL=-1;
	int maxP=-1;
	for(int i=pos+1;i<n;i++){
		if(dat[i][0]<=pt+len){
			int nextL = min(dat[i][0]-pt,dat[i][1]);
			DFS(i,dat[i][0],nextL);
		}else{
			break;
		}
	}
}

int main(){
	int t;
	
	fin >> t;
	for(int i=1; i<=t; i++){
    fout << "Case #" << i << ": ";
    rs = false;
    fin>>n;
    for(int j=0;j<n;j++){
			fin >> dat[j][0] >> dat[j][1];
		}
		fin >> d;
    
		int pt=dat[0][0];
		int len=dat[0][1];
		if(pt<=len){
//cout << pt << ' ' << pt << endl;
			DFS(0,pt,pt);
		}
    
    if(rs){
			fout << "YES" << endl;
		}else{
			fout << "NO" << endl;
		}
	}
	system("pause");
}
