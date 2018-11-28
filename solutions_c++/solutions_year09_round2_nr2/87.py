#include<iostream>
using namespace std;

int ct[10];
bool work(string& s){
        int n,i,j;
        n=s.length();
        for (i=0;i<10;++i) ct[i]=0;

        for (i=n-2;i>=0;--i) if (s[i]<s[i+1]) break;
        if (i<0){
            s=string("0")+s;
            return false;
        }
        for (j=i+1;j<n;++j) ++ct[s[j]-48];
        for (j=s[i]-47;j<10;++j) if (ct[j]) break;
        ++ct[s[i]-48];
        --ct[j];
        cout<<s.substr(0,i)<<j;
        for (j=0;j<=9;++j){
            while (ct[j]){
                --ct[j];
                cout<<j;
            }
        }
        cout<<endl;
        return true;
}

int main(){
    int Ncase,Ci;
    cin>>Ncase;
    string s;
    for (Ci=1;Ci<=Ncase;++Ci){
        cout<<"Case #"<<Ci<<": ";
        cin>>s;
        while (!work(s));
    }
    return 0;
}
