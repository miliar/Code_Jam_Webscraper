#include<iostream>
#include<fstream>
#include<string>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    string ss="welcome to code jam";
    void pri(int i,int j){
      fout<<"Case #"<<i+1<<": ";
      if(j/1000>0)
        fout<<j<<endl;
      else if(j/100>0)
             fout<<"0"<<j<<endl;
           else if(j/10>0)
                   fout<<"00"<<j<<endl;
                else fout<<"000"<<j<<endl;
    }
int main(){
    int n;
    fin>>n;
    string s;
    getline(fin,s);
    for(int i=0;i<n;i++){
      getline(fin,s);
      int num=0,l=s.length();
      int a[l][18];
      for(int j=0;j<l;j++)
        if(s[j]=='w')
          a[j][0]=1;
        else a[j][0]=0;
      for(int t=1;t<18;t++)
        for(int j=0;j<l;j++){
          a[j][t]=0;
          if(s[j]==ss[t])
            for(int k=0;k<j;k++)
              if(s[k]==ss[t-1])
                a[j][t]+=a[k][t-1];
        }
      for(int j=0;j<l;j++)
        if(s[j]=='m')
          for(int k=0;k<j;k++)
            if(s[k]=='a')
              num+=a[k][17];
      pri(i,num);
    }
    return 0;
}
        
