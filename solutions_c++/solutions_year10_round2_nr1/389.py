#include <iostream>
#include <set>
#include <vector>
#include <sstream>

using namespace std;

int T,M,N;

int main(){
    cin>>T;
    for(int TT=1;TT<=T;++TT){
        cin>>N>>M;
        set<string> mem;
        string s;

        for(int i=0;i<N;i++){
            cin>>s;
            for(int j=0;j<s.size();j++) if (s[j]=='/') s[j]=' ';
            stringstream ss(s);
            string a,b;

            int x=0;
            while(ss>>b){
                a+='/';
                a+=b;
                mem.insert(a);
            }
        }

        long long poc=0;
        for(int i=0;i<M;i++){
            cin>>s;
            for(int j=0;j<s.size();j++) if (s[j]=='/') s[j]=' ';
            stringstream ss(s);
//cout<<s<<" fsdfsdfsdfdsfsdfdsfsd"<<endl;
            string a,b;

            while(ss>>b){
                a+='/';
                a+=b;
                if(mem.find(a)==mem.end()){
                    mem.insert(a);
                    ++poc;
                    //cout<<"add "<<a<<endl;
                }
            }
        }
        cout<<"Case #"<<TT<<": "<<poc<<endl;
    }
    return 0;
}
