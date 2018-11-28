#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 110
double wp[maxn][maxn],owp[maxn],oowp[maxn];
int t,n;
char mat[maxn][maxn];
int cnt[maxn],hav[maxn];
void get_wp()
{
	int i,j,k;
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			if(mat[i][j]=='0'){
				cnt[i]++;
			}else if(mat[i][j]=='1'){
				cnt[i]++;
				hav[i]++;
			}
		}
		for(j=1;j<=n;j++){
			if(mat[i][j]=='0'){
				if(cnt[i]!=1)
					wp[i][j]=hav[i]*1.0/(cnt[i]-1);
			}else if(mat[i][j]=='1'){
				if(cnt[i]!=1)
					wp[i][j]=(hav[i]-1)*1.0/(cnt[i]-1);
			}
		}
		//printf("%d %lf\n",i,hav[i]*1.0/cnt[i]);
	}
}
void get_owp()
{
	int i,j,k;
	double tmp;
	for(i=1;i<=n;i++){
		k=0;
		tmp=0;
		for(j=1;j<=n;j++){
			if(mat[i][j]!='.'){
				k++;
				tmp+=wp[j][i];
			}
		}
		if(k!=0)
			owp[i]=tmp/k;
		//printf("%d %d %lf %lf\n",i,k,tmp,owp[i]);
	}
}
void get_oowp()
{
	int i,j,k;
	double tmp;
	for(i=1;i<=n;i++){
		k=0;
		tmp=0;
		for(j=1;j<=n;j++){
			if(mat[i][j]!='.'){
				k++;
				tmp+=owp[j];
			}
		}
		if(k!=0)
			oowp[i]=tmp/k;
	}
}
double get_score(int id)
{
	double res=0;
	if(cnt[id]!=0)res+=0.25*(hav[id]*1.0/cnt[id]);
	return res+0.5*owp[id]+0.25*oowp[id];
}
int main()
{
	int i,j,k,cas;
    freopen("A-large.in","r",stdin);    freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf("%s",mat[i]+1);
			//printf("%s\n",mat[i]+1);
		}
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				wp[i][j]=0;
			}
			owp[i]=oowp[i]=0;
			cnt[i]=hav[i]=0;
		}
		get_wp();
		get_owp();
		get_oowp();
		printf("Case #%d:\n",cas);
		for(i=1;i<=n;i++){
			printf("%.8lf\n",get_score(i));
		}
		
	}
	return 0;
}

