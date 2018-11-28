/*
 * solve.ccű
 *
 * Copyright 2012 Tóth Bence <bence.toth@ericsson.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */


#include <iostream>
#include <string>
#include <vector>
#include <fstream>

#include <cassert>

using namespace std;

unsigned solve(unsigned S, unsigned p, const vector<unsigned> & t) {
    unsigned n=0, s=0, tmp;
    for (unsigned i = 0; i < t.size(); ++i) {
        tmp = t[i]/3;
        cout << t[i] << "=" << t[i]/3 << "*3+" << t[i]%3 << endl;
        if (t[i] == 0 && p != 0) continue;
        switch (t[i]%3) {
            case 0:
                if (tmp >= p) ++n;
                if (tmp+1 >= p) ++s;
            break;
            case 1:
                if (tmp+1 >= p) ++n;
                if (tmp+1 >= p) ++s;
            break;
            case 2:
                if (tmp+1 >= p) ++n;
                if (tmp+2 >= p) ++s;
            break;
        };
    }
    cout << "n=" << n << ", s=" << s << ", S=" << S << ", p=" << p << endl;
    return (s-n > S ? n+S : s);
}

int main(int /*argc*/, char ** /*argv*/)
{
    ifstream input ("input.txt");
    ofstream output("output.txt");

    if (input.is_open() && output.is_open()) {
        unsigned TCcount = 0;
        input >> TCcount;
        for (unsigned i = 0; i < TCcount; ++i) {
            unsigned N, S, p;
            vector<unsigned> t;
            input >> N;
            input >> S;
            input >> p;
            for (unsigned j = 0; j < N; ++j) {
                unsigned tmp;
                input >> tmp;
                t.push_back(tmp);
            }

            unsigned solution = solve(S, p, t);

            output << "Case #" << i+1 << ": " << solution << "\n";
        }
        input.close();
        output.close();
    } else {
        cout << "Unable to open files";
    }

    return 0;
}

