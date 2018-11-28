#include<stdio.h>   
#include<stdlib.h> 
#include<string.h>
int main(void){   
    char* p=(char*)malloc(11*sizeof(char));
    char* q=(char*)malloc(11*sizeof(char));
    int i,j,t,tmp;
    long ans,k,l,c,d,m,n;
    scanf("%d",&t);
    //FILE* z;
    //z = fopen ("C:\\myfile.txt","w");
    for(i=0;i<t;i++){
        ans=0;
        scanf("%ld%ld",&c,&d);
        for(k=c;k<=d;k++){
            for(l=k+1;l<=d;l++){
              sprintf(p,"%ld",k);
              sprintf(q,"%ld",l);  
              if(strlen(p)==strlen(q)){
                for(m=0;m<strlen(p);m++){
                    if(p[strlen(p)-1]==q[m]){
                        tmp=m;
                        for(n=strlen(p)-1;n>=0;n--){
                            if(p[n]!=q[tmp])
                                break;
                            tmp--;
                            if(tmp<0)
                                tmp+=strlen(p);
                        }
                        if(n<=-1){
                            ans++;
                            //printf("%s %s\n",p,q);
                            m=strlen(p);
                        }
                    }
                }          
              }
            }
        }
        //fprintf(z,"Case #%d: %ld\n",i+1,ans); 
        printf("Case #%d: %ld\n",i+1,ans);
    }
    //fclose(z);
    //system("pause");
    return 0;
}

