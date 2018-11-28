#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

int n,m,len;
string a,base,now;
int com[300][300],opp[300][300];
int t,tt;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> t;
    while( t -- ){

        memset(com,0,sizeof(com));
        memset(opp,0,sizeof(opp));
        cin >> n;
        for(int i=1;i<=n;i++){
            cin >> a;
            com[a[0]][a[1]] = com[a[1]][a[0]] = (int)a[2];
        }
        cin >> m;
        for(int i=1;i<=m;i++){
            cin >> a;
            opp[a[0]][a[1]] = opp[a[1]][a[0]] = 1;
        }
        cin >> len;
        cin >> base;
        now.clear();
        for(int i=0;i<len;i++){
            if(now.size() == 0)
                now.push_back(base[i]);
            else if(com[now[now.size() - 1]][base[i]] != 0)
                now[now.size() - 1] = (char)com[now[now.size() - 1]][base[i]];
            else{
                int found = 0;
                for(int j=now.size()-1;j>=0;j--)
                    if(opp[now[j]][base[i]] != 0){
                        found = 1;
                        now.clear();
                        if(j > 0)
                            now = now.substr(0,j);
                        break;
                    }
                if(found == 0)
                    now.push_back(base[i]);
            }
        }
        printf("Case #%d: [",++tt);
        for(int i=0;i<now.size();i++){
            printf("%c",now[i]);
            if(i != now.size() - 1)
                printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
