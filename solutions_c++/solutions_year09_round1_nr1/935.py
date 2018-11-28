#include<iostream>
#include<fstream>
#include<string>
#include<set>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
   const int tt=99000,kk=20;
   bool e[tt][kk],f[tt][kk];
   void pri(int i,int j){
      fout<<"Case #"<<i+1<<": "<<j<<endl;
   }
   bool aa(int k,int m){
        set<int> q;
        while(q.count(k)==0){
          q.insert(k);
          int t=k,l=0;
          while(t>0){
            l+=(t%m)*(t%m);
            t=t/m;
          }
          k=l;
        }
        return k==1;
   }
   bool bb(int l,int b[],int k){
        bool mark=true;
        for(int i=0;i<k;i++){
          if(b[i]<kk&&l<tt&&e[l][b[i]]==false){
            e[l][b[i]]=true;
            f[l][b[i]]=aa(l,b[i]);
          }
          if((l<tt&&b[i]<kk&&!f[l][b[i]])||((b[i]>=kk||l>=tt)&&!aa(l,b[i]))){
            mark=false;
            break;
          }
        }
        return mark;
   }
int main(){
    int n;
    string s;
    fin>>n;
    getline(fin,s);
    for(int i=0;i<tt;i++)
      for(int j=2;j<kk;j++){
            e[i][j]=false;
            f[i][j]=false;
    }
    for(int i=0;i<n;i++){
            getline(fin,s);
            int k=0,b[9],w=0;
            for(int j=0;j<s.length();j++)
              if(s[j]>='0'&&s[j]<='9')
                w=w*10+s[j]-'0';
              else{
                b[k]=w;
                w=0;
                k++;
              }
           b[k]=w;
           k++; 
           int l=2;
           while(!bb(l,b,k))
             l++;
           pri(i,l);
    }
    return 0;
} 
