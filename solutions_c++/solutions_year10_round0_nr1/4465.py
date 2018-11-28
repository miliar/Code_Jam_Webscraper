#include <iostream>

using namespace std;

int N,K;
bool * state;
bool * power;

void dispatch_power()
{
    for(int i=1 ; i < N ; i++)
        if(state[i-1] && (power[i-1]) )
            power[i] = true;
        else
            power[i] = false;
}

void snap()
{
    for(int i=0 ; i < N ; i++)
        if(power[i])
            state[i] = !state[i];

    dispatch_power();
}

void display_state()
{
    cout << "state : ";
    for(int i=0; i < N ;i++)
        cout << state[i] << " ";

    cout << endl;
}

void display_power()
{
    cout << "power : ";
    for(int i=0; i < N ;i++)
        cout << power[i] << " ";

    cout << endl;
}

void init_state()
{
    state = new bool[N];
    power = new bool[N];
    for(int i=0 ; i <N ; i++)
    {
        state[i] = false;
        power[i] = false;
    }
    power[0] = true;
}

bool isLightOn()
{
    if(state[N-1])
    if(power[N-1])
    {
        return true;
    }

    return false;
}

void experiment()
{
    for(int i=0 ; i< K ; i++)
    {
        snap();
    }
}

int main()
{
    N=4;
    K=47;

    int T;
    cin >> T;

    int * arrayN = new int[T];
    int * arrayK = new int[T];

    for(int i=0 ; i < T ; i++)
        cin >> arrayN[i] >> arrayK[i];

    for(int i=0 ; i< T ; i++)
    {
        cout << "Case #" << (i+1) << ": ";

        N = arrayN[i];
        K = arrayK[i];

        init_state();
        experiment();

        if(isLightOn())
        cout << "ON" << endl;
        else cout << "OFF" << endl;
    }

    return 0;
}
