#include<iostream>
#include<cstdio>
using namespace std;
bool isluc(int n,int l){
    int m,sum=n;
    bool ch[1000000]={0};
    while(!ch[sum]){
        ch[sum]=1;
        m=sum;
        sum=0;
        while(m){
            sum+=(m%l)*(m%l);
            m=m/l;
        }
       
        
            }
   // cout<<n<<" "<<l<<" "<<sum<<" hey\n";
    return (sum==1);
}
int main(){
    int base[10],t,n,i,j,l,num,flag;
    cin>>t;
    i=1;
    getchar();
    while(i<=t){
        char c=getchar();
        num=0;
        for(j=0;j<10;j++)
            base[j]=0;
        while((c!='\n')&&(c!='\r'))
        {
            if(c==' ')num++;
            else base[num]=base[num]*10+c-'0';
            c=getchar();
            }
        //for(j=0;j<=num;j++)cout<<base[j]<<" ";
        for(j=2;;j++){
            n=j;flag=0;
            l=0;
            while(flag==0&&l<=num)
            {
                if(!isluc(n,base[l]))flag=1;
            l++;
            }
            if (flag==0)break;
        }
        cout<<"Case #"<<i<<": "<<j<<endl;
        i++;
    }
return 0;

}
