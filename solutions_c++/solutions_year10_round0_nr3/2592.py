#include <iostream>
#include <deque>


using namespace std;

FILE *f = fopen("park.in", "r");
FILE *g = fopen("park.out", "w");

int T, R, K, N;
int afisare(deque <int> a)
{
    for (int i = 0; i < a.size(); ++i)
        cout << a[i] << " ";
    cout << "\n";
    
    return 0;
}

int main()
{
    
    fscanf(f, "%d", &T);
    for (int k = 0; k < T; ++k)
    {
        deque<int> mydeque;
        long long total = 0;
        fscanf(f, "%d %d %d", &R, &K, &N);
        for (int i = 0; i < N; ++i)
        {
            int x;
            fscanf(f, "%d", &x);
            mydeque.push_back(x);
        }
        //afisare(mydeque);
        for (int j = 0; j < R; ++j)
        {
            int sum = 0, groups = 0;
            while (((sum + mydeque.front()) <= K) && (groups < N))
            {
                groups++;
                sum += mydeque.front();
                mydeque.push_back(mydeque.front());
                mydeque.pop_front();
            }
            //cout << sum << " ";
            //afisare(mydeque);
            total += sum;
            
        }
        mydeque.clear();
        fprintf(g, "Case #%d: %lld\n", k + 1, total);
    }
    
    fclose(f);
    fclose(g);
    
    return 0;
}
