#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>


#define pb(n,v) n.push_back(v)
#define all(n) n.begin(),n.end()




using namespace std;

int main(){
    int T;
    cin>>T;
    int cc=0;
    while(T--){
        cc++;
        

        string pat[51];
        int R,C;
        cin>>R>>C;

        bool bp=false;
        for(int i=0;i<R;i++){
            string s;
            cin>>s;
            pat[i]=s;
            if(count(all(pat[i]),'#') > 0){
                bp=true;
            }
        }

        cout<<"Case #"<<cc<<":"<<endl;
        if(bp && (R==1 || C==1)){
            cout<<"Impossible"<<endl;
            continue;
        }

        bool solved = true;

        if(R>=2 && C>=2){


            for(int i=0;i<=R-2;i++){
                for(int j=0;j<=C-2;j++){
                    char tl,tr,bl,br;
                    tl = pat[i][j];
                    tr = pat[i][j+1];
                    bl = pat[i+1][j];
                    br = pat[i+1][j+1];

                    if(tl=='#' && tr=='#' && bl=='#' && br=='#'){
                        pat[i][j]='/';
                        pat[i][j+1]='\\';
                        pat[i+1][j]='\\';
                        pat[i+1][j+1]='/';

                    }
                }
            }


            for(int i=0;i<R;i++){
                if(count(all(pat[i]),'#') != 0){
                    cout<<"Impossible"<<endl;
                    solved = false;
                    break;
                }
            }
        }
        if(solved){
            for(int i=0;i<R;i++){
                cout<<pat[i]<<endl;
            }
        }

    }
    return 0;
}