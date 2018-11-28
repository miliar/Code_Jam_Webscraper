#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(){
    int nc;
    cin>>nc;
    string s;
    for(int nt=0;nt<nc;nt++){
        int res=0;
        cin>>s;
        string sold=s;
        bool ok=next_permutation(s.begin(),s.end());
        //cout<<"s="<<s<<endl;
        //cout<<"sold="<<sold<<endl;
        if(!ok){
            sort(s.begin(),s.end());
            int ct=0;
            while(s[ct]=='0') ct++;
            for(int k=0;k<ct;k++){
                s.erase(s.begin());
            }
            for(int k=0;k<ct;k++){
                s.insert(s.begin()+1,'0');
            }
            s.insert(s.begin()+1,'0');
        }
        cout<<"Case #"<<nt+1<<": "<<s<<endl;
    }
}
