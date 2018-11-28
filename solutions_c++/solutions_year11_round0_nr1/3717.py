#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstring>
#include<set>
#include<map>

using namespace std;

int in(){int a; scanf("%d",&a); return a;}

int main(){
	int t = in();
	int n;
	int p;
	char r;
	for(int i=1;i<=t;++i){
		n = in();
		int ot=0,bt=0;
		int oi=1,bi=1;
		for(int j=0;j<n;++j){
			scanf(" %c",&r);
			p=in();
			if(r=='O'){
				ot = max(bt+1,ot+abs(p-oi)+1);
				oi=p;
			}else{
				bt = max(ot+1,bt+abs(p-bi)+1);
				bi=p;
			}
		}
		cout << "Case #" << i << ": " << max(ot,bt) << endl;
	}
	return 0;
}
