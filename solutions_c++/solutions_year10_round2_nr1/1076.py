#include<map>
#include<cstdio>
#include<iostream>
using namespace std;

char made[101][101];
char make[101][101];
int main(){
	int tc; scanf("%d",&tc);
	for(int t=1;t<=tc;t++){
		map<string,int> M;
		int m,n; scanf("%d%d",&m,&n);
		for(int i=0;i<m;i++) scanf("%s",made[i]);
		for(int i=0;i<n;i++) scanf("%s",make[i]);
		
		for(int i=0;i<m;i++){
			string str=made[i];
			int loc=str.find("/",0);
			while(loc!=-1){
				loc=str.find("/",loc+1);
				M[str.substr(0,loc)]=1;
			}
		}
		
		int ans=0;
		for(int i=0;i<n;i++){
			string str=make[i];
			int loc=str.find("/",0);
			while(loc!=-1){
				loc=str.find("/",loc+1);
				string temp=str.substr(0,loc);
				if(M.count(temp)==0){
					ans++; M[temp]=1;
				}
			}
		}
		
		printf("Case #%d: %d\n",t,ans);
	}
}
