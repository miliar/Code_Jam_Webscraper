#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<iostream>
#include<string.h>
using namespace std;
int play[1010];
void solve(int test){
    int n;
    scanf("%d",&n);
    vector<pair<int,int> > v;
    for(int i=0;i<n;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        v.push_back(make_pair(b,a));
    }
    memset(play,0,sizeof(play));
    sort(v.rbegin(),v.rend());
    int now=0;
    int time=0;
    printf("Case #%d: ",test);
    while(now!=n*2){
        bool isPlay=0;
        int play1=-1,play2=-1;
        for(int i=0;i<n;i++){
            if(now>=v[i].first&&play[i]!=2&&play2==-1){
                play2=i;
            }
            if(now>=v[i].second&&play[i]==0&&play1==-1){
                play1=i;
            }
        }
        if(play1==-1&&play2==-1){
            printf("Too Bad\n");
            return;
        }
        if(play2!=-1){
            now+=2-play[play2];
            time++;
            play[play2]=2;
        }
        else if(play1!=-1){
            now++;
            time++;
            play[play1]=1;
        }
    }
    printf("%d\n",time);
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)solve(i);
}
