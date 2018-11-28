#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
        
        int r,c;
        cin>>r>>c;
        vector<string> v;
        for(int i=0;i<r;i++){
            string temp;
            cin>>temp;
            v.push_back(temp);
        }
        bool flag=true;
        for(int i=0;i<v.size();i++){
            for(int j=0;j<v[i].size();j++){
                if(v[i][j]=='#'){
                    v[i][j]='/';
                    if(j==v[i].size()-1){
                        flag=false;
                    } else {
                        if(v[i][j+1]=='#'){
                            v[i][j+1]='\\';
                        } else {
                            flag=false;
                        }
                    }
                    if(i==v.size()-1){
                        flag=false;
                    } else {
                        if(v[i+1][j]=='#'){
                            v[i+1][j]='\\';
                        } else {
                            flag=false;
                        }
                        if(v[i+1][j+1]=='#'){
                            v[i+1][j+1]='/';
                        } else {
                            flag=false;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<ii+1<<":"<<endl;
        if(flag){
            for(int i=0;i<v.size();i++){
                for(int j=0;j<v[i].size();j++){
                    cout<<v[i][j];
                }
                cout<<endl;
            }
        } else {
            cout<<"Impossible"<<endl;
        }
    }
}