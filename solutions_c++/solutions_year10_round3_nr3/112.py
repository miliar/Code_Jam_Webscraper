#include<iostream>
using namespace std;
int main(){
    int count,t,num=0,m,n,ms,s,i,j,mx,my,f,k,a[512][512]={0},size[515];
    char c;
    cin>>t;
    while(t--){
        
        cin>>m>>n;
        for(i=0;i<515;i++)size[i]=0;
        for(i=0;i<m;i++)
            for(j=0;j<n/4;j++){
                cin>>c;
                //cout<<"\""<<c<<"\"";
                if(c>='0'&&c<='9')c-='0';
                else c=c-'A'+10;
                a[i][j*4]=(c&0x8)>>3;
                a[i][j*4+1]=(c&0x4)>>2;
                a[i][j*4+2]=(c&0x2)>>1;
                a[i][j*4+3]=(c&0x1);
                //cout<<a[i][j*4]<<a[i][j*4+1]<<a[i][j*4+2]<<a[i][j*4+3]<<endl;
                }
      
        while(true){    
        ms=mx=my=-1;
        for(i=0;i<m;i++)
            for(j=0;j<n;j++)if(a[i][j]!=2){
                s=1;
                f=0;
                while(f==0){
                for(k=0;k<s&&f==0;k++)
                    if((a[i+k][j+s]+a[i+k][j+s-1])!=1){f=1;}
                for(k=0;k<=s&&f==0;k++)
                    if((a[i+s][j+k]+a[i+s-1][j+k])!=1){f=1;}
                s++;
               // cout<<s<<" "<<i<<" "<<j<<" "<<f<<endl;
                //cin>>count;
                }
                s--;
                if(s>ms){ms=s;mx=i;my=j;}
                }
        if(ms==-1)break;
        size[ms]++;
        for(i=0;i<ms;i++)
            for(j=0;j<ms;j++)a[mx+i][my+j]=2;
       // cout<<ms<<" "<<mx<<" "<<my<<endl;
        //for(i=0;i<m;i++){
          //  for(j=0;j<n;j++)cout<<a[i][j];
          //cout<<endl;}
        //cin>>count;
        }
        count=0;
        for(i=(m>n)?n:m;i>0;i--)if(size[i]>0)count++;
        cout<<"Case #"<<++num<<": ";
        cout<<count<<endl;
        for(i=(m>n)?n:m;i>0;i--)if(size[i]>0)cout<<i<<" "<<size[i]<<endl;
        }
    return 0;
    }
