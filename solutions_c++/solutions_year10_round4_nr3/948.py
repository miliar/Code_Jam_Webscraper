#include<stdio.h>
#include<string.h>

char mmap[110][110];

int c,r;

int in(int a,int b,int c){
    if(c>=a&&c<=b)   return 1;
    if(c>=b&&c<=a)   return 1;
    return 0;
}


int main(){

    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("cout.txt","w",stdout);
    scanf("%d",&c);
    int ccount = 0;
    while(c--){
        for(int i=0;i<=100;i++)
           for(int j=0;j<=100;j++)
              mmap[i][j]  ='0';
        scanf("%d",&r);
        while(r--){
           int a,b,c,d;
           scanf("%d %d %d %d",&a,&b,&c,&d);
           for(int i=1;i<=100;i++)
              for(int j=1;j<=100;j++){
                  if(in(a,c,i)==1&&in(b,d,j)==1)
                     mmap[i][j]  ='1';
              }
        }


        int ans = 0;
        int has = 0;
        for(int i=1;i<=100;i++)
           for(int j=1;j<=100;j++)
              if(mmap[i][j]=='1')  has ++;
        while(has>0){
           ans ++;
           for(int i=100;i>=1;i--)
              for(int j=100;j>=1;j--)
                if(mmap[i][j]=='1'){
                   if(mmap[i-1][j]=='0'&&mmap[i][j-1]=='0'){
                      mmap[i][j]   = '0';
                      has--;
                   }
                }
           for(int i=100;i>=1;i--)
              for(int j=100;j>=1;j--)
                 if(mmap[i][j]=='0'){
                    if(mmap[i-1][j]=='1'&&mmap[i][j-1]=='1'){
                       mmap[i][j] = '1';
                       has++;
                    }
                 }

        }

        printf("Case #%d: %d\n",++ccount,ans+1);
    }

    return 0;
}
