#include<iostream>
#include<vector>
#include<string>
#include<list>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<map>

#define LE length()
#define PB push_back
#define SL size()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

using namespace std;

int calc(int n){
    int res=0,ac;
    while(n){
       ac = n%10; n/=10;
       res += (ac*ac);
    }
    return res;
}

string convert(int n,int b){
       string res="";
       while(n>=b){
           res.PB(n%b); n/=b;
       } res.PB(n); reverse(res.begin(),res.end());
       while(res.SL>0 && res[0]==0)res.erase(res.begin());
       return res;
}

void print(string n){for(int i=0;i<(int)n.LE;i++){n[i]+='0';} cout<<n;}

bool happy(string n,int b){
     map<string,bool> m;
     map<string,bool>::iterator it=m.end();
   //  cout<<m.SL<<" "<<b<<" ";print(n);cout<<endl; system("pause");
     m[n] = true;
     while(it==m.end()){
          int ac=0;
          for(int i=0;i<(int)n.LE;i++) ac += (n[i]*n[i]); 
          n = convert(ac,b); //cout<<m.SL<<" "<<b<<" "<<ac<<" ";print(n);cout<<endl; system("pause");
          if((int)n.SL==1 && n[0] == 1) return true;
          it = m.find(n);
          m[n] = true;
     }
     return false;
}

int main(){
    int kases; cin>>kases;
    string s; getline(cin,s);
    for(int k=1;k<=kases;k++){
       getline(cin,s);
       stringstream ss(s); int base;
       vector<int> v; 
       while(ss>>base){
           v.PB(base);
       }
       sort(v.begin(),v.end());
       int res=-1;
       for(int i=2;;i++){ //cout<<"I:"<<i<<endl;
          bool ok=true;
          for(int j=0;j<(int)v.SL;j++){
             if(!happy(convert(i,v[j]),v[j])){ok=false;break;}
          }
          if(ok){res = i;break;}
       }
       cout<<"Case #"<<k<<": "<<res<<endl;
    }
}
