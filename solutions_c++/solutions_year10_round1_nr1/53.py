
#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int n,K;scanf("%d%d",&n,&K);
		char buf[n][n+2];
		for(int i=0;i<n;i++)scanf("%s",buf[i]);

		char tmp[n][n+2];memset(tmp,'.',sizeof(tmp));
		for(int i=0;i<n;i++){
			int cnt=0;
			for(int k=0;k<n;k++)if(buf[n-1-i][n-1-k]!='.'){
				tmp[n-1-cnt][i]=buf[n-1-i][n-1-k];
				cnt++;
			}
		}
#if 0
		for(int i=0;i<n;i++)tmp[i][n]=0;
		for(int i=0;i<n;i++)puts(tmp[i]);
#endif

		int ok=0;
		for(int i=0;i<2;i++){
			char c="BR"[i];

			for(int k=0;k<n;k++){
				int cnt=0;
				for(int t=0;t<n;t++){
					if(tmp[k][t]==c){
						if(++cnt==K)ok|=(1<<i);
					}else cnt=0;
				}
			}
			for(int k=0;k<n;k++){
				int cnt=0;
				for(int t=0;t<n;t++){
					if(tmp[t][k]==c){
						if(++cnt==K)ok|=(1<<i);
					}else cnt=0;
				}
			}
			for(int k=0;k<=2*(n-1);k++){
				//cout<<"reset"<<endl;
				int cnt=0;
				for(int t=0;t<n;t++)if(0<=-t+k && -t+k<=n-1){
					//cout<<"pos"<<t<<","<<-t+k<<endl;
					if(tmp[t][-t+k]==c){
						if(++cnt==K)ok|=(1<<i);
					}else cnt=0;
				}
			}
			for(int k=0;k<=2*(n-1);k++){
				//cout<<"reset"<<endl;
				int cnt=0;
				for(int t=0;t<n;t++)if(0<=t+k-(n-1) && t+k-(n-1)<=n-1){
					//cout<<"pos"<<t<<","<<t+k-(n-1)<<endl;
					if(tmp[t][t+k-(n-1)]==c){
						if(++cnt==K)ok|=(1<<i);
					}else cnt=0;
				}
			}
		}

		printf("Case #%d: ",npr);
		if(ok==0)puts("Neither");
		if(ok==1)puts("Blue");
		if(ok==2)puts("Red");
		if(ok==3)puts("Both");
	}
	return 0;
}
