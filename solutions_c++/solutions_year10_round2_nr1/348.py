#include <cstdio>
#include <map>
#include <string>
#include <cstring>

using namespace std;
char list[202][102], tem[102]="/";
int n, m;

int main(){
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int nca;
    scanf("%d", &nca);
    for(int ii=1;ii<=nca;ii++){
        int ans=0, len, x;
        map<string,int>mp;
        scanf("%d%d", &n, &m);
        for(int i=0;i<n;i++){
            scanf("%s", list[i]);
            len = strlen(list[i])+1;
            list[i][len-1]='/';
            x=1;
            for(int j=1;j<len;j++){
                if(list[i][j]=='/'){
                    for(int k=x;k<j;k++){
                        tem[k]=list[i][k];
                    }
                    x=j;
                    tem[j]='\0';
                    mp[tem]=1;
                }
            }
        }
        m=m+n;
        for(int i=n;i<m;i++){
            scanf("%s", list[i]);
            len = strlen(list[i])+1;
            list[i][len-1]='/';
            x=1;
            for(int j=1;j<len;j++){
                if(list[i][j]=='/'){
                    for(int k=x;k<j;k++){
                        tem[k]=list[i][k];
                    }
                    tem[j]='\0';
                    if(mp.find(tem)==mp.end()){
                        mp[tem]=1;
                        //printf("tem: %s\n", tem);
                        ans++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", ii, mp.size()-n);
    }
    return 0;
}