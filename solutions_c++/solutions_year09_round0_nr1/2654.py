#include<stdio.h>
#include<string.h>
int l,d,n;
char c[5000][16],p[5000];
int data[26][15];
int main(int argc,char **argv){
    int i,j,k,tmp;
    int index;
    int sum,min;
    scanf("%d %d %d",&l,&d,&n);
    for(i=0; i<d; i++){
        scanf("%s",c[i]);
    }
    /*for(i=0; i<d; i++){
        printf("+%s\n",c[i]);
    }/**/
    for(i=0; i<n; i++){
        sum = 0;
        for(j=0; j<26; j++){
            for(k=0; k<l; k++){
                data[j][k] = 0;
            }
        }
        scanf("%s",p);
        //printf("--%s\n",p);
        index=0;
        tmp = 0;
        for(j=0; j<strlen(p); j++){
            if(p[j] == '(') tmp = 1;
            else if(p[j] == ')'){ tmp = 0;  index++; } 
            else{            
                //printf("%d %c <%d>\n",index,p[j],p[j]-'a');
                data[p[j]-'a'][index]++;               
                if(tmp == 0){ index++;}
            }            
        }
        /*for(j=0; j<26; j++){
            for(k=0; k<l; k++){
                printf("%d ",data[j][k]);
            }
            printf("\n");
        }/**/
        
        for(j=0; j<d; j++){
            min=999999999;
            for(k=0; k<l; k++){
                //printf(" == %d %c\n",data[c[j][k]-'a'][k],c[j][k]);
               if(data[c[j][k]-'a'][k] < min){
                    min = data[c[j][k]-'a'][k];                    
               }
            }
            //printf("Min : %d\n",min);
            sum+=min;
        }
        printf("Case #%d: %d\n",i+1,sum);
    }
   
    return 0;
}
