/* 
 * File:   main.cpp
 * Author: lolo
 *
 * Created on May 8, 2010, 8:21 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

#define MAX 1010

int T;
int N,R,k;
int group[ MAX ];
int sum[MAX];
vector< long long > sumList;

int main(int argc, char** argv) {
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;

    for (int t = 0; t < T; t++){
        cin>>R>>k>>N;
        sumList.clear();
        
        for (int i = 0; i < N; i++)
            cin>>group[i];
        memset(sum,-1,sizeof(sum));
        int i = 0;
        long long prev = 0;
        while (sum[i] == -1){
            long long s = 0;
            int j;
            for (j = i; s + group[j] <= k;){
                s += (long long)group[j];
                j = (j+1)%N;
                if (j == i) break;
            }
            //cout<<s<<" "<<j<<endl;
            sum[i] = sumList.size();
            prev += s;
            sumList.push_back(prev);            
            i = j;
        }        
        long long res = 0;
        if (R <= sumList.size()) res = sumList[R-1];
        else{            
            long long minus = sum[i] > 0 ? minus = sumList[sum[i]-1] : 0;
            long long oneSeg = *(sumList.end()-1) - minus;            
            R -= sum[i];
            res += minus;            
            res += (long long)R/(sumList.size() - sum[i]) * oneSeg;            
            long long add = sum[i]-1;
            add += R % (sumList.size() - sum[i]);
            if (add < 0) add = 0;
            else add = sumList[add];
            res += add - minus;
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return (EXIT_SUCCESS);
}

