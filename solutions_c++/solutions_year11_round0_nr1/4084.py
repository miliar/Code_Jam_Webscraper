#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int i, oi, bi, b, T, N, total;
    int nextB, nextO;
    char r;
    vector<int> orange; // Orange's buttons
    vector<int> blue;   // Blue's buttons
    vector<char> I;      // Robot's turns
    
    scanf("%d", &T);
    for (int it = 1; it <= T; it++) {
        scanf("%d ", &N);
        I.erase(I.begin(), I.end());
        orange.erase(orange.begin(), orange.end());
        blue.erase(blue.begin(), blue.end());
        for (i = 0; i < N; i++) {
            scanf ("%c %d ", &r, &b);
            if (r == 'O')
                orange.push_back(b);
            else if (r == 'B')
                blue.push_back(b);
            I.push_back(r);
        }
        
        nextB = nextO = total = 0;
        oi = bi = 1;
        for (i = 0; i < int(I.size()); i++) {
            if (I[i] == 'O') {
                if (oi == orange[nextO]) {
                    total++;
                    if (bi != blue[nextB])
                        bi = (bi < blue[nextB]) ? (bi + 1) : (bi - 1);
                } else if (oi < orange[nextO]) {
                    while (oi < orange[nextO]) {
                        total++;
                        if (bi != blue[nextB])
                            bi = (bi < blue[nextB]) ? (bi + 1) : (bi - 1);
                        oi++;
                    }
                    total++;    // Push button
                    if (bi != blue[nextB])  // While orange push button blue can advance
                            bi = (bi < blue[nextB]) ? (bi + 1) : (bi - 1);
                } else {
                    while (oi > orange[nextO]) {
                        total++;
                        if (bi != blue[nextB])
                            bi = (bi < blue[nextB]) ? (bi + 1) : (bi - 1);
                        oi--;
                    }
                    total++;    // Push button
                    if (bi != blue[nextB])
                            bi = (bi < blue[nextB]) ? (bi + 1) : (bi - 1);
                }
                nextO++;
                //cout << "bi = " << bi << "  oi = " << oi << " total = " << total << endl;
            } else { // Ends Orange turn
                if (bi == blue[nextB]) {
                    total++;
                    if (oi != orange[nextO])
                        oi = (oi < orange[nextO]) ? (oi + 1) : (oi - 1);
                } else if (bi < blue[nextB]) {
                    while (bi < blue[nextB]) {
                        total++;
                        if (oi != orange[nextO])
                            oi = (oi < orange[nextO]) ? (oi + 1) : (oi - 1);
                        bi++;
                        //cout << "bi = " << bi << " oi = " << oi << endl;
                    }
                    total++;    // Push button
                    if (oi != orange[nextO])
                        oi = (oi < orange[nextO]) ? (oi + 1) : (oi - 1);
                } else {
                    while (bi > blue[nextB]) {
                        total++;
                        if (oi != orange[nextO])
                            oi = (oi < orange[nextO]) ? (oi + 1) : (oi - 1);
                        bi--;
                    }
                    total++;    // Push button
                    if (oi != orange[nextO])
                        oi = (oi < orange[nextO]) ? (oi + 1) : (oi - 1);
                }
                nextB++;
                //cout << "bi = " << bi << "  oi = " << oi << endl << endl;
            } // Ends Blue turn
        }
        
        cout << "Case #" << it << ": " << total << endl;
        
        
    } // Ends test cases
    return 0;
}

