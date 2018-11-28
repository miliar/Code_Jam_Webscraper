//      GoroSort.cpp
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

unsigned estimateSortStepCount(vector<unsigned> elems) {
    const unsigned elemCount = elems.size();
    unsigned steps = elemCount;
    for (unsigned i = 0; i < elemCount; ++i) {
        if (elems[i] == i+1) --steps;
    }
    return steps;
}

int main(int argc, char **argv)
{
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);
    unsigned int tcnum;
    input >> tcnum;
    for (unsigned int i = 0; i < tcnum; ++i) {
        unsigned elemCount;
        input >> elemCount;
        vector<unsigned> elemArray;

        for (unsigned j = 0; j < elemCount; ++j) {
            unsigned elem;
            input >> elem;
            elemArray.push_back(elem);
        }

        unsigned result = estimateSortStepCount(elemArray);
        output << "Case #" << i+1 << ": " << result << ".000000" << endl;
        cout   << "Case #" << i+1 << ": " << result << ".000000" << endl;
    }
    input.close();
    output.close();
    return 0;
}

