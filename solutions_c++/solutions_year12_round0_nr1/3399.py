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
#include <map>
#include <set>

#include <fstream>

#include <cassert>

using namespace std;

int main(int /*argc*/, char ** /*argv*/)
{
    string o = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
               "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
               "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string t = "our language is impossible to understand"
               "there are twenty six factorial possibilities"
               "so it is okay if you want to just give up";
    map <char, char> m;
    m['z'] = 'q'; m['q'] = 'z';

    for (unsigned i = 0; i < o.length(); ++i) {
        auto iter = m.find(o[i]);

        if (iter == m.end()) {
            m[o[i]] = t[i];
            cout << o[i] << ">" << t[i] << ",";
        } else {
            assert(m[o[i]] == t[i]);
        }
        cout << endl;
    }

    unsigned lineCount = 0;
    string line;
    ifstream input("input.txt");
    ofstream output("output.txt");

    if (input.is_open() && output.is_open()) {
        input >> lineCount;
        unsigned tci = 0;

        while (input.good() && output.good()) {
            getline(input, line);
            if (line.length() == 0) {
                ++tci;
                continue;
            }

            for (unsigned i = 0; i < line.length(); ++i) {
                line[i] = m[line[i]];
            }

            output << "Case #" << tci++ << ": " << line << "\n";
        }

        input.close();
        output.close();
    } else {
        cout << "Unable to open files";
    }

    return 0;
}

