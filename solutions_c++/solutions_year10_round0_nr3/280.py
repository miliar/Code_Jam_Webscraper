#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;
#define lint long long

lint R,K;
int n;
lint g[1024];
int nxt[1024];
lint pep[1024];
int main(){
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int cas,it;fin >> cas;
	for(it=1;it<=cas;it++){
		fin >> R >> K >> n;
		int i,j;
		for(i=0;i<n;++i)
			fin >> g[i];
		for(i=0;i<n;++i){
			lint tot=0;
			for(j=i;tot+g[j%n]<=K && j<i+n;tot+=g[j%n],j++);
			nxt[i]=j%n;pep[i]=tot;
		}
		int vis[1024],cur=0;
		for(i=0;i<n;++i)vis[i]=-1;int offSet=0,cycLen=-1;
		for(i=0,cur=0;1;i=nxt[i]){
			if(vis[i]<0){
				vis[i]=cur++;
				
			}
			else{
				cycLen = cur-vis[i];
				offSet = vis[i];
				break;
			}
		}
		lint ans = 0;
		if(R<=offSet){
			for(i=0,j=0;i<R;++i,j=nxt[j])
				ans+=pep[j];
		}
		else{
			R -= offSet;lint ans2=0;
			for(i=0,j=0;i<offSet;++i,j=nxt[j])
				ans += pep[j];
			for(i=0;i<cycLen;++i,j=nxt[j])
				ans2 += pep[j];
			ans2 *= R/cycLen;ans+= ans2;
			for(i=0;i<R%cycLen;++i,j=nxt[j])
				ans+=pep[j];
		}
		fout << "Case #" << it << ": " << ans << endl;
	}
	fin.close();fout.close();
	return 0;
}
