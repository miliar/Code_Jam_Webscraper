#include <vector>
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

struct Chain {
    
    int size;
    bool *power, *state;
    
    Chain(int n)
        : size(n), power(new bool[n + 1]), state(new bool[n])
    {
        power[0] = true;
        memset(power + 1, false, n * sizeof(bool));
        memset(state, false, n * sizeof(bool));
    }
    
    ~Chain() {
        delete[] power;
        delete[] state;
    }
    
    inline void run(int steps) {
        for (int i = 0; i < steps; i++)
            snap();
    }
    
    inline void snap()
    {
        for (int i = 0; i < size; ++i) {
            if (power[i])
                state[i] = !state[i];
            if (i != 0)
                power[i] = power[i - 1] && state[i - 1];
        }
        power[size] = power[size - 1] && state[size - 1];
    }
    
    void dump() {
        for (int i = 0; i < size + 1; i++)
            cout << power[i] << " ";
        cout << "\n ";
        for (int i = 0; i < size; i++)
            cout << state[i] << " ";
        cout << "\n\n";
    }
    
    inline const char *output() {
        return power[size] ? "ON" : "OFF";
    }

};

int main(int argc, char **argv)
{
    int cases, size, steps;
    Chain *chain;
    
    scanf("%d", &cases);
    
    for (int i = 0; i < cases; i++) {
        scanf("%d %d", &size, &steps);
        chain = new Chain(size);
        chain->run(steps);
        printf("Case #%d: %s\n", i + 1, chain->output());
    }
}

