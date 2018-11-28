#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

const int MAX_GROUPS = 1000;
int first = -1;
int last = -1;
int grpsQueue[MAX_GROUPS];
int t;
int r, k, n;

void push(int i)
{
    if ((last + 1) % n == first) {
        cerr << "Queue is full." << endl;
        return;
    }

    last = (last + 1) % n;
    grpsQueue[last] = i;

    if (first == -1)
        first = 0;
}

void pop()
{
    if (first == -1) {
        cerr << "Queue is empty" << endl;
        return;
    }

    if (first == last)
        first = last = -1;
    else
        first = (first + 1) % n;
}

int peek()
{
    return grpsQueue[first];
}

int main()
{
    ifstream in;
    in.open("C-small.in");
    if (!in) {
        cerr << "Err, what's happening with input file." << endl;
        return 1;
    }

    ofstream out;
    out.open("out.txt");
    in >> t;

    for (int i = 1; i <= t; ++i) {
        in >> r >> k >> n;
        
        first = last = -1;      // empty queue
        int c = n;
        while (c--) {
            int temp;
            in >> temp;
            push(temp);
        }

        int sum = 0;
        while (r--) {
            int numOfGrpEntered = 0;
            int currentPeople = 0;
            while (numOfGrpEntered < n) {
                int temp = peek();
                if (currentPeople + temp <= k) {
                    currentPeople += temp;
                    sum += temp;
                    pop();
                    push(temp);
                    ++numOfGrpEntered;
                } else
                    break;
            }
        }

        out << "Case #" << i << ": " << sum;
        if (i != t)
            out << endl;
    }

    in.close();
    out.close();
}
