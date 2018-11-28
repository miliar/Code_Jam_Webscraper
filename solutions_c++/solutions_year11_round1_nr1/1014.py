#include<iostream>
using namespace std;
int t,pd,pg;
long long n;
int main(){
    //freopen("A.out","w",stdout);
    scanf("%d",&t);
    for (int z=1;z<=t;z++){
        scanf("%I64d %d %d",&n,&pd,&pg);
        if (pg==100 && pd!=100) printf("Case #%d: Broken\n",z);
           else 
            if (pg==0 && pd!=0) printf("Case #%d: Broken\n",z);
            else{
                int ans=0;
                /*if (pd%2==0){
                   if (pd%10==0){
                       if (n>=5) ans=1;
                       if (pd==100) ans=1;
                   }
                   else{
                        if (n>=25 && (pd%2)%2==0) ans=1;
                        if (n>=50) ans=1;
                   }
                }
                else{
                     if (n>=100) ans=1;
                }*/
                
                int pd1,n1;
                int x=100;
                int pd2=0;
                pd1=pd;

                while (++pd2 && pd1!=0) 
                      if (pd1%2) break;
                         else{pd1=pd1/2;if (x%2==0)x=x/2;}
                int pd5=0;
                pd1=pd;
                while (++pd5 && pd1!=0) 
                      if (pd1%5) break; else{ pd1=pd1/5;if (x%5==0)x=x/5;}
                
                //printf("%d",x);
                if (n>=x) 
                   ans=1;
                if (pd==0) ans=1;
                if (ans) printf("Case #%d: Possible\n",z);
                else printf("Case #%d: Broken\n",z);
            }
    }
} 
