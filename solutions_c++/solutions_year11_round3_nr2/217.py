#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int a[1000001];
long long b[1000001],B;
int main(){
    int C,Case=1,l,n,c;
    long long t,sum,save;
    scanf("%d",&C);
    while(C--){
        cin>>l>>t>>n>>c;
        sum=0;
        for(int i=0;i<c;i++){
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        sum*=n/c;
        for(int i=0;i<n%c;i++)
            sum+=a[i];
        printf("Case #%d: ",Case++);
        if(t>sum||l==0)
            cout<<sum*2<<endl;
        else{
            int i;
            long long temp;
            sum=0;
            for(i=0;i<n;i++){
                sum+=a[i%c];
                if(sum>(t>>1))
                    break;
            }
            temp=sum-(t>>1);
            b[0]=temp,B=1;
            for(i++;i<n;i++){
                b[B++]=a[i%c];
                sum+=a[i%c];
            }
            sort(b,b+B);
            save=0;
            for(int i=B-1;i>=0&&l>0;i--)
                save+=b[i],l--;
            cout<<(sum<<1)-save<<endl;
        }
    }
}
