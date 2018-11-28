#include<iostream>
#include<cstring>

using namespace std;

int main(){
  int t;
  int n[101],m=0;
  cin>>t;
  for(int i=1;i<=t;i++){
    cin>>n[i];
    if(n[i]>m) m=n[i];
  }
  int s[501][501],c[501][501],a[501];
  c[0][0]=1;
  for(int j=1;j<m;j++){
    c[j][0]=c[j][j]=1;
    for(int k=1;k<j;k++)
      c[j][k]=(c[j-1][k-1]+c[j-1][k])%100003;
  }
  for(int j=2;j<=m;j++){
    a[j]=s[j][1]=1;
    for(int k=2;k<j;k++){
      for(int l=1;l<k;l++)
        s[j][k]=(s[j][k]+s[k][l]*(long long)c[j-k-1][k-l-1])%100003;
      a[j]=(a[j]+s[j][k])%100003;
    }
  }
  for(int i=1;i<=t;i++)
    cout<<"Case #"<<i<<": "<<a[n[i]]<<endl;
  return 0;
}


