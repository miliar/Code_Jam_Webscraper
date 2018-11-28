#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
using namespace std;
typedef struct{
	string fold;
	vector<int> subf;
}tp;
int t,m,n;
char c,str[105];
vector<int> kos;
vector<tp> vc;
int main(){
	scanf("%d",&t);
	for(int k=1;k<=t;++k){
		int pros=0;
		//printf(" 1\n");
		vc.resize(0);
		vc.push_back((tp){"",kos});
		scanf("%d%d",&m,&n);
		//printf(" 2 =%d\n",m);
		for(int j=0;j<m;++j){
			int pos=0,id=0;
			//printf("=");
			while(1){
				//printf("=");
				c=getchar();
				if(c=='/' || c=='\n') { if(id>0) {
					str[id]='\0';
					//printf(" %s\n",str);
					int l=vc[pos].subf.size(),i;
					for(i=0;i<l;++i) if(strcmp(str,vc[vc[pos].subf[i]].fold.c_str())==0) break;
					if(i==l){
						vc[pos].subf.push_back(vc.size());
						vc.push_back((tp){str,kos});
						pos=vc.size()-1;
						//printf(" tambah %s\n",str);
					}
					else{
						pos=vc[pos].subf[i];
						//printf(" sudah ada %s\n",str);
					}
					id=0;
					if(c=='\n') break;
				}}
				else {
					str[id]=c;
					++id;
					
				}
			}
		}
		//printf("====\n");
		for(int j=0;j<n;++j){
			int pos=0,id=0;
			//printf("=");
			while(1){
				//printf("=");
				c=getchar();
				if(c=='/' || c=='\n') { if(id>0) {
					str[id]='\0';
					//printf(" %s\n",str);
					int l=vc[pos].subf.size(),i;
					for(i=0;i<l;++i) if(strcmp(str,vc[vc[pos].subf[i]].fold.c_str())==0) break;
					if(i==l){
						vc[pos].subf.push_back(vc.size());
						vc.push_back((tp){str,kos});
						pos=vc.size()-1;
						//printf(" tambah %s\n",str);
						++pros;
					}
					else{
						pos=vc[pos].subf[i];
						//printf(" sudah ada %s\n",str);
					}
					id=0;
					if(c=='\n') break;
				}}
				else {
					str[id]=c;
					++id;
					
				}
			}
		}
		printf("Case #%d: %d\n",k,pros);
	}
	return 0;
}
