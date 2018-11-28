#include<cstdio>
const int N=110;
char a[N][N];
double wp[N],owp[N],oowp[N],s;
int x[N],y[N],m,n;
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int i,j,t,tt=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				scanf(" %c",&a[i][j]);
		for(i=0;i<n;i++){
			x[i]=y[i]=0;
			for(j=0;j<n;j++){
				if(a[i][j]=='1')x[i]++;
				if(a[i][j]!='.')y[i]++;
			}
			wp[i]=(double)x[i]/y[i];
		}
		for(j=0;j<n;j++){
			s=0;m=0;
			for(i=0;i<n;i++){
				if(a[i][j]!='.'){
					m++;
					if(a[i][j]=='1')s+=(double)(x[i]-1)/(y[i]-1);
					else s+=(double)x[i]/(y[i]-1);
				}
			}
			owp[j]=s/m;
		}
		for(i=0;i<n;i++){
			s=0;m=0;
			for(j=0;j<n;j++){
				if(a[i][j]!='.'){
					m++;
					s+=owp[j];
				}
			}
			oowp[i]=s/m;
		}
		printf("Case #%d:\n",tt++);
		for(i=0;i<n;i++)
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}