#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;

int A,B,counter;
int p10[10]={1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};

int f(int x)
{
    int ret=0;
    int d=0;
    int y=x;
    set<int> myset;
    while(y){
        y/=10;
        d++;
    }
    y=p10[d];
    y/=10;
    int z=10,r,s;
    while(y>=10){
        r=x%z;
        s=x/z;
        int curr=r*y+s;
        if(curr>x && curr<=B){
            myset.insert(curr);
        }
        z *= 10;
        y /= 10;
    }
    return myset.size();
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    for(int tt=1;tt<=cases;tt++){
        scanf("%d%d",&A,&B);
        counter=0;
        for(int i=A;i<B;i++){
            counter += f(i);
        }
        printf("Case #%d: %d\n",tt,counter);
    }
    return 0;
}
