#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int T, N;
vector<string> s;

bool check(string & S, int x, bool type){
    if(type){
        for(int i=x+1;i<N;i++) if(S[i]=='1') return false;
    }
    else{
        for(int i=0;i<x;i++) if(S[i]=='1') return false;
    }
    return true;
}

int cost1(){
    vector<string> mat = s;
    string tmp;
    int cnt =0;
    for(int i=0;i<N;i++){
        int j;
        for(j=i;j<N;j++) if(check(mat[j], i, true)) break;
        if(j==N) return 9999;
        else{
            cnt += j-i;
            for(int k=j;k>i;k--) mat[k] = mat[k-1];
        }
    }
    return cnt;
}
int cost2(){
    vector<string> mat = s;
    string tmp;
    int cnt =0;
    for(int i=N-1;i>=0;i--){
        int j;
        for(j=i;j>=0;j--) if(check(mat[j], i, false)) break;
        if(j<0) return 9999;
        else{
            cnt += i-j;
            for(int k=j;k<i;k++) mat[k] = mat[k+1];
        }
    }
    return cnt;
}

int main(){
    scanf("%d", &T);
    for(int nCase=1;nCase<=T;nCase++){
        scanf("%d", &N);
        s = vector<string>(N);
        for(int i=0;i<N;i++)
            cin>>s[i];
        printf("Case #%d: ", nCase);
        cout<<min(cost1(), cost2())<<endl;
    
    
    }
    return 0;
}
