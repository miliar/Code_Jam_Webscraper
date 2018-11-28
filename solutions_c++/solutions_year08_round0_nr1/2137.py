#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;
map<string,int> sq;
vector<string> sn;
int main(){
    string sname;
    int n,loop,s,q,i,j;
    cin>>n;
    for(loop=1;loop<=n;loop++,sq.clear(),sn.clear()){
        cin>>s;getchar();
        sn.resize(s);
        for(i=0;i<s;i++){
            getline(cin,sn[i]);
            sq.insert(pair<string,int>(sn[i],0));
        }
        cin>>q;getchar();
        for(i=0,j=0;i<q;i++){
            getline(cin,sname);
            if(sq[sname]==j/s){
                if((j+1)%s) j++,sq[sname]++;
                else j+=2,sq[sname]+=2;
            }
        }
        cout<<"Case #"<<loop<<": "<<j/s<<endl;
    }
    return 0;  
} 
