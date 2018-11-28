#include<iostream>
#include<string>
using namespace std;
int main(){
    int t;
    cin>>t;
    cin.get();
    string tmp;
    string base="ynficwlbkuomxsevzpdrjgthaq";
    for(int z=1;z<=t;z++){
        getline(cin,tmp);
        string ans="";
        for(int i=0;i<tmp.length();i++){
            if(tmp[i]>='a'&&tmp[i]<='z'){
                ans+=(base.find(tmp[i])+'a');
            }
            else ans+=tmp[i];
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
}
