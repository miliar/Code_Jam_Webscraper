#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    int N;
    scanf("%d", &N);
    for(int n = 1; n <= N; n++){
       int P, K, L;
       vector<int> freq;
       scanf("%d%d%d", &P, &K, &L);
       for(int i = 0; i < L; i++){
               int a; 
               scanf("%d", &a);
               freq.push_back(a);        
       }     
       sort(freq.begin(), freq.end());
       int wyn = 0;
       for(int i = 0; i < freq.size(); i++){
               wyn += freq[i] * (int)((L - i)/K + ((L - i) % K?1:0));
          //     printf("%d\n", (int)((L - i)/K + ((L - i) % K?1:0)));        
       }
       printf("Case #%d: %d\n", n, wyn);
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
