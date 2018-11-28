/*
 * solve.cc
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
#include <algorithm>

#include <cassert>

using namespace std;

struct Pair {
    unsigned a;
    unsigned b;
};

struct Cmp {
    bool operator()(const Pair & lhv) {
        return (lhv.a==p.a && lhv.b == p.b) || (lhv.a==p.b && lhv.b == p.a);
    }
    Pair p;
};

unsigned log10(unsigned num) {
    unsigned i = 1;
    while (num /= 10) ++i;
    return i;
}

unsigned a10(unsigned hatvany) {
    unsigned sol = 1;
    for (unsigned i = 1; i < hatvany; ++i) {
        sol *= 10;
    }
    return sol;
}

unsigned shift(unsigned num, unsigned shift) {
    const unsigned log = log10(num);
    const unsigned max = a10(log);
    for (unsigned i = 0; i < shift; ++i) {
        num = num/10 + max*(num%10);
    }
    if (log10(num) != log) num = 0;
    return num;
}

unsigned solve(unsigned A, unsigned B) {
    vector<Pair> solutions;
    unsigned num2, l = log10(B);
    for (unsigned num = A; num <= B; ++num) {
        for (unsigned i = 1; i < l; ++i) {
            num2 = shift(num, i);
            if (num2 != 0 && num < num2 && num2 <= B && num2 >= A) {
                if (find_if(solutions.begin(), solutions.end(), Cmp{Pair{num, num2}}) == solutions.end()) {
                    solutions.push_back(Pair{num, num2});
                }
            }
        }
    }

    return solutions.size();
}

int main(int /*argc*/, char ** /*argv*/)
{
    ifstream input ("input.txt");
    ofstream output("output.txt");

    if (input.is_open() && output.is_open()) {
        unsigned TCcount = 0;
        input >> TCcount;
        for (unsigned i = 0; i < TCcount; ++i) {
            unsigned A, B;
            input >> A;
            input >> B;
            output << "Case #" << i+1 << ": " << solve(A, B) << "\n";
        }
        input.close();
        output.close();
    } else {
        cout << "Unable to open files";
    }

    return 0;
}

