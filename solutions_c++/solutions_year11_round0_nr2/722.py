#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int t,c,d,n;
char cs[220][220];
bool ds[220][220];
char ns[220];
char ans[220];
char ans1[220];
int ls[220];

int main(){
	scanf("%d",&t);
	int h,i,j,k,l;
	bool de;
	char tmp[10],w;
	for(h=1;h<=t;h++){
		memset(cs,0,sizeof(cs));
		memset(ds,0,sizeof(ds));
		memset(ans,0,sizeof(ans));
		scanf("%d",&c);
		for(i=0;i<c;i++){
			scanf("%s",tmp);
			cs[tmp[0]][tmp[1]]=tmp[2];
			cs[tmp[1]][tmp[0]]=tmp[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++){
			scanf("%s",tmp);
			ds[tmp[0]][tmp[1]]=1;
			ds[tmp[1]][tmp[0]]=1;
		}
		scanf("%d",&n);
		scanf("%s",ns);
		j=-1;
		for(i=0;i<n;i++){
			w=ns[i];
			while(j!=-1 && cs[w][ans[j]]!=0)w=cs[w][ans[j]],j=ls[j];
			if(j!=-1){
				if(ds[w][ans[j]])j=-1;
				else{
					de=0;
					for(k=j;ls[k]!=-1;k=ls[k]){
						if(ds[w][ans[ls[k]]]){
							j=-1;
							de=1;
							break;
						}
					}
					if(!de){
						ans[j+1]=w;
						ls[j+1]=j;
						j++;
					}
				}
			}else{
				ans[j+1]=w;
				ls[j+1]=j;
				j++;
			}
		}
		l=0;
		for(k=j;k!=-1;k=ls[k]){
			ans1[l++]=ans[k];
		}
		ans1[l]=0;
		printf("Case #%d: [",h);
		for(k=l-1;k>=0;k--){
			putchar(ans1[k]);
			if(k!=0)printf(", ");
		}
		putchar(']');
		putchar('\n');
	}
	return 0;
}
