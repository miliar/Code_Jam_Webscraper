#include<stdio.h>


int main(){
int i,j,k,l,n,r,c,error,t;
char a[1000][1000];
FILE *pt=fopen("out.txt","w");
scanf("%d",&t);
			for(i=0;i<t;i++){
			scanf("%d %d",&r,&c);
			for(j=0;j<r;j++)
			scanf("%s",a[j]);
			error=0;
			for(j=0;j<r;j++){
						for(k=0;k<c;k++)
									{
									if(a[j][k]=='#')
										{
										a[j][k]='/';
										if(a[j+1][k]!='#')
										{error=1;break;}
										else
										a[j+1][k]='\\';
										
										if(a[j+1][k+1]!='#')
										{error=1;break;}
										else
										a[j+1][k+1]='/';
										
										if(a[j][k+1]!='#')
										{error=1;break;}
										else
										a[j][k+1]='\\';
										
										}
									}
									if(error==1)
									break;
			}
			if(error==1)
			fprintf(pt,"Case #%d:\nImpossible\n",i+1);
			else{
			fprintf(pt,"Case #%d:\n",i+1);
			for(j=0;j<r;j++)
			fprintf(pt,"%s\n",a[j]);
			}
			}

}
