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

int k;
string s;

int calc(const string &a){
	int res=1,tam=a.size(),i;
	
	for (i=0;i+1<tam;i++) if (a[i]!=a[i+1]) res++;
	return res;
}

int main(){
	int casos,c,i,j;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<":";
		cin>>k>>s;
		
		vector<int> p(k,0);
		for (i=0;i<k;i++) p[i]=i;
		int rta=100000,tam=((int)s.size()/k);
		do{
			string tmp(s);
			for (j=0;j<tam;j++){
				for (i=0;i<k;i++) tmp[j*k+i]=s[j*k+p[i]];
			}
			rta<?=calc(tmp);
		}while (next_permutation(all(p)));
		cout<<" "<<rta<<endl;
	}
	
	return 0;
}
