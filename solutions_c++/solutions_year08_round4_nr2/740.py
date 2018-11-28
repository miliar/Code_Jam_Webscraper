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
    for(int cs=0;cs<t;cs++){
        int n,m,a;
        vector<int>ans;
        scanf("%d%d%d",&n,&m,&a);
        int flag=0;
        if(n*m>=a){
            for(int i=0;i<=n;i++){
                for(int j=0;j<=n;j++){
                    for(int k=0;k<=n;k++){
                        for(int l=0;l<=m;l++){
                            for(int o=0;o<=m;o++){
                                for(int p=0;p<=m;p++){
                                    int area=i*o-j*l+j*p-k*o+k*l-i*p;
                                    if(area<0)area*=-1;
                                    if(area==a){flag=1;
                                        ans.push_back(i);
                                        ans.push_back(l);
                                        ans.push_back(j);
                                        ans.push_back(o);
                                        ans.push_back(k);
                                        ans.push_back(p);
                                        break;}
                                }
                                if(flag)break;
                            }
                            if(flag)break;
                        }
                        if(flag)break;
                    }
                    if(flag)break;
                }
                if(flag)break;
            }
        }
        if(!flag)printf("Case #%d: IMPOSSIBLE\n",cs+1);
        else{
            printf("Case #%d: %d %d %d %d %d %d\n",cs+1,ans[0],ans[1],ans[2],ans[3],ans[4],ans[5]);
        }
    }
    return 0;
}
