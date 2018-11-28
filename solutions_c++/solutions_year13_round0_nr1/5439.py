
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <cctype>
#include <complex>
#include <vector>
#include <algorithm>

using namespace std;


int Endflag(int a[][4]){
	
	//èüé“îªíË
	
	int res;
	//â°
	for(int i=0;i<4;i++){
		res = 0;
		for(int j=0;j<4;j++){
			if(a[i][j]==0){
				break;
			}
			if(!res){
				if(a[i][j]==3) continue;
				res = a[i][j];
				continue;
			}
			if(j==3){
				if(a[i][j]==res || a[i][j]==3) return res;
			}else{
				if(a[i][j]!=res && a[i][j]!=3) break;
			}
		}
	}
	//èc
	for(int j=0;j<4;j++){
		res = 0;
		for(int i=0;i<4;i++){
			if(a[i][j]==0){
				break;
			}
			if(!res){
				if(a[i][j]==3) continue;
				res = a[i][j];
				continue;
			}
			if(i==3){
				if(a[i][j]==res || a[i][j]==3) return res;
			}else{
				if(a[i][j]!=res && a[i][j]!=3) break;
			}
		}
	}
	//éŒÇﬂÅ_
	int s;
	s = a[0][0];
	if(s==3) s = a[1][1];
	if((a[1][1]==s||a[1][1]==3)&&(a[2][2]==s||a[2][2]==3)&&(a[3][3]==s||a[3][3]==3)) return s;
	//éŒÇﬂÅ^
	s = a[0][3];
	if(s==3) s = a[1][2];
	if((a[1][2]==s||a[1][2]==3)&&(a[2][1]==s||a[2][1]==3)&&(a[3][0]==s||a[3][0]==3)) return s;
	
	
	//èüé“Ç»Çµ
	//ñ¢èIóπÇ©
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(a[i][j]==0) return 0;
		}
	}
	
	//à¯Ç´ï™ÇØ
	return 3;
}

bool solve(){

	int n;
	cin>> n;
	
	for(int k=0;k<n;k++){
		int a[4][4]={0};
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				char c;
				cin>> c;
				if(c=='.')	a[i][j] = 0;
				if(c=='X')	a[i][j] = 1;
				if(c=='O')	a[i][j] = 2;
				if(c=='T')	a[i][j] = 3;
			}
		}
				
		int eflag = Endflag(a);
		
		if(eflag){
			if(eflag == 1) cout<< "Case #"<< k+1<< ": X won"<<endl;
			if(eflag == 2) cout<< "Case #"<< k+1<< ": O won"<<endl;
			if(eflag == 3) cout<< "Case #"<< k+1<< ": Draw"<<endl;
		}else{
			cout<< "Case #"<< k+1<< ": Game has not completed"<<endl;
		}
	}

	return true;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	solve();

	return 0;
}

 