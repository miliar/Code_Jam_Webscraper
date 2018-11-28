#include<iostream>
#include<cstring>
#include<cstdlib>
using namespace std;

int T,A,B,t,ans;
bool flag[1000000];

string n2s(int n){
       string temp,out;
       while (n!=0) {
             temp+=(n%10-0+'0');
             n/=10;
       }
       for (int i=0;i<temp.length();i++) out+=temp[temp.length()-1-i];
       return out;
}

int s2n(string s){
    int out=0;
    for (int i=0;i<s.length();i++) out=out*10+(s[i]-'0');
    return out;
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>T;t=0;
    int n,nc,ntt;string ns,nt;
    while (T--) {
          t++;cin>>A>>B;ans=0;
          memset(flag,0,sizeof(flag));
          for (n=A;n<=B;n++) {
              nc=1;
              if (flag[n-A]) continue;
              flag[n-A]=1;
              ns=n2s(n);
              for (int i=1;i<ns.length();i++) {
                  nt.clear();
                  nt+=ns[i];
                  for (int j=(i+1)%ns.length();j!=i;j=(j+1)%ns.length()) nt+=ns[j];
                  ntt=s2n(nt);
                  if (nt[0]=='0') continue;
                  else if ((ntt>=A)&&(ntt<=B)&&(!flag[ntt-A])) {nc++;flag[ntt-A]=1;} 
              }
              ans+=nc*(nc-1)/2;
          }
          cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
