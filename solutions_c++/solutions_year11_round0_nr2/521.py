/*
 * Author: fatboy_cw
 * Created Time:  2011/5/7 10:31:11
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())

int test,ca,c,d,n;
char comb['Z'+1]['Z'+1];
bool opp['Z'+1]['Z'+1];
string str;
vector<char> ans;

bool combine(){
    bool flag=false;
    while(ans.size()>=2){
        char c1=ans[ans.size()-1];
        char c2=ans[ans.size()-2];
        if(comb[c1][c2]!='$'){
            ans.pop_back();
            ans.pop_back();
            ans.push_back(comb[c1][c2]);
            flag=true;
        }
        else{
            break;
        }
    }
    return flag;
}       

int main() {
    freopen("B.out","w",stdout);
    std::ios::sync_with_stdio(false);
    cin>>test;
    while(test--){
        cin>>c;
        for(int i='A';i<='Z';i++){
            for(int j='A';j<='Z';j++){
                comb[i][j]='$';
                opp[i][j]=false;
            }
        }
        for(int i=0;i<c;i++){
            string t;
            cin>>t;
            comb[t[0]][t[1]]=t[2];
            swap(t[0],t[1]);
            comb[t[0]][t[1]]=t[2];
        }
        cin>>d;
        for(int i=0;i<d;i++){
            string t;
            cin>>t;
            opp[t[0]][t[1]]=true;
            swap(t[0],t[1]);
            opp[t[0]][t[1]]=true;
        }
        ans.clear();
        cin>>n;
        cin>>str;
        for(int i=0;i<n;i++){
            ans.push_back(str[i]);
            if(!combine()){
                for(int j=0;j<ans.size()-1;j++){
                    if(opp[ans[j]][ans.back()]){
                        ans.clear();
                        break;
                    }
                }
            }
        }
        //for(int i=0;i<ans.size();i++){
            //cout<<ans[i]<<" ";
        //}
        //cout<<endl;
        printf("Case #%d: ",++ca);
        printf("[");
        for(int i=0;i<(int)ans.size()-1;i++){
            printf("%c, ",ans[i]);
        }
        if(ans.size())  printf("%c",ans.back());
        printf("]\n");
    }           
    return 0;
}

