//      Square Tiles.cpp
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

typedef vector< vector< char > > Picture;

bool rePaint (Picture & picture) {
    if (picture.size() == 0) return true;
    unsigned maxX = picture[0].size(), maxY = picture.size();
    for (unsigned y = 0; y < maxY; ++y) {
        for (unsigned x = 0; x < maxX; ++x) {
            if (picture[y][x] == '#') {
                if (x != maxX - 1 &&
                    y != maxY -1 &&
                    picture[y+1][x] == '#' &&
                    picture[y][x+1] == '#' &&
                    picture[y+1][x+1] == '#')
                {
                    picture[y][x] = '/';
                    picture[y][x+1] = '\\';
                    picture[y+1][x] = '\\';
                    picture[y+1][x+1] = '/';
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

int main(int argc, char **argv) {
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);

    unsigned testCaseCount;
    input >> testCaseCount;

    for (unsigned testCase = 0; testCase < testCaseCount; ++testCase) {
        output << "Case #" << testCase+1 << ":" << endl;
        cout   << "Case #" << testCase+1 << ":" << endl;

        unsigned row, column;
        input >> row;
        input >> column;

        Picture picture;

        for (unsigned y = 0; y < row; ++y) {
            vector<char> line;
            for (unsigned x = 0; x < column; ++x) {
                char dot;
                input >> dot;
                line.push_back(dot);
            }
            picture.push_back(line);
        }

        bool isRepaintSuccessful = rePaint(picture);

        if ( isRepaintSuccessful ) {
            for (unsigned y = 0; y < row; ++y) {
                for (unsigned x = 0; x < column; ++x) {
                    output << picture[y][x];
                    cout   << picture[y][x];
                }
                output << endl;
                cout   << endl;
            }
        } else {
            output << "Impossible" << endl;
            cout   << "Impossible" << endl;
        }
    }

    input.close();
    output.close();
    return 0;
}
