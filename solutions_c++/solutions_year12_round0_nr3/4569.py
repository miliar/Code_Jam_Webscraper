#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct string{
    char s[10];
    };
struct string ch[10] ;


void check(int n,int a,int b,int *c){
    
    sprintf(ch[0].s,"%d",n);
    int l = strlen(ch[0].s);
    int i=0,j=0 ,m=0;
    strcpy(ch[1].s,ch[0].s);
    
    
       
    for(i=1;i<l;i++){
        
        strcpy(ch[i+1].s,ch[i].s);
        
        for(j=0;j<l;j++)
            ch[i+1].s[(j+1)%l]=ch[i].s[j];
            
        //printf("%s - %s",ch[i].s,ch[i+1].s);
        
        if(ch[i].s[l-1]!='0'){
            m = atoi(ch[i+1].s);
            if(m <= b && m>n)  
                *c=*c+1; 
          }
            
       // printf("-->%d ..... %d. .... \n",m,*c);
      
         //system("pause");
        }
    
    }

int main(){
    int f;
    char out[30];
    sprintf(out,"output3.txt",f);
    freopen(out,"w",stdout);
    
    int t;
    int a,b ;
    scanf("%d",&t);
    
    int i,j ;
    for(i=0;i<t;i++){
        scanf("%d %d",&a,&b);    
        int count = 0;
        for(j=a;j<b;j++){
            check(j,a,b,&count);
            }
        printf("Case #%d: %d\n",i+1,count);
        }
        
    //system("pause");
    return 0;
    }
