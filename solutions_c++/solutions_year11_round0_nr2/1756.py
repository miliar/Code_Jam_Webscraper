#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<utility> 
#define inf 10000
using namespace std;

int main(){
    int T,C,D,N,i,j;
        freopen ("B-large.in","r",stdin);
       freopen ("BBL.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>C;
        vector < pair < int ,int > > p[300];
        vector < int > pp[300];
        char ct[5];
      //  cout<<C<<endl;
        for(i=0;i<C;i++){
            cin>>ct;
       //     cout<<ct<<" ";
            p[ct[0]].push_back(make_pair(ct[1],ct[2]));
            p[ct[1]].push_back(make_pair(ct[0],ct[2]));
        }
       // cout<<endl;
        cin>>D;
      //  cout<<D<<endl;
        char op[5];
        for(i=0;i<D;i++){
            cin>>op;
       //     cout<<op<<" ";
            pp[op[0]].push_back(op[1]);
            pp[op[1]].push_back(op[0]);
        }
       // cout<<endl;
        char gt[120];
        cin>>N;
        cin>>gt;
      //  cout<<N<<" "<<gt<<endl;
        string s;
        s="";
        for(i=0;i<N;i++){
            if(i==0){
                s+=gt[i];
            }
            else {
                int flag=0;
                s+=gt[i];
                for(j=0;s.size()>1&&j<p[s[s.size()-1]].size();j++){
                    if(s[s.size()-2]==p[s[s.size()-1]][j].first){
                        char ch= p[s[s.size()-1]][j].second ;
                        string ns="";
                        ns+=ch;
                        s.replace(s.size()-2,2,ns);
                        j=-1;
                    }
                }
                int loc=inf;
                for(j=0;s.size()>1&&j<pp[s[s.size()-1]].size();j++){
                    int locc=s.find(pp[s[s.size()-1]][j],0);
                    if(locc!=string::npos){
                        loc=min(locc,loc);
                    }
                }
                if(loc!=inf)s="";
            }
        }
        printf("Case #%d: [",cas);
        if(s.size()==0){cout<<"]"<<endl;continue;}
        for(i=0;i<s.size()-1;i++){
            cout<<s[i]<<", ";
        }
        cout<<s[s.size()-1]<<"]"<<endl;
    }
}
                    
