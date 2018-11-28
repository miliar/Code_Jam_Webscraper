#include<iostream>
#include <fstream>
#include<cmath>
#include<string>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    int a[44],b[44],c[44],t,n,d[44];
    bool f[44];
void pri(int a,int b){
     fout<<"Case #"<<a<<": "<<b<<endl;
}
int aa(int k1,int k2){
    if(k1+1==k2)
      return 0;
    int t1=k1,t2=(k1+k2)/2,sum=aa(k1,(k1+k2)/2)+aa((k1+k2)/2,k2);
    for(int p=k1;p<k2;p++){
            if(t2==k2||(t1<(k1+k2)/2&&c[t1]<=c[t2])){
              d[p]=c[t1];
              t1++;
            }
            else{
                 d[p]=c[t2];
                 t2++;
                 sum+=((k1+k2)/2-k1-(t1-k1));
                 }
    }
    for(int p=k1;p<k2;p++)
      c[p]=d[p];
    return sum;
}
int main(){
    fin>>t;
    int temp=t;
    while(t--){
      fin>>n;
      string s;
      getline(fin,s);
      for(int i=0;i<n;i++){
              getline(fin,s);
              int ma=0;
              for(int j=0;j<n;j++)
                if(s[j]=='1')
                  ma=j;      
              a[i]=ma;
      }
      for(int i=0;i<n;i++)
        f[i]=true;
      for(int i=0;i<n;i++)    
        for(int j=0;j<n;j++)
          if(f[j]&&a[j]<=i){
            f[j]=false;
            c[j]=i;
            break;
          }
      pri(temp-t,aa(0,n));
    }
    return 0;
}
