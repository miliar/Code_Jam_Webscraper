
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "algorithm"
#include "vector"
#include "string"
using namespace std;
typedef long long int i64;

long long int T,R,K,G;
int q[10000001];
pair<int,int> mark[10000001];
bool mark2[10000001];
i64  simul(){
	i64 gan=0;
	vector<int> cant;
	memset(mark2,false,sizeof(mark2));
	int pos=0,pmark=0;
	for(int i=0;i<R;++i){
		if(mark2[pos]){
			pmark=mark[pos].first;
			pos=mark[pos].second;
			gan+=cant[pmark];
		}else{
			mark2[pos]=true;
			pair<int,int> &pp=mark[pos];
			pp.first=cant.size();
			int cap=0;
			int cont=0;
			while(true){
				int &v=q[pos];
				if(K>=cap+v){
					cont++;
					if(cont>G) break;
					pos=(pos+1)%G;
					cap+=v;
					gan+=v;
				}else break;
			}
			pp.second=pos;
			cant.push_back(cap);
		}
	}
	return gan;
}
int main(){
	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	//FILE *f=fopen("C-small-attempt0.out","w");
	scanf("%d",&T);
	int tmp;
	for(int ca=1;ca<=T;++ca){
		scanf("%d %d %d",&R,&K,&G);
		for(int i=0;i<G;++i) {
			scanf("%d",&q[i]);
		}
		i64 sol=simul();
		printf("Case #%d: %lld\n",ca,sol);
		//fprintf(f,"Case #%d: %lld\n",ca,sol);
	}
	//fclose(f);
	return 0;
}