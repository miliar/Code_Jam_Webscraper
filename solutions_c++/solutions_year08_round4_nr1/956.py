#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<string>
#include<set>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    int m,n,g,c,v;
    for(int cs=1;cs<=t;cs++){
        scanf("%d%d",&m,&v);
        vector<int> vi(m+1);
        vector<int> vg(m+1);
        vector<int> vc(m+1);

        int change=0;
        vector<int> vchange;
        
        for(int i=0;i<(m-1)/2;i++){
            scanf("%d%d",&g,&c);
            vg[i+1]=g;
            vc[i+1]=c;
            if(c){change++;vchange.push_back(i+1);}

        }
        for(int i=(m-1)/2;i<m;i++){
            scanf("%d",&n);
            vi[i+1]=n;
        }

        int interior = (m-1)/2;
        for(int i=interior;i>0;i--){
            if(vg[i]==1){
                vi[i]=vi[2*i]&vi[2*i+1];
            }
            else {
                vi[i]=vi[2*i]|vi[2*i+1];
            }
        }

        int min=m+1;
        int nc=1<<change;

        for(int x=0;x<nc;x++){
            int ccnt=0;
            int temp=x;
            vector<int> changed=vg;
            for(int j=0;j<change;j++){
                if(temp%2){
                    changed[vchange[j]]=1-changed[vchange[j]];
                    ccnt++;
                }
                temp/=2;
            }
            for(int i=interior;i>0;i--){
                if(changed[i]==1){
                    vi[i]=vi[2*i]&vi[2*i+1];
                }
                else {
                    vi[i]=vi[2*i]|vi[2*i+1];
                }
            }
            if(min>ccnt && v==vi[1])
                min=ccnt;
        }
        if(min==m+1){
            printf("Case #%d: IMPOSSIBLE\n",cs);
        }
        else printf("Case #%d: %d\n",cs,min);
    }
    return 0;
}
