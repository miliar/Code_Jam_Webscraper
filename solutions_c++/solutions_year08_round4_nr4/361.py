#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;

int T, k;
string s;

int main() {
    scanf("%d",&T);
    for(int z=0;z<T;z++) {
        int best = 100000;        
        scanf("%d",&k);
        cin>>s;
        string os = s;
        vector<int> v;
        for(int i=0;i<k;i++) v.push_back(i);
        do {
            s = os;
            for(int i=0;i<s.size()/k;i++) {
                for(int j=0;j<k;j++) s[i*k+j] = os[i*k+v[j]];
            }
            int tmp = 1;
            for(int i=1;i<s.size();i++) if(s[i] != s[i-1]) tmp++;
            best = min(best,tmp);            
        }while(next_permutation(v.begin(),v.end()));
        
        printf("Case #%d: %d\n",z+1,best);
    }
    return 0;
}
              
        
