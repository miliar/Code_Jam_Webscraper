#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;
namespace
{
    enum ElementState{
        UNDEF,
        TO_BE_SORT,
        ALREADY_FIXED,
        ALREADY_GROUPED
    };
}

int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N;
        cin >> N;
        vector<int> v(N);
        vector<ElementState> state(N);
        for(int j=0; j<N; j++){
            cin >> v[j];
            if(v[j]==j+1){
                state[j]=ALREADY_FIXED;
            }else{
                state[j]=TO_BE_SORT;
            }
        }
        vector<int> groups;
        for(int j=0; j<N; j++){
            if(state[j]==TO_BE_SORT){
                int n=0;
                int p=j;
                do{
                    state[p]=ALREADY_GROUPED;
                    p=v[p]-1;
                    n++;
                }while(p!=j);
                groups.push_back(n);
            }
        }
        vector<int>::iterator it;
        int ratio=0;
        for(it=groups.begin(); it!=groups.end(); it++){
            ratio+=(*it);
        }
        printf("Case #%d: %.6f\n", (i+1), (double)ratio);
    }
    return 0;
}
