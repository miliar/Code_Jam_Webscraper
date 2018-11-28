#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    int T;
   // ifstream cin("in.txt");
    ifstream cin("B-small-attempt9.in");
    ofstream cout("B-small-attempt9.out");
    cin>>T;
    for(int i=1;i<=T;++i){
        int c,d,n;
        string cs,ds,ns;
        cin>>c;
        for(int j=0;j<c;++j)
        cin>>cs;
        cin>>d;
        for(int j=0;j<d;++j)
        cin>>ds;
        cin>>n>>ns;
       /* if(ds.size()!=0){
            if(ds[0]==ns[n-1]&&ds[1]==ns[n-2]||ds[0]==ns[n-2]&&ds[1]==ns[n-1]){
                cout<<"Case #"<<i<<": "<<"[]"<<endl;
                continue;
            }
        }*/
        int len=0;
        string abc;
        if(cs.size()!=0)
        abc.push_back(cs[2]);
        int jj;
        for(int j=1;j<n;++j){
            jj=j;
            jj-=len;
           // cout<<jj<<endl;
                if(cs.size()!=0&&jj>=1&&(cs[0]==ns[jj]&&cs[1]==ns[jj-1]||cs[0]==ns[jj-1]&&cs[1]==ns[jj])){
                    ns.replace(jj-1,2,abc);
                    len+=1;
                    continue;
                }
                for(int k=0;k<=jj-1;++k){
                    if(ds.size()!=0&&ds[0]==ns[jj]&&ds[1]==ns[k]||ds[0]==ns[k]&&ds[1]==ns[jj]){
                        //cout<<jj<<" "<<k<<" "<<ns[jj]<<ns[k]<<endl;
                        ns.erase(0,jj+1);
                        len+=jj;
                       // cout<<len<<endl;
                        break;
                    }
                }
            }
            cout<<"Case #"<<i<<": [";
            if(ns.size()==0)
            cout<<"]"<<endl;
            else{
                for(int j=0;j<ns.size()-1;++j){
                    cout<<ns[j]<<", ";
                }
                cout<<ns[ns.size()-1]<<"]"<<endl;
            }
    }
    return 0;
}
