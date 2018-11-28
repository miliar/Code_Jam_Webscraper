#include<iostream>
#include<string>
using namespace std;
bool ch[1000],ch1[1000],bb[70];
long long a[1000];
long long b[70];
void beforework(int x,int len){
     b[1]=1;
     for (int i=2;i<=len;i++)
     b[i]=b[i-1]*x;
}
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    int tt=0;
    cin>>t;
    for (int tt=1;tt<=t;tt++){
    memset(ch,0,sizeof(ch));
    memset(ch1,0,sizeof(ch1));
    memset(bb,0,sizeof(bb));
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    string s;
    int total=0;
    cin>>s;
    for (int i=0;i<s.size();i++)
    if(!ch[s[i]]){
         total++;
         ch[s[i]]=true;
    }
    if (total<2) total=2;
    int tot=0;
    a[s[0]]=1;
    ch1[s[0]]=true;
    beforework(total,s.size());
    long long ans=0;
    ans+=b[s.size()];
    bb[1]=true;
    for (int i=1;i<s.size();i++){
        if (ch1[s[i]]){
              ans+=a[s[i]]*b[s.size()-i];
        }else{
              ch1[s[i]]=true;
              a[s[i]]=tot;
              tot++;
              while (bb[tot]) tot++;
              ans+=a[s[i]]*b[s.size()-i];
        }
    }
    cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
