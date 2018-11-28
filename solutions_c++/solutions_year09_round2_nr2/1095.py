#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;





void solve(string s)
{
    string sorted = s;
    vector<string> results;
    sort(results.begin(),results.end());
    for(int i=0;i<s.size();i++) {
        int smallest=-1;
        for(int j=i+1;j<s.size();j++) {
            if(s[j]>s[i]) {
                //smallest=min(smallest
                if(smallest==-1)smallest=j;
                else
                if(s[smallest]>s[j]) {
                    smallest=j;
                }
            }
        }
        //cout<<i<<" "<<smallest<<endl;
        if(smallest!=-1) {
            string ret="";
            for(int j=0;j<i;j++) {
                ret+=s[j];
            }
            ret+=s[smallest];
            string str="";
            for(int j=i;j<s.size();j++) {
                if(j==smallest) continue;
                str+=s[j];
            }
            sort(str.begin(),str.end());
            ret+=str;

            results.push_back(ret);

        }
    }
    sort(results.begin(),results.end());
    if(results.size()==0){
        cout<<-1<<endl;
        return;
    }

    cout<<results[0]<<endl;


}

int largest(string s)
{
    string temp=s;
    sort(s.begin(),s.end(),greater<char>());
    if(temp==s) return 1;
    return 0;

}



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    string s;
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        cin>>s;
        cout<<"Case #"<<t<<": ";
        /*hanle largets*/
        if(largest(s)) {
            string zeros="",nzeros="";
            for(int i=0;i<s.size();i++) {
                if(s[i]=='0') zeros+=s[i];
                else nzeros+=s[i];
            }
            sort(nzeros.begin(),nzeros.end());
            for(int i=0;i<nzeros.size();i++) {
                cout<<nzeros[i];
                if(i==0) {
                    for(int j=0;j<zeros.size();j++) cout<<0;
                    cout<<0;
                }


            }
            cout<<endl;
        }
        else solve(s);


    }
    return 0;
}
