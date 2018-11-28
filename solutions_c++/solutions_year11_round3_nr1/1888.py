#include<algorithm>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<deque>
#include<fstream>
#include<iostream>
#include<iterator>
#include<map>
#include<memory.h>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<string>
#include<utility>
#include<vector>
#pragma comment(linker, "/STACK:16777216")

#define FILE
using namespace std;

int main(){
    #ifdef FILE
    freopen("A-large.in", "rt", stdin);
    freopen("alarge.out","wt",stdout);
    #endif
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        int R,C;
        cin>>R;cin>>C;
        char tiles[R][C];
        for(int j=0;j<R;j++){
            for(int k=0;k<C;k++){
                cin>>tiles[j][k];
            }
        }
        bool possible=true;
        for(int j=0;j<R;j++){
            for(int k=0;k<C;k++){
                if(k!=C-1){
                    if(tiles[j][k]=='#'){
                        if(tiles[j][k+1]=='#'){
                            k++;
                        }else{
                            possible =false;
                            break;
                        }
                    }
                }else{
                    if(tiles[j][k]=='#'){
                        possible =false;break;
                    }
                }
            }
        }
        for(int k=0;k<C;k++){
            for(int j=0;j<R;j++){
                if(j!=R-1){
                    if(tiles[j][k]=='#'){
                        if(tiles[j+1][k]=='#') j++;
                        else{
                            possible =false;break;
                        }
                    }
                }else{
                    if(tiles[j][k]=='#'){
                        possible=false;break;
                    }
                }
            }
        }
        if(possible){
            int countR[R];
            int countC[C];
            for(int j=0;j<R;j++) countR[j]=0;
            for(int j=0;j<C;j++) countC[j]=0;
            for(int j=0;j<R;j++){
                for(int k=0;k<C;k++){
                    if(tiles[j][k]=='#'){
                        if((countR[j]%2==0)&&(countC[k]%2==0))tiles[j][k]='/';
                        else if((countR[j]%2==1)&&(countC[k]%2==0)) tiles[j][k]='\\';
                        else if((countR[j]%2==0)&&(countC[k]%2==1)) tiles[j][k]='\\';
                        else if((countR[j]%2==1)&&(countC[k]%2==1)) tiles[j][k]='/';
                        countR[j]++;countC[k]++;
                    }
                }
            }

            cout<<"Case #"<<i+1<<":"<<endl;
            for(int j=0;j<R;j++){
                for(int k=0;k<C;k++){
                    cout<<tiles[j][k];
                }
                cout<<endl;
            }
        }else{
            cout<<"Case #"<<i+1<<":"<<endl;cout<<"Impossible"<<endl;
        }
    }
    return 0;
}
