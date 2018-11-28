#include<iostream>
#include<algorithm>
 
using namespace std;
long long calc(int x){
    long long sthing=1;
    for (int i=0;i<x;i++) sthing*=10;
    return sthing;
}
 
int main()
{
 
    // freopen("y.in" , "r" , stdin);
        //freopen("y.out" , "w" , stdout);
    int t,check;
    cin >> t;
 
    for (int i=1;i<=t;i++){
        long long a,b;
       
        cin >> a >> b;
        int length=1;
        
        int dig=b;
        while (dig/=10) length++;
        long long total=0;
        for (long long j=a;j<=b;j++){long long arr[]={0,0,0,0,0,0,0};
            for (int k=1;k<length;k++)
       {        check=0;
                long long temp=(j%calc(k))*calc(length-k)+(j/calc(k));
                arr[k-1]=temp;
                for(int m=0;m<k-1;m++){if(temp==arr[m])check++;}
                if (temp != j && temp >= a && temp <= b&&check==0) total++;
       }
 
        }
 
        cout << "Case #" << i << ": " << total/2 << "\n";
 
    }
 
    return 0;
}