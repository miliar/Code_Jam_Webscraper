#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<map>


int a,b,l,n;
char c[1000],t[1000];

void create(int x)
{
    itoa(x,c,10);
    l=strlen(c);   
    strcpy(t,c);
    strcat(c,t);        
//    printf("%s ",c);
}
int nub(int a,int b)
{
    int k=0,count=0;
    int chk[10];
    
    for(int i=0;i<10;i++)
    chk[i]=0;
    
    for(int i=0;i<l;i++)
    {   
        int j=0,ch=0,p=0;
                
        for(j=i;j<i+l;j++)
        t[j-i]=c[j];        
        t[j-i]='\0';        
        k=atoi(t);        
       // printf("%d\n",k);
       for(ch=0;ch<10;ch++)
       if(chk[ch]==k) break; 
             
       if(k<=b&&k>a&&ch==10) {chk[p++]=k; /*printf("%d-%d\n",a,k);*/ count++;}       
    }
    return count;
}

int main(){
   freopen("output3.txt","w",stdout);
    scanf("%d",&n);    
    for(int i=0;i<n;i++)
    {   int count=0;
    
        scanf("%d %d",&a,&b);
        for(int j=a;j<b;j++)
        {

           create(j);
           count+=nub(j,b);        
        }                    
        printf("Case #%d: %d\n",i+1,count);
    }    
   // system("pause");
    return 0;
}
