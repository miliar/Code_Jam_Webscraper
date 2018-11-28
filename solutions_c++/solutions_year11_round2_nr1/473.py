#include<stdio.h>
//#include<algorithm>
//using namespace std;

struct node{
	double wp,owp,oowp,num,ownnum,rip;
}res[110];

char str[110][110];

//int cmp(node a,node b){
//	if(a.rip>b.rip) return -1;


int main(){
	freopen("Ain2.txt","r",stdin);
	freopen("Aout.txt","w",stdout);
	int N,Case=1,T;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&N);
		for(int i=0;i<N;++i){
			scanf("%s",str[i]);
		}
		for(int i=0;i<N;++i){
			double n=0.0,m=0.0;
			for(int j=0;j<N;++j){
				if(str[i][j]=='1'||str[i][j]=='0'){
					n+=1.0;
					if(str[i][j]=='1'){
						m+=1.0;
					}
				}
			}
			res[i].num=n;
			res[i].ownnum=m;
			res[i].wp=m/n;
		}
		for(int i=0;i<N;++i){
			double nwp=0.0;
			for(int j=0;j<N;++j){
				if(str[i][j]=='1'||str[i][j]=='0'){
					if(str[i][j]=='0'){
						nwp+=(res[j].ownnum-1.0)/(res[j].num-1.0);
					}
					else
					{
						nwp+=(res[j].ownnum)/(res[j].num-1.0);
					}
				}
			}
			res[i].owp=nwp/res[i].num;
		}
		for(int i=0;i<N;++i){
			double nowp=0.0;
			for(int j=0;j<N;++j){
				if(str[i][j]=='1'||str[i][j]=='0'){
					nowp+=res[j].owp;
				}
			}
			res[i].oowp=nowp/res[i].num;
		}
		for(int i=0;i<N;i++){
			res[i].rip=0.25*res[i].wp+0.5*res[i].owp+0.25*res[i].oowp;
		}
		//sort();
		printf("Case #%d:\n",Case++);
		for(int i=0;i<N;i++){
			printf("%.12lf\n",res[i].rip);
		}
	}


	return 0;
}