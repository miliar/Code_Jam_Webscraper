//
//  main.cpp
//  P3
//
//  Created by Witzy Huang on 12-4-28.
//  Copyright (c) 2012年 SinoSoft. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <vector>
#include <memory.h>
#include <climits>
#include <string.h>
using namespace std;
#define MAXN 500
int T;
int N;

int S[MAXN];
map<int, vector<int> > Status;
bool Used[MAXN];


ofstream fout("fout.txt");

bool dfs1(int sum, vector<int> ops, int index){
    if (sum==0) {
        for (int i=0; i<ops.size(); i++) {
            fout<<S[ops[i]]<<" ";
        }
        fout<<endl;
        
        for (int i=0; i<N; i++) {
            if (Used[i]) {
                fout<<S[i]<<" ";
            }
        }
        fout<<endl;
        return true;
    }
    if (index>=N) {
        return false;
    }
    
    if (!Used[index]) {
        int nsum=sum-S[index];
        if (nsum>=0) {
            ops.push_back(index);
            if(dfs1(nsum, ops, index+1)){
                ops.pop_back();
                return true;
            }
            ops.pop_back();
        }
    }

    
    if (dfs1(sum, ops, index+1)) {
        return true;
    }
    
    return false;
}



bool dfs(int index, int sum){
    
    if (index>=N) {
        return false;
    }
    if (sum>0 && dfs1(sum, vector<int>(), 0)) {
        return true;
    }
    
    Used[index]=true;
    if(dfs(index+1, sum+S[index])){
        Used[index]=false;
        return true;
    }
    Used[index]=false;
    
    
    if(dfs(index+1, sum)){
        return true;
    }
    
    return false;

    
}
void solve(){
    Status.clear();
    memset(Used, 0, sizeof(Used));
    if (dfs(0, 0)) {
        
    }else{
        fout<<"Impossible\n";
    }
    
    
}

int main (int argc, const char * argv[])
{
    
    ifstream fin("C-small-attempt0.in");
    
    fin>>T;
    for (int caseIndex=1; caseIndex<=T; caseIndex++) {
        fin>>N;
        for (int i=0; i<N; i++) {
            fin>>S[i];
        }
        fout<<"Case #"<<caseIndex<<":"<<endl;
        solve();
        
    }
    return 0;
}

