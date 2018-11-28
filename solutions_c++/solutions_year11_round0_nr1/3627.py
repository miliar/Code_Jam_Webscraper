#include<iostream>
#include <cstdlib>
using namespace std;
#include <fstream>

bool move(int r, int &pre, int next) {
    if (pre < next)
        pre++;
    else
        if (pre > next)
        pre--;
    if (pre == next)
        return true;
    return false;

}

int main(int argc, char** argv) {


    char buffer[10];
    ifstream in;
    ofstream out;
    in.open("A-large.in", ios_base::in);
    out.open("output.txt", ios_base::out);
    if (in && out) {

        int m;
        in >> buffer;
        m = atoi(buffer);
        for (int k = 0; k < m; k++) {

            bool b1 = false;
            bool b2 = false;
            int r1 = 1;
            int r2 = 2;
            int p1 = 1, p2 = 1;
            int *R1;
            int *R2;
            int n;
            int n1 = 0;
            int n2 = 0;
            char *order;


            in >> buffer;
            n = atoi(buffer);
            R1 = new int[n];
            R2 = new int[n];
            order = new char[n];
            for (int i = 0; i < n; i++) {
                in >> buffer;
                if (buffer[0] == 'B') {
                    in >> buffer;
                    R1[n1] = atoi(buffer);
                    order[i] = 'B';
                    n1++;
                } else {
                    in >> buffer;
                    R2[n2] = atoi(buffer);
                    order[i] = 'O';
                    n2++;
                }
            }
            int time = 0;
            int next = 0;
            int i1 = 0, i2 = 0;
            if(order[0]=='B' && R1[0]==1)
                b1=true;
            if(order[0]=='O' && R2[0]==1)
                b2=true;
            for (int i = 0; i1 < n1 || i2 < n2; i++) {
                if (b1 && order[next] == 'B') {
                    if(i1+1<n1 && R1[i1+1]!=R1[i1])
                    b1 = false;
                    if(i2<n2)
                    b2 = move(r2, p2, R2[i2]);
                    time++;
                    next++;
                    i1++;
                } else if (b2 && order[next] == 'O') {
                    if(i2+1<n2 && R2[i2+1]!=R2[i2])
                    b2 = false;
                    if(i1<n1)
                    b1 = move(r1, p1, R1[i1]);
                    time++;
                    next++;
                    i2++;
                } else {
                    if (i1 < n1)
                        b1 = move(r1, p1, R1[i1]);
                    if (i2 < n2)
                        b2 = move(r2, p2, R2[i2]);
                    time++;
                }
            }
            out << "Case #" << k + 1 << ": " << time << endl;
        }
    }
    in.close();
    out.close();
}
