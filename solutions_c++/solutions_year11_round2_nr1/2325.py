#include<stdio.h>
int main(){
	int t,i;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		int n,j,k,c[101];
		char m[101][101];
		double wp[101],owp[101],oowp[101],aowp[101][101];
		scanf("%d ",&n);
		for(j=0;j<n;j++){
			wp[j]=0;c[j]=0;char ch;
			//scanf("%c",&ch);
		 for(k=0;k<n;k++)
				aowp[j][k]=0;
			for(k=0;k<n;k++){
				scanf("%c",&m[j][k]);
    			//	printf("%c\n",m[j][k]);
				if(m[j][k]=='1'){
					wp[j]++;c[j]++;//printf("s=%f c=%d\n",wp[j],c[j]);
					for(int l=0;l<n;l++){
						if(l!=k)
							aowp[j][l]++;
					}
				}
				else if(m[j][k]=='0')
					c[j]++;
			}//printf("s=%f c=%d\n",wp[j],c[j]);
			wp[j]=wp[j]/(double)c[j];
		//	printf("wp[%d]= %lf\n",j,wp[j]);
			for(k=0;k<n;k++){
                             
				//printf("aowp[%d][%d]= %f  c=%d\n",j,k,aowp[j][k],c[j]);
				aowp[j][k]=aowp[j][k]/(double)(c[j]-1);
				//printf("aowp[%d][%d]= %f\n",j,k,aowp[j][k]);
			}
			scanf("%c",&ch);
		}
    int cn=0;
			for(j=0;j<n;j++){
			owp[j]=0;cn=0;
                             for(k=0;k<n;k++){
                                              if(m[j][k]!='.'){
                                                               owp[j]+=aowp[k][j];cn++;//printf(" owp[%d] = %f k=%d\n",j,owp[j],k);
                                                               }
                                              }
                                              owp[j]=owp[j]/cn;//printf(" owp[%d] = %lf \n",j,owp[j]);
                             }
   for(j=0;j<n;j++){
                    oowp[j]=0;cn=0;
                    for(k=0;k<n;k++){
                                     if(m[j][k]!='.'){
                                                      oowp[j]+=owp[k];cn++;
                                                      }
                                     }
                                     oowp[j]=oowp[j]/cn;//printf(" oowp[%d] = %lf \n",j,oowp[j]);
                    }
                    printf("Case #%d:\n",i+1);
                    for(j=0;j<n;j++){
                                     printf("%0.7lf\n",wp[j]/4+owp[j]/2+oowp[j]/4);
                                     }
             	}
	return 0;
}
				
				
