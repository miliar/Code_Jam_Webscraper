
#include <iostream>
#include <vector>

using namespace std;

class F
{
public:
    enum state_type {
        zero,
        t,
        o1,
        o2,
        o3,
        x1,
        x2,
        x3,
        ook,
        xok,
    };

private:
    state_type state;

public:
    F() 
        : state(zero) {
        
    }
    
    state_type getResult() {
        return state;
    }

    void receive(char c) {
        if (state == ook || state == xok)
            return;

        if (c == 'O') {
            if (state == zero)
                state = o1;
            else if (state == o1 || state == t)
                state = o2;
            else if (state == o2)
                state = o3;
            else if (state == o3)
                state = ook;
            else 
                state = zero;
        }
        else if (c == 'X') {
            if (state == zero)
                state = x1;
            else if (state == x1 || state == t)
                state = x2;
            else if (state == x2)
                state = x3;
            else if (state == x3)
                state = xok;
            else
                state = zero;
        }
        else if (c == 'T') {
            if (state == x1)
                state = x2;
            else if (state == x2)
                state = x3;
            else if (state == x3)
                state = xok;
            else if (state == o1)
                state = o2;
            else if (state == o2)
                state = o3;
            else if (state == o3)
                state = ook;
        }
        else
            state = zero;
    }
};

int main(int argc, char *argv[])
{
    int t;
    cin >> t;

    for (int i = 0; i<t; ++i)
    {
        vector<char> v;
        bool isdraw = true;
        F xs[4];
        F ys[4];
        F di[2];

        for (int j=0; j<16; ++j) {
            char c;
            cin >> c;
            v.push_back(c);
        }

        for (int y=0; y<4; ++y) {
            for (int x=0; x<4; ++x) {
                char c = v[4*y+x];
                xs[x].receive(c);
                ys[y].receive(c);
                if (y == x)
                    di[0].receive(c);
                if (3 - y == x)
                    di[1].receive(c);
                if (c == '.')
                    isdraw = false;
            }
        }

        cout << "Case #" << (i+1) << ": ";
        for (int j=0; j<4; ++j) {
            if (xs[j].getResult() == F::xok || ys[j].getResult() == F::xok || (j < 2 && di[j].getResult() == F::xok)) {
                cout << "X won\n";
                goto next_problem;
            } 
            else if (xs[j].getResult() == F::ook || ys[j].getResult() == F::ook || (j < 2 && di[j].getResult() == F::ook)) {
                cout << "O won\n";
                goto next_problem;
            }
            else if (isdraw) {
                cout << "Draw\n"; 
                goto next_problem;
            }
        }
        cout << "Game has not completed\n";
    next_problem:
        ;
    }
    return 0;
}
