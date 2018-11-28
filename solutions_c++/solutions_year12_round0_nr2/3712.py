/*
ID: zjshenn1
PROG:
LANG: C++
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int score[110];
int ans1,ans2;
int main(){
    #if 0
    freopen("in.txt","r",stdin);
    #else
    freopen("B-large.in","r",stdin);
    freopen("out2.out","w",stdout);
    #endif
    int T,ca=0;
    cin>>T;
    while(T--){
        ans1=0;ans2=0;
        memset(score,0,sizeof(score));
        int n,s,p;
        cin>>n>>s>>p;
        for(int i=0;i<n;i++){
            cin>>score[i];
        }
        //sort(score,score+n);
        for(int i=0;i<n;i++){
            if(score[i]>=3*p||score[i]>=3*p-2&&p-1>=0){
                ans1++;
            }else if(score[i]>=3*p-4&&p-2>=0){
                ans2++;
            }
        }
        int ans=ans1+min(ans2,s);
        cout<<"Case #"<<++ca<<": "<<ans<<endl;
    }
    return 0;
}
