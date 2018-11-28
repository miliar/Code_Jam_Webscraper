#include<stdio.h>
#include<string.h>
#include<ctype.h>

//char eng[]={a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
//char gog[]={y,n,f,i,c,w,l,b,k,u,o,m,x,s,e,v,z,p,d,r,j,g,t,h,a,q};

char gog[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char eng[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char in[150];
int main(){
int t,count=1;
scanf("%d\n",&t);
while(t--){          
          gets(in);
           int i=0;
           for(;in[i];i++){
                          // printf("%d",in[i]-'a');
                          if(islower(in[i]))
                           in[i]=eng[gog[in[i]-'a']-'a'];
                           }
          printf("Case #%d: %s\n",count++,in);
           }

}
