#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int c=0,a[20],flag,j,tmp,i,len;
    int t,count=0;
    char s[65];
    unsigned long long n;
    //cout<<(unsigned long long)-1;
    cin>>t;
    while(t--){
        n=0;
        int ch[256]={-1};
        for(i=0;i<256;i++)ch[i]=-1;
        cin>>s;
        len=0;
        while(s[len++]);len--;
        count=0;
        if(len!=0){
        //ch[s[1]]=0;ch[s[0]]=1;
        
        for (i=0;i<len;i++)
            if(ch[s[i]]==-1)
                if(count==0||count==1)
                {ch[s[i]]=!count;count++;}
                else ch[s[i]]=count++;
        count=(count>1)?count:2;
        //for(i=0;i<len;i++)cout<<s[i]<<" "<<ch[s[i]]<<endl;
        for(i=0;i<len;i++){
            n=n*count+ch[s[i]];
            //cout<<"hey"<<n<<" ";
        }
        }
    cout<<"Case #"<<++c<<": "<<n<<endl;
    }
return 0;
}        
