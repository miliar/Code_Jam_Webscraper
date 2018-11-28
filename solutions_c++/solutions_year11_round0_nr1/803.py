#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int abs(int a)
{
    if (a < 0)
        return -a;
    else
        return a;
}
struct Order
{
    char robot;
    int spot;
    Order(char r, int s) : robot(r), spot(s) { }
    Order() { }
};

int main()
{
    ifstream fin("task1.in");
    ofstream fout("task1.out");
    int total;
    fin >> total;
    for (int brojac = 0; brojac < total; ++brojac)
    {
        vector<Order> orders;
        int n;
        fin >> n;
        while (n--)
        {
            char c;
            int b;
            fin >> c >> b;
            orders.push_back(Order(c, b));
        }
        
        int sz = orders.size();
        int O = 1;
        int B = 1;
        int moves = 0;
        for (int current = 0; current < sz; ++current)
        {
            int next_o;
            int next_b;
            for (int i = current; i < sz; ++i)
            {
                if (orders[i].robot == 'O')
                {
                    next_o = orders[i].spot;
                    break;
                }
            }
            for (int i = current; i < sz; ++i)
            {
                if (orders[i].robot == 'B')
                {
                    next_b = orders[i].spot;
                    break;
                }
            }
            int next = orders[current].spot;
            int use;
            if (orders[current].robot == 'O')
                use = O;
            else
                use = B;
            int add_moves = abs(orders[current].spot - use) + 1;
            moves += add_moves;
            if (orders[current].robot == 'O')
            {
                O = next;
                if (B < next_b)
                {
                    B += add_moves;
                    if (B > next_b)
                        B = next_b;
                }
                else if (B > next_b)
                {
                    B -= add_moves;
                    if (B < next_b)
                        B = next_b;
                }
            }
            else
            {
                B = next;
                if (O < next_o)
                {
                    O += add_moves;
                    if (O > next_o)
                        O = next_o;
                }
                else if (O > next_o)
                {
                    O -= add_moves;
                    if (O < next_o)
                        O = next_o;
                }
            }
        }
        fout << "Case #" << brojac + 1 << ": " << moves << endl;
    }
    return 0;
}
