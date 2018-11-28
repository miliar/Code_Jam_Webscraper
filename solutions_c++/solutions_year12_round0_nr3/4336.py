#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
int main(){
    int test,l=1;
    cin>>test;
    while(test--)
    {
    
    int a,b,count=0;
    cin>>a>>b;
    for(int i=a;i<=b;i++ )
    {
            int j=i,m=1;
            int digit;
            if(i<=9)
            digit=1;
            else if(i<100)
            digit=2;
            else  if(i<1000)
            digit=3;
            else
            digit=4;
            while(j)
            {       
                    int p=pow(10,(float)m); 
                    int k=i%p;
                    int q=i/p;
                    q=k*(pow(10,(float)(digit-m)))+q;
                   // cout<<q<<endl;
                    if(q<=b && q>i )
                    count++;
                    j=j/10;
                    m++;
            }
    } 
    printf("Case #%d: %d\n",l++,count);            
    }   

return 0;
}
