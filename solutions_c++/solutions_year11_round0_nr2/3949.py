#include<stdio.h>

int main(){
int i,j,k,l,n,d,c,t,k1=0,f,h,p,f2;
char combine[500][1000],oppose[500][1000],str[10000],list[10000];
FILE *pt=fopen("out.txt","w");
scanf("%d",&t);
				for(i=0;i<t;i++){k1=0;
								scanf("%d",&c);
								for(j=0;j<c;j++)
								scanf("%s",combine[j]);
								scanf("%d",&d);
								for(j=0;j<d;j++)
								scanf("%s",oppose[j]);
								scanf("%d",&n);
								scanf("%s",str);
							for(k=0;k<n;k++){f=0;f2=0;
									
									for(p=0;p<d;p++){
									if(oppose[p][0]==str[k]){
										for(h=0;h<k1;h++){
										if(list[h]==oppose[p][1])
										{k1=0;
										f=1;
										break;
										}
														}
															}
										
										if(f==1)
									    break;
									
									
									
									if(oppose[p][1]==str[k]){
										
										for(h=0;h<k1;h++){
										if(list[h]==oppose[p][0]){
										k1=0;f=1;break;          }
															}
										if(f==1)
									break;
									
															}
									
									
									}
									if(f==1)
									continue;
								///////////////////////////////////////////
								for(p=0;p<c;p++){
									if(combine[p][0]==str[k]&&combine[p][1]==str[k+1]){
									list[k1++]=combine[p][2];k++;f2=1;break;}
									if(combine[p][1]==str[k]&&combine[p][0]==str[k+1]){
									list[k1++]=combine[p][2];k++;f2=1;break;}
									}
									if(f2==1)
									continue;
								///////////////////////////////////////////
									list[k1++]=str[k];
							
							}	
							
							
							if(k1==0)
							fprintf(pt,"Case #%d: []\n",i+1);
							if(k1==1)
							fprintf(pt,"Case #%d: [%c]\n",i+1,list[0]);
							if(k1>1){
							fprintf(pt,"Case #%d: [",i+1);
							for(h=0;h<k1-1;h++)
					fprintf(pt,"%c, ",list[h]);
						fprintf(pt,"%c]\n",list[k1-1]);
						}			
					}	

fclose(pt);
}
