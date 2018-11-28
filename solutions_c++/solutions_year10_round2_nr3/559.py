#include <cstdio>
#include <iostream>
#include <vector>

#define modulo 100003

using namespace std;

vector<int> a;
int t,n;
int an[100];

int find(int num){
    for(int i=0;i<a.size();i++)
        if(a[i]==num)
            return i;
    return 0;
}

int test2(){
    int pos=n;
    while(pos>1){
        if (pos==find(pos))
            return 0;
        pos=find(pos);
    }
    return pos;
}

int main(){
//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attemot2.out","w",stdout);
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
        scanf("%d",&n);
        if(an[n]){
            printf("Case #%d: %d\n",test,an[n]);
            cerr << test<<" ";
            continue;
        }
        int ans=0;
        for(int mask=0;mask<(1<<(n-2));mask++){
            a.clear();
            a.push_back(0);
            for(int j=0;j<(n-2);j++)
                if(mask & (1<<j))
                    a.push_back(j+2);
            a.push_back(n);
//            for(int j=0;j<a.size();j++)
//                  cerr << a[j]<<" ";
//            cerr << test2();
//            cerr << "\n";
            ans+=test2();
        }
        printf("Case #%d: %d\n",test,ans%modulo);
        an[n]=ans%modulo;
        cerr << test<<" ";
    }
}
