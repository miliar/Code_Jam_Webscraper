#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    const int MAX = 2400;
    int N = 0;
    cin >> N;
    
    for (int i = 1; i <= N; i++)
    {
        int T, NA, NB;
        cin >> T >> NA >> NB;
        int A[MAX] = { 0 };
        int B[MAX] = { 0 };
        
        int d1, d2, a1, a2;
        for (int j = 0; j < NA + NB; j++)
        {
            scanf("%d:%d %d:%d\n", &d1, &d2, &a1, &a2);
            int dep = d1*100 + d2;
            int arr = a1*100 + a2;
            int* array;
            if (j < NA)
                array = A;
            else
                array = B;
            for (int k = dep; k < MAX; k++)
                array[k]++;
            if (array == A)
                array = B;
            else
                array = A;
            for (int k = arr + T; k < MAX; k++)
                array[k]--;
        }
        
        int trainsA = 0, trainsB = 0;
        for (int j = 0; j < MAX; j++)
        {
            trainsA = max(trainsA, A[j]);
            trainsB = max(trainsB, B[j]);
        }
        
        cout << "Case #" << i << ": " << trainsA << " " << trainsB << endl;
    }
    
    return 0;
}
