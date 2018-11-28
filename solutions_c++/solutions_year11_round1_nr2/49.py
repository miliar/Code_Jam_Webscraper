#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

int t,n,m;
char li[20000][20];
int len[20000];
char w[200][40];
int vl[20000];
int two[31];
int s[20000];
int ans[20000];
bool cutt[20000];

bool cmp(const int&a,const int&b){
	return vl[a]<vl[b];
}
bool cmp1(const int&a,const int&b){
	return len[a]<len[b];
}

int main(){
	int h,i,j,k,l,o,la;
	bool us;
	two[0]=1;
	for(i=1;i<31;i++)
		two[i]=two[i-1]*2;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d",&n,&m);
		memset(len,0,sizeof(len));
		for(i=0;i<n;i++){
			scanf("%s",li[i]);
			len[i]=strlen(li[i]);
		}
		for(j=0;j<m;j++)
			scanf("%s",w[j]);
		printf("Case #%d:",h);
		for(j=0;j<m;j++){
			memset(ans,0,sizeof(ans));
			memset(cutt,0,sizeof(cutt));
			for(i=0;i<n;i++)
				s[i]=i;
			sort(&s[0],&s[n],cmp1);
			for(i=1;i<n;i++){
				if(len[s[i]]!=len[s[i-1]])
					cutt[i-1]=1;
			}
			cutt[n-1]=1;
			for(k=0;k<26;k++){
				us=0;
				la=0;
				/*printf("\n");
				for(i=0;i<n;i++)
					printf(" %3d",vl[i]);
				for(i=0;i<n;i++)
					printf(" %3d",s[i]);
				for(i=0;i<n;i++)
					printf(" %3d",cutt[i]);
				for(i=0;i<n;i++)
					printf(" %3d",ans[i]);
				printf("\n");*/
				for(i=0;i<n;i++){
					vl[s[i]]=0;
					for(o=0;o<strlen(li[s[i]]);o++){
						if(li[s[i]][o]==w[j][k]){
							vl[s[i]]+=two[o];
							us=1;
						}
					}
					if(cutt[i]==1){
						sort(&s[la],&s[i+1],cmp);
						if(us){
							for(o=la;o<=i;o++){
								if(vl[s[o]]==0)
									ans[s[o]]++;
							}
							for(o=la+1;o<=i;o++){
								if(vl[s[o]]!=vl[s[o-1]])
									cutt[o-1]=1;
							}
						}
						us=0;
						la=i+1;
					}	
				}
			}
			/*for(i=0;i<n;i++)
				printf(" %d",ans[i]);
			printf("\n");*/
			k=0;
			for(i=1;i<n;i++){
				if(ans[i]>ans[k])k=i;
			}
			printf(" %s",li[k]);
		}
		printf("\n");
	}
	return 0;
}
