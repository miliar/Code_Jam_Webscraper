#include<stdio.h>
char a[1010][1010];
double w[1010],ow[1010],oow[1010];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("AL.txt","w",stdout);
	int T,t,n,i,j,k;
	double x,y,c,d;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",a[i]);
			x=0;y=0;
			for(j=0;j<n;j++){
				if(a[i][j]=='1'){x++;y++;}
				if(a[i][j]=='0'){y++;}
			}
			w[i]=x/y;
		}
		for(i=0;i<n;i++){
			x=0;y=0;
			for(j=0;a[i][j]!=0;j++){
				if(a[i][j]=='1'||a[i][j]=='0'){
					for(k=0,c=0,d=0;a[j][k]!=0;k++){
						if(k==i)continue;
						if(a[j][k]=='1'){c++;d++;}
						if(a[j][k]=='0'){d++;}	
					}
					x+=c/d;y++;
				}
			}
			ow[i]=x/y;
		}
		for(i=0;i<n;i++){
			x=0;y=0;
			for(j=0;a[i][j]!=0;j++){
				if(a[i][j]=='1'||a[i][j]=='0'){
					x+=ow[j];
					y++;
				}
			}
			oow[i]=x/y;
		}
		printf("Case #%d:\n",t);
		for(i=0;i<n;i++){
			//printf("%lf %lf %lf\n",w[i],ow[i],oow[i]);
			printf("%.10lf\n",0.25*w[i]+0.5*ow[i]+0.25*oow[i]);
		}
	}
}
