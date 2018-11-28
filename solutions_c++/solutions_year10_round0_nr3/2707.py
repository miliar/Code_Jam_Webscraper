#include <iostream>
#include <queue>

using namespace std;


struct Roller_coaster
{
    queue<int> waiting;
    queue<int> riding;
    int load;
    int capacity;
    int benefit;

    Roller_coaster()
    {
        load = 0;
        capacity = 0;
        benefit = 0;
        while (waiting.size() > 0)
        {
            waiting.pop();
        }
        while (riding.size() > 0)
        {
            riding.pop();
        }
    }

    void MakeRide()
    {
        load = 0;
        while ((waiting.front() <= (capacity-load)) & (waiting.size() > 0))
        {
            riding.push(waiting.front());
            load += waiting.front();
            benefit += waiting.front();
            waiting.pop();
        }
        while (riding.size() > 0)
        {
            waiting.push(riding.front());
            riding.pop();
        }
    }
};

int main()
{
    int count;
    cin >> count;
    for (int i=0;i<count;i++)
    {
        Roller_coaster ride = Roller_coaster();
        int R, k, N, g;

        cin >> R;
        cin >> k;
        cin >> N;
        ride.capacity = k;

        for (int j=0;j<N;j++)
        {
            cin >> g;
            ride.waiting.push(g);
        }

        for (int j=0;j<R;j++)
        {
            ride.MakeRide();
        }
        cout << "Case #" << (i+1) << ": " << ride.benefit << endl;
    }
    return 1;
}
