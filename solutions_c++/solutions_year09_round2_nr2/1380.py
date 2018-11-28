#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int a[20],flag,j,tmp,i;
    int t,count=0;
    char s[25];
    long long n;
    cin>>t;
    while(t--){
        cin>>n;
        int numb[10]={0};
        long long tmp=n;
        while(tmp){
            numb[tmp%10]++;
            tmp=tmp/10;
        }
        flag=0;
        while(flag==0){
            tmp=++n;
            int numb2[10]={0};
            while(tmp)
            {
                numb2[tmp%10]++;
            tmp=tmp/10;
        }
        flag=1;
        for(i=1;i<10;i++)if(numb[i]!=numb2[i]){flag=0;break;}
        
        }
        cout<<"Case #"<<++count<<": "<<n<<"\n";
    }
    return 0;
}
        /*int i=-1,num=0;
        while(s[++i])a[num++]=s[i];
        for (i=0;i<num;i++)
            for(j=i+1;j<num;j++){
                if(a[j-1]>a[j]){tmp=a[j];
                                a[j]=a[j-1];
                                a[j-1]=tmp;
                            }
        for(i=num-1;i>=0;i--){
            if(s[i]!=a[i]){
                if(i==num-1){
                tmp=s[i];
                s[i]=s[i-1];
                s[i-1]=s[i];
                break;}
                for(j=i;j<
            }
          */  
                
