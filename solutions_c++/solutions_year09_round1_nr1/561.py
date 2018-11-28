#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<iomanip>
#include<set>
using namespace std;
int T;
int size;
int base[11];
set<int> has;
int min_happy(){
    for(int i=2;;i++){
//        cout<<i<<endl;
        bool is_min=true;
        for(int j=0;j<size;j++){
            has.clear();
            int k=i;
            int tp=i;
            while(has.find(tp)==has.end()){
//                cout<<"tp=="<<tp<<" k="<<k<<endl;
                has.insert(tp);
                k=tp;
                tp=0;
                while(k>0){
                    tp+=(k%base[j])*(k%base[j]);
                    k=k/base[j];
                }
                if(tp==1) break;
            }
            if(tp!=1) is_min=false;
            else continue;
        }
        if(is_min==true) return i;
    }
}

int main()
{
    ifstream in("A-small-attempt0.in");
    string tmp;
    istringstream ins;
    int ans=0;
    in>>T;
    getline(in, tmp);
    
    for(int i=1;i<=T;i++){
        getline(in, tmp);
        memset(base,0,sizeof(base));
        ins.clear();
        ins.str(tmp);
        int j=0;
        while(ins>>base[j++]);
        size=j-1;
/*      
        for(int k=0;k<size;k++)
            cout<<base[k]<<" ";
        cout<<endl;
*/       
        ans=min_happy();
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    
    in.close();
    return 0;
}
