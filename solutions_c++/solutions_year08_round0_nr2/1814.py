#include <algorithm>
#include<iostream>
#include<map>
#include<string>
using namespace std;
int main(){
    int n,t,na,nb,a[100000],b[100000];
    bool va[100],vb[100];
    string s;
    cin >> n;
    for(int i=1;i<=n;i++){
            
            cin >>t;
            cin >> na>>nb;
            for(int j=0;j<100000;j++) a[j]=b[j]=0;
            for(int j=0;j<na;j++){
                    cin >> s;
                    a[((s[0]-'0')*10+(s[1]-'0'))*3600+((s[3]-'0')*10+(s[4]-'0'))]--;;
                    cin >> s;
                    b[((s[0]-'0')*10+(s[1]-'0'))*3600+((s[3]-'0')*10+(s[4]-'0'))+t]++;
                    };
            for(int j=0;j<nb;j++){
                    cin >> s;
                    b[((s[0]-'0')*10+(s[1]-'0'))*3600+((s[3]-'0')*10+(s[4]-'0'))]--;;
                    cin >> s;
                    a[((s[0]-'0')*10+(s[1]-'0'))*3600+((s[3]-'0')*10+(s[4]-'0'))+t]++;
                    };
            int oa=0,ob=0;
            for(int j=0;j<95000;j++){
                     if(a[j]<0){ oa-=a[j]; a[j]=0;}
                     a[j+1]+=a[j];
                     if(b[j]<0){ ob-=b[j]; b[j]=0;}
                     b[j+1]+=b[j];
                     };
                     cout << "Case #"<<i<<": "<<oa<<" "<<ob<<endl;
            };
    
    return 0;   
};
