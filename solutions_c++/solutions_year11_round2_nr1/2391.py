#include<stdio.h>
int main()
{
    int t,n,k,i,j,count,countw,l;
    double w[105],ow[105],wl[105],oow[105],rpi;
    char str[105][105];
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d",&n);
        for(j=0;j<n;j++){                     
            scanf("%s",str[j]);
            count = 0;
            countw = 0; 
            for(k=0;k<n;k++){
                if(str[j][k]!='.')
                   count++;
                if(str[j][k]=='1')
                   countw++;                    
            }
            w[j] = countw * 1.0 / count ; 
        }
        
        for(j=0;j<n;j++){
            ow[j] =0;
            for(l=0;l<n;l++){
            count  = 0;
            countw=0;
            for(k=0;k<n;k++){
                if(str[l][k]!='.'&&j!=k)
                   count++;
                if(str[l][k]=='1'&&j!=k)
                   countw++;                    
            }
            wl[l] = countw * 1.0 / count ;
            //  printf("%d %d\n",count,countw); 
            // printf("%f\n",wl[l]);
             }             
             //printf("\n");
             count  = 0;
            for(k=0;k<n;k++){
                if(str[j][k]!='.'){
                     count++ ;
                     ow[j]+=wl[k];  
                     }          
                }
                ow[j]=ow[j]/count;
               // printf("%f\n",ow[j]);                  
            }
       for(j=0;j<n;j++){
            count = 0;
            oow[j] = 0;           
            for(k=0;k<n;k++){
                if(str[j][k]!='.'){
                     count++;
                     oow[j]+=ow[k];
                     }            
                }
                
                oow[j] = oow[j] / count ;
                 // printf("%f\n",oow[j]);                     
            }
    printf("Case #%d:\n",i+1);     
    for(j=0;j<n;j++){
        rpi =    0.25 * w[j] + 0.50 * ow[j] + 0.25 * oow[j];
        printf("%f\n",rpi);
        }        
    }
    return 0;
}
