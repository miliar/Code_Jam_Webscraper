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

#define MAX 10010
#define INF 1000000

int val[MAX],gate[MAX],ch[MAX];
int m,v,inte;
int mini[MAX][2];

int calc(int pos, int valor){
	if (mini[pos][valor]!=-1) return mini[pos][valor];
	if (pos>inte) return mini[pos][valor]=((valor==val[pos])?0:INF);
	if (val[pos]==valor) return mini[pos][valor]=0;
	int rta=INF;
	if (ch[pos]){
		if (!gate[pos]){
			if (valor) rta<?=1+calc(2*pos,1)+calc(2*pos+1,1);
			else rta<?=1+min(calc(2*pos,0),calc(2*pos+1,0));
		}else{
			if (valor) rta<?=1+min(calc(2*pos,1),calc(2*pos+1,1));
			else rta<?=1+calc(2*pos,0)+calc(2*pos+1,0);
		}
	}
	if (gate[pos]){
		if (valor) rta<?=calc(2*pos,1)+calc(2*pos+1,1);
		else rta<?=min(calc(2*pos,0),calc(2*pos+1,0));
	}else{
		if (valor) rta<?=min(calc(2*pos,1),calc(2*pos+1,1));
		else rta<?=calc(2*pos,0)+calc(2*pos+1,0);
	}
	return mini[pos][valor]=rta;
}

int main(){
	int casos,i,c;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<":";
		
		cin>>m>>v;
		inte=(m-1)/2;
		for (i=1;i<=m;i++){
			if (i<=inte){
				cin>>gate[i]>>ch[i];
			}
			else cin>>val[i];
		}
		for (i=inte;i>=1;i--){
			if (gate[i]) val[i]=val[2*i]&&val[2*i+1];
			else val[i]=val[2*i]||val[2*i+1];
		}
		memset(mini,-1,sizeof(mini));
		int res=calc(1,v);
		
		if (res<INF) cout<<" "<<res<<endl;
		else cout<<" IMPOSSIBLE"<<endl;
	}
	
	return 0;
}
