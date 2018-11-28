#include<iostream>
#include<vector>
#include<map>
using namespace std;
string getstr(string &s,int index=0){
        string out;int i;
        for(i=index;i<s.size() && s[i]!='/';i++){
                out.push_back(s[i]);
        }
        if(i!=s.size())
                out.push_back('/');
        return out;
}
main(){

        int t;
        cin>>t;
        for(int g=1;g<=t;g++){
                int n,m;
                cin>>n>>m;
                vector<string> str(n);map<string,bool> ma;
                ma["/"]=1;
                for(int i=0;i<n;i++){
                        cin>>str[i];int l=0;
                        while(1){
                                string out = getstr(str[i],l);
                                if(!out.size())
                                        break;
                                l+=out.size();
                                ma[str[i].substr(0,l-1)]=1;
                        }
                }
                ma[""]=1;
                int ct=0;
                while(m--){
                        string str;
                        cin>>str;int l=0;
                        while(1){
                                        string out = getstr(str,l);
                                        if(!out.size())
                                                break;
                                        l+=out.size();
                                        if(ma.find(str.substr(0,l-1))==ma.end()){
                                                ma[str.substr(0,l-1)]=1;
                                                ++ct;
                                        }
                        }
                }
                cout<<"Case #"<<g<<": "<<ct<<endl;
        }
        return 0;
}
