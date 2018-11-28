#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int n, k, nums[10], length, mini = 10000000;
char s[1005], otherS[1005];

int countGroups() {
    int count = 1;
    for(int i = 1; i < length; i++) {
        if(otherS[i] != otherS[i - 1])
            count++;
    }
    return count;
}


int main() {
    freopen("permrle.in", "r", stdin);
    freopen("permrle.out", "w", stdout);
    
    scanf("%d%*c", &n);
    
    for(int cases = 1; cases <= n; cases++) {
        mini = 10000000;
        scanf("%d%*c", &k);
        gets(s);
        length = strlen(s);
        for(int i = 0; i < k; i++)
            nums[i] = i;
        
        
        do {
            
            for(int i = 0; i < length / k; i++) {
                for(int j = 0; j < k; j++) {
                    otherS[i * k + j] = s[i * k + nums[j]];
                }
            }
            
            int count = countGroups();
            
            if(count < mini)
                mini = count;
            
        } while(next_permutation(nums, nums + k));
        
        printf("Case #%d: %d\n", cases, mini);
        
    }
    
}