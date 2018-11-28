/*
ID: ivailok1
TASK: magicka
LANG: C++
*/

#include <iostream>
#include <set>
#include <queue>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string.h>

using namespace std;

#define h 1a

int T,C,D,N;
int opp[28][28];
int comb[28][28];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    for(int i=1; i<=T; i++){
        cin>>C;
        string temp;
        memset(comb,0,sizeof(comb));
        memset(opp,0,sizeof(opp));
        for(int j=1; j<=C; j++){
            cin>>temp;
            comb[temp[0]-'A'+1][temp[1]-'A'+1]=temp[2]-'A'+1;
            comb[temp[1]-'A'+1][temp[0]-'A'+1]=temp[2]-'A'+1;
        }
        cin>>D;
        for(int j=1; j<=D; j++){
            cin>>temp;
            opp[temp[0]-'A'+1][temp[1]-'A'+1]=1;
            opp[temp[1]-'A'+1][temp[0]-'A'+1]=1;
        }
        cin>>N;
        temp="";
        char a;
        for(int j=1; j<=N; j++){
            cin>>a;
            if(temp.size()==0){
                temp+=a;
                continue;
            }
            char last=temp[temp.size()-1];
            if(comb[last-'A'+1][a-'A'+1]!=0){
                temp.erase(temp.size()-1,1);
                temp+=(char)(comb[last-'A'+1][a-'A'+1]+'A'-1);
                continue;
            }
            int flag=0;
            for(int k=0; k<temp.size(); k++){
                if(opp[temp[k]-'A'+1][a-'A'+1]==1){
                    temp="";
                    flag=1;
                    break;
                }
            }
            if(flag) continue;
            temp+=a;
        }
        if(temp.size()){
            cout<<"Case #"<<i<<": ["<<temp[0];
            for(int j=1; j<temp.size(); j++){
                cout<<", "<<temp[j];
            }
            cout<<"]"<<endl;
        }
        else cout<<"Case #"<<i<<": []"<<endl;
    }
    return 0;
}
