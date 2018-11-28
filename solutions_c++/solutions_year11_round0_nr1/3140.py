/*
LANG: C++
TASK: bottrust
*/

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int T,N;
queue< pair<int,int> > o;
queue< pair<int,int> > b;
int dp[101][101];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int i=1; i<=T; i++){
        cin>>N;
        char a;
        int c;
        for(int j=1; j<=N; j++){
            cin>>a>>c;
            if(a=='O') o.push(make_pair(c,j));
            else b.push(make_pair(c,j));
        }
        int posb=1,poso=1;
        int time=0;
        while(!o.empty() || !b.empty()){
            if(o.empty()){
                time+=abs(posb-b.front().first)+1;
                posb=b.front().first;
                b.pop();
            }
            else if(b.empty()){
                time+=abs(poso-o.front().first)+1;
                poso=o.front().first;
                o.pop();
            }
            else{
                int bnextbutton=b.front().first,onextbutton=o.front().first;
                int bnextpos=b.front().second,onextpos=o.front().second;
                if(bnextpos<onextpos){
                    time+=abs(posb-bnextbutton)+1;
                    if(abs(posb-bnextbutton)+1>abs(poso-onextbutton)){
                        poso=onextbutton;
                    }
                    else{
                        if(poso>onextbutton) poso=poso-abs(posb-bnextbutton)-1;
                        else poso=poso+abs(posb-bnextbutton)+1;
                    }
                    posb=bnextbutton;
                    b.pop();
                }
                else{
                    time+=abs(poso-onextbutton)+1;
                    if(abs(poso-onextbutton)+1>abs(posb-bnextbutton)){
                        posb=bnextbutton;
                    }
                    else{
                        if(posb>bnextbutton) posb=posb-abs(poso-onextbutton)-1;
                        else posb=posb+abs(poso-onextbutton)+1;
                    }
                    poso=onextbutton;
                    o.pop();
                }
            }
        }
        cout<<"Case #"<<i<<": "<<time<<endl;
    }
	return 0;
}
