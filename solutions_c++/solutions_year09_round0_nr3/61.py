#include<iostream>
#include<string>
using namespace std;

string arr="welcome to code jam",st;
int best[20][505];

int sol(int a,int b)
{
 //cout<<a<<" "<<b<<"  "<<best[1][2]<<endl;
 if(best[a][b]!=-1)return best[a][b];
 if(a==arr.size())return 1;
 if(b==st.size()){return 0;}
 
 int ans=(sol(a,b+1))%10000;
 if(arr[a]==st[b])
 ans+=sol(a+1,b+1);
 ans%=10000;
 return best[a][b]=ans;  
    
}
int T,k;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>T;
    
                    char c[1005];
    cin.getline(c,1000);
    for(k=0;k<T;k++)
    {
                    memset(best,-1,sizeof best);
                    cin.getline(c,1000);
                    st=c;
                    int ans=sol(0,0);
                    cout<<"Case #"<<k+1<<": ";
                    if(ans<10)
                    cout<<"000"<<ans<<endl;
                    else if(ans<100)
                    cout<<"00"<<ans<<endl;
                    else if(ans<1000)
                    cout<<"0"<<ans<<endl;
                    else
                    cout<<ans<<endl;
                                    
                    
                    
                    
                    
    }
    //cin>>st;
    
    
 return 0;   
}
