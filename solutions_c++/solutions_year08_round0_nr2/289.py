#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int s2i(string s){
    s[s.find(':')]=' ';
    istringstream iss(s);
    int h,m;
    iss>>h>>m;
    return h*60+m;
}

int main(){
    int n;
    cin>>n;
    for (int cn=0;cn<n;++cn){
        int ttime,na,nb;
        cin>>ttime>>na>>nb;
        vector<vector<int> > trains(1440,vector<int>(2,0));
        string a,z;
        int ta,tz;
        for (int i=0;i<na;++i){
            cin>>a>>z;
            ta=s2i(a);
            tz=s2i(z)+ttime;
            trains[ta][0]--;
            if (tz<1440) trains[tz][1]++;
        }
        for (int i=0;i<nb;++i){
            cin>>a>>z;
            ta=s2i(a);
            tz=s2i(z)+ttime;
            trains[ta][1]--;
            if (tz<1440) trains[tz][0]++;
        }
        vector<int> ans(2,0),cur(2,0);
        for (int t=0;t<1440;++t){
            for (int i=0;i<2;++i){
                cur[i]+=trains[t][i];
                if (cur[i]<0){
                    ans[i]-=cur[i];
                    cur[i]=0;
                }
            }
        }
        cout<<"Case #"<<cn+1<<": "<<ans[0]<<' '<<ans[1]<<endl;
    }
}
            
            
            
            
