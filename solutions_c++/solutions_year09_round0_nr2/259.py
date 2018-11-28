#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

int tabla[105][105];
int valor[105][105];
int pri,sec,cant;
int di[]={-1,0,0,1};
int dj[]={0,-1,1,0};

inline bool in(int a, int b){
	return 0<=a && a<pri && 0<=b && b<sec;
}

int calc(int i, int j){
	if (valor[i][j]!=-1) return valor[i][j];
	int k,mej=200000,mpos=-1;
	
	for (k=0;k<4;k++){
		int ni=i+di[k],nj=j+dj[k];
		
		if (in(ni,nj)){
			if (tabla[ni][nj]<mej){
				mej=tabla[ni][nj];
				mpos=k;
			}
		}
	}
	if (mej<tabla[i][j]){
		return valor[i][j]=calc(i+di[mpos],j+dj[mpos]);
	}
	return valor[i][j]=cant++;
}

int main(){
	int casos,c;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<":"<<endl;
		cin>>pri>>sec;
		
		int i,j;
		
		for (i=0;i<pri;i++) for (j=0;j<sec;j++) cin>>tabla[i][j];
		
		memset(valor,-1,sizeof(valor));
		
		cant=0;
		for (i=0;i<pri;i++) for (j=0;j<sec;j++) if (valor[i][j]==-1){
			valor[i][j]=calc(i,j);
		}
		
		for (i=0;i<pri;i++){
			cout<<(char)(valor[i][0]+'a');
			for (j=1;j<sec;j++) cout<<" "<<(char)(valor[i][j]+'a');
			cout<<endl;
		}
	}
	
	return 0;
}
