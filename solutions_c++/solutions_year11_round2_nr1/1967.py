#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
double wp[102],owp[102][104],oowp[198],owpp[103];
int main(){
    int T,n;
      freopen ("A-large.in","r",stdin);
      freopen ("Ab.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        string s[104];
        cin>>n;
        for(int i=0;i<n;i++){cin>>s[i];}
        for(int i=0;i<n;i++){
            double cnt=0,ans=0;
            for(int j=0;j<n;j++){
                if(s[i][j]!='.'){
                    cnt+=1;
                    if(s[i][j]=='1'){
                        ans+=1;
                    }
                }
            }
            wp[i]=ans/cnt;
            
           // rp[i]+=(0.25*wp[i]);
        }
        
        for(int i=0;i<n;i++){
            double tt=0;
            int num=0;
            for(int j=0;j<n;j++){
                if(s[i][j]!='.'){
                    num++;
                    double cnt=0,ans=0;
                    for(int k=0;k<n;k++){
                        if(k==i)continue;
                        if(s[j][k]!='.'){
                            cnt+=1;
                            if(s[j][k]=='1')
                                ans+=1;
                        }
                    }
                    owp[i][j]=ans/cnt;
          //          cout<<owp[i][j]<<endl;
                    tt+=owp[i][j];
                }
                
            }
            owpp[i]=tt/num;
        //    cout <<owpp[i]<<endl;
        }
        for(int i=0;i<n;i++){
            double cnt=0,ans=0;
            for(int j=0;j<n;j++){
                if(s[i][j]!='.'){
                    cnt+=1;
                    ans+=owpp[j];
                  //  cout<<owpp[j]<<endl;
                }
            }
          //  cout<<endl;
            oowp[i]=ans/cnt;
            
        }
        cout<<"Case #"<<cas<<":"<<endl;
        for(int i=0;i<n;i++)
        {
        //    cout<<wp[i]<<" "<<owpp[i]<<" "<<oowp[i]<<endl;
           cout<<0.25 * wp[i] + 0.50 * owpp[i] + 0.25 * oowp[i]<<endl;
        }
        
    }
}   
                    
                    
                    
