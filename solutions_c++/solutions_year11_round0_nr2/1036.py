//kbriut@yahoo.com
//GNU:Ming@Code:Blocks
#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
int n,t,mn,sum,xsum,txt,C,D,N;
int F[300][300];
string seq;
vector<char>ans;
vector<int>E[300];
string cc,cd;
bool Merge(char ch){
    if(ans.size()==0)return false;
    char c=ans[ans.size()-1];
    if(F[ch][c]!=0)return true;
    else return false;
}
bool Erase(char ch){
    if(ans.size()==0)return false;
    int lim=ans.size();
    for(int j=0;j<E[ch].size();j++){
        for(int i=0;i<lim;i++)if(ans[i]==E[ch][j])return true;
    }
    return false;
}
int main(){
    //freopen("1.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    while(t--){
        memset(F,0,sizeof F);
        //memset(E,0,sizeof E);
        for(i=0;i<300;i++)E[i].clear();
        ans.clear();
        scanf("%d",&C);
        while(C--){
            cin>>cc;
            char cha=cc[0];
            char chb=cc[1];
            char chc=cc[2];
            F[cha][chb]=F[chb][cha]=chc;
        }
        scanf("%d",&D);
        while(D--){
            cin>>cd;
            char cha=cd[0];
            char chb=cd[1];
            E[cha].push_back(chb);
            E[chb].push_back(cha);
        }
        cin>>N>>seq;
        for(i=0;i<N;i++){
            char ch=seq[i];
            if(Merge(ch)){
                char tem=ans[ans.size()-1];
                ans[ans.size()-1]=F[ch][tem];
            }
            else if(Erase(ch)){
                ans.clear();
            }
            else ans.push_back(ch);
        }
        printf("Case #%d: [",++txt);
        for(i=0;i<ans.size();i++){
            if(i)printf(", ");
            printf("%c",ans[i]);
        }
        printf("]\n");
    }
    return 0;
}
