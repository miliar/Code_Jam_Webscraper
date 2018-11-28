#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int ntest;
string c[50],r[50];
int n,k;
int res=0;
void check(int x, int y){
    //Row
    int i=1;
    while(x+i<n && r[x+i][y]==r[x+i-1][y]) i++;
    if(i>=k){
        if(r[x][y]=='B') res|=1;
        else res|=2;
    }
    i=1;
    while(y+i<n && r[x][y+i]==r[x][y+i-1]) i++;
    if(i>=k){
        if(r[x][y]=='B') res|=1;
        else res|=2;
    }
    i=1;
    while(x+i<n && y+i<n && r[x+i][y+i]==r[x+i-1][y+i-1]) i++;
    if(i>=k){
        if(r[x][y]=='B') res|=1;
        else res|=2;
    }
}
int main(){
    freopen("A-small.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int test=0; test<ntest; test++){
        printf("Case #%d: ",test+1);
        scanf("%d %d\n",&n,&k);
        for(int i=0; i<n;i++) c[i].clear(),r[i].clear();
        for(int i=0; i<n; i++)
            getline(cin,c[i]);                    
        //Gravity
        for(int i=0; i<n; i++)
            for(int j=n-1; j>-1;j--)
                if(c[i][j]=='.'){
                    int k=-2;
                    for(k=j-1; k>-1;k--)
                        if(c[i][k]!='.') break;
                        if(k>=0) swap(c[i][j],c[i][k]);
                }
        //Rotate
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                r[n-1-i]+= c[n-1-j][n-1-i];       
        //Check
        res=0;
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++){
                if(r[i][j]!='.')
                    check(i,j);
            }
        if(res==1)
            printf("Blue\n");
        else if(res==2)
            printf("Red\n");
        else if(res==3)    
            printf("Both\n");
        else
            printf("Neither\n");
    }
    return 0;
}
