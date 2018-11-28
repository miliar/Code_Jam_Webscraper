#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream input("A-large.in", fstream::in);
    ofstream output("out.txt", fstream::out);
    std::list<char> order;
    std::list<int> Obuttons;
    std::list<int> Bbuttons;

    int T;
    bool Opush = false;
    input >> T;
    for (int i=0; i < T; i++) {
        int Opos = 1;
        int Bpos = 1;
        unsigned int N;
        input >> N;
        for (unsigned int j=0; j<N; j++) {
            char color;
            int button;
            input >> color >> button;
            order.push_back(color);
            if (color == 'O') Obuttons.push_back(button);
            else Bbuttons.push_back(button);
        }
        if (order.front() == 'O') Opush = true;
        int time = 0;
        while (!order.empty()) {
            if (Opos > Obuttons.front())  Opos--;
            else if (Opos < Obuttons.front()) Opos++;
            else if (Opush) {
                Obuttons.pop_front();
                order.pop_front();
            }
            if (Bpos > Bbuttons.front())  Bpos--;
            else if (Bpos < Bbuttons.front()) Bpos++;
            else if (!Opush) {
                Bbuttons.pop_front();
                order.pop_front();
            }
            if (order.front() == 'O') Opush = true;
            else Opush = false;
            time++;
        }
        output << "Case #" << i+1 << ": " << time << "\n";
    }
    return 0;
}
