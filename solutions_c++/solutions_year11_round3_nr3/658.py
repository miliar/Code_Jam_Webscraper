//      Perfect Harmony.cpp
//
//      Copyright 2011 Tóth Bence <totesz@totesz-desktop>
//
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

unsigned getHarmony(unsigned lowestNote, unsigned highestNote, const vector<unsigned> & frequencies) {
    for (unsigned frequency = lowestNote; frequency <= highestNote; ++frequency) {
        bool found = true;
        for (unsigned i = 0; i < frequencies.size() && found; ++i) {
            if (frequency % frequencies[i] == 0 || frequencies[i] % frequency == 0) {
                // found, check the next musician...
            } else {
                found = false;
            }
        }
        if (found) return frequency;
    }
    return 0;
}

int main(int argc, char **argv) {
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);

    unsigned testCaseCount;
    input >> testCaseCount;

    for (unsigned testCase = 0; testCase < testCaseCount; ++testCase) {
        output << "Case #" << testCase+1 << ": ";
        cout   << "Case #" << testCase+1 << ": ";

        unsigned musicians;
        input >> musicians;
        unsigned lowestNote;
        input >> lowestNote;
        unsigned highestNote;
        input >> highestNote;

        vector<unsigned> frequencies;
        for (unsigned i = 0; i < musicians; ++i) {
            unsigned frequency;
            input >> frequency;
            frequencies.push_back(frequency);
        }

        unsigned result = getHarmony(lowestNote, highestNote, frequencies);

        if (result) {
            output << result << endl;
            cout   << result << endl;
        } else {
            output << "NO" << endl;
            cout   << "NO" << endl;
        }
    }

    input.close();
    output.close();
    return 0;
}

