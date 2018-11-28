#include <cstdio>
#include <algorithm>
using namespace std;

int main() {

    int T; scanf("%d", &T);
    for (int t=0; t<T; t++) {
        int N; scanf("%d", &N);
        
        int X[100];
        for (int i=0; i<N; i++) {
            char s[120]; scanf("%s", s);
            X[i]=-1;
            for (int j=0; j<N; j++)
                if (s[j]=='1') X[i]=j;
        }
                
/*        for (int i=0; i<N; i++) printf("%d ", X[i]);
        printf("\n");*/
        
        int result = 0;
        for (int fix=0; fix<N; fix++) {
            
            int k=fix;
            while (X[k]>fix) k++;
            for (int i=k-1; i>=fix; i--)
                swap(X[i], X[i+1]), result++;
        
/*            for (int i=0; i<N; i++) printf("%d ", X[i]);
            printf("\n");*/
        }
        
        printf("Case #%d: %d\n", t+1, result);
    }
    

    return 0;
}
