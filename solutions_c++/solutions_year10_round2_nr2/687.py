#include <iostream>
#include <stack>

using namespace std;


typedef struct ChickenRunStruct
{
    stack<int> FlockSpeed;
    stack<int> FlockPos;
    int Barn, FlockSize, Needed, Time;

    ChickenRunStruct(int N, int B, int T, int K)
    {
        Barn = B;
        FlockSize = N;
        Needed = K;
        Time = T;
    }

    int GetSwaps()
    {
        int swaps_needed = 0;
        int alive_chicks = 0;
        int dead_chicks = 0;
        while ((alive_chicks < Needed) && (FlockPos.size() != 0))
        {
            if ((FlockPos.top() + Time * FlockSpeed.top()) >= Barn)
            {
                swaps_needed += dead_chicks;
                alive_chicks++;
            }
            else
            {
                dead_chicks++;
            }
            FlockPos.pop();
            FlockSpeed.pop();
        }
        if (alive_chicks == Needed)
        {
            return swaps_needed;
        }
        else
        {
            return -1;
        }
    }
} ChickenRun;


int main()
{
    int C, B, T, N, K, X, V;

    cin >> C;
    for (int i=1;i<=C;i++)
    {
        cin >> N;
        cin >> K;
        cin >> B;
        cin >> T;

        ChickenRun Run = ChickenRunStruct(N, B, T, K);

        Run.FlockSize = N;
        Run.Needed = K;
        Run.Barn = B;
        Run.Time = T;

        for (int j=0;j<N;j++)
        {
            cin >> X;
            Run.FlockPos.push(X);
        }
        for (int j=0;j<N;j++)
        {
            cin >> V;
            Run.FlockSpeed.push(V);
        }

        int res = Run.GetSwaps();
        if (res < 0)
        {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << i << ": " << res << endl;
        }
    }
}
