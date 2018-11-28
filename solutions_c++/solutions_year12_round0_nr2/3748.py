#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int T;

int solve(int n,int s,int p,vector<int> pt){
    int ans = 0;
    vector<int> v;
    for(int c=0;c<pt.size();c++){
        int a = pt[c];
        int b = a / 3;
        int d = b + (a > b * 3 ? 1 : 0);
        if(d >= p){
            ans++;
        }else{
            if(pt[c] != 0){
                v.push_back(pt[c]);
            }
        }
    }
    int sup = s;
    for(int c=0;c<v.size() && sup>0;c++){
        int a = v[c];
        int b = a / 3;
        int d = a % 3;
        //printf("%d:%d:%d\n",a,b,d);
        if(d == 2){
            int e = b + 2;
            if(e >= p){
                ans++;
                sup--;
            }
        }
        if(d == 0){
            int e = b + 1;
            if(e >= p){
                ans++;
                sup--;
            }
        }

    }
    return ans;
}

int main(){
    scanf("%d",&T);
    int n,s,p;
    for(int c=1;c<=T;c++){
        vector<int> pt;
        scanf("%d %d %d",&n,&s,&p);
        int temp;
        for(int i=0;i<n;i++){
            scanf("%d",&temp);
            pt.push_back(temp);
        }
        printf("Case #%d: %d\n",c,solve(n,s,p,pt));
    }
}
