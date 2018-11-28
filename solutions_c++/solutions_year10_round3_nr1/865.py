#include <vector>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
    int T, c=1;

    scanf("%d", &T);

    while(c <= T) {
        int N, number=0;
        vector<int> A, B;
        scanf("%d", &N);

        while(N > 0) {
            int a,b;
            scanf("%d %d", &a, &b);
            A.push_back(a); B.push_back(b);
            N -= 1;
        }

        for(int i=0;i<A.size(); ++i) {
            for(int j=0;j<A.size(); ++j) {
                if((A[i] < A[j]) && (B[i] > B[j])) number +=1;
            }
        }

        printf("Case #%d: %d\n", c, number);

        c+=1;
    }
    return 0;
}
