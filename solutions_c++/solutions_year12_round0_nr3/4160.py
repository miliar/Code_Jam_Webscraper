#include <iostream>
#include <vector>

using namespace std;

bool comp(int a,int b){
    vector <int> x,y;
    x.resize(0);y.resize(0);
    if(a >= b) return false;
    while(a != 0){
        x.push_back(a%10);
        a /= 10;
        } 
    while(b != 0){
        y.push_back(b%10);
        b /= 10;
        }
    if(x.size() != y.size()) return false;
    for(int i=0;i<y.size();i++){
        bool flag = true;
        for(int j=0;j<y.size();j++)
            if(x[j] != y[(j+i)%y.size()]) flag = false;
        if(flag) return true;
        }
    return false;
    }

int main(){
    freopen("C-small-0.in","r",stdin);
    freopen("C-small-0.out","w",stdout);
    int t, a, b, ans;
    scanf("%d\n", &t);
    for(int k=0;k<t;k++){
        ans = 0;
        scanf("%d %d\n", &a, &b);
        for(int i=a;i<=b;i++)
            for(int j=a;j<=b;j++)
                if(comp(i,j)) ans++;
        printf("Case #%d: %d\n", k+1, ans);
        }
    return 0;
    }
