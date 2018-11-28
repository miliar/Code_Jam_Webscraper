#include <vector>
#include <string>
#include <sstream>
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
#define bits(x) __builtin_popcount(x)


int main(){
	int casos,c;
	string nro;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<": ";
		
		cin>>nro;
		nro="0"+nro;
		
		int tam=nro.size();
		int i,j,mej=10000,mejpos;
		
		for (i=tam-2;i>=0;i--) if (nro[i]<nro[i+1]) break;
		for (j=i+1;j<tam;j++) if (nro[j]>nro[i]){
			if (mej>nro[j]){
				mej=nro[j];
				mejpos=j;
			}
		}
		swap(nro[i],nro[mejpos]);
		string tmp=nro.substr(i+1);
		sort(all(tmp));
		nro=nro.substr(0,i+1);
		while (nro.size()>0 && nro[0]=='0') nro=nro.substr(1);
		cout<<nro<<tmp<<endl;
	}
	
	return 0;
}
