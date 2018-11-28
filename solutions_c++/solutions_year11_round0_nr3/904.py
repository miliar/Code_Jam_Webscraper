//      Candy.cpp
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
#include <bitset>
#include <algorithm>
#include <climits>

using namespace std;

bool isCryingAvoidable(const vector<unsigned> & candies) {
    unsigned sum = 0;
    for (unsigned int i = 0; i < candies.size(); ++i) {
        sum ^= candies[i];
        //cout << sum << ", " ;
    }
    return sum == 0;
}

unsigned candyPatrickValue(const vector<unsigned> & candies) {
    unsigned sum = 0;
    for (unsigned int i = 0; i < candies.size(); ++i) {
        sum ^= candies[i];
    }
    return sum;
}

unsigned candySeanValue(const vector<unsigned> & candies) {
    unsigned sum = 0;
    for (unsigned int i = 0; i < candies.size(); ++i) {
        sum += candies[i];
    }
    return sum;
}

unsigned countMaxValue (const vector<unsigned> & candies) {
    const unsigned candiesnum = candies.size();
    bitset<1000> isPatricks;
    isPatricks.set(0);
    do {
        unsigned seanXOR = 0, seanSUM = 0, patrickXOR = 0;
        for (unsigned int i = 0; i < candiesnum; ++i) {
            if (isPatricks.test(i)) {
                patrickXOR ^= candies[i];
//                cout << "It's patrick's : " << candies[i] << " -> " << patrickXOR << endl;
            } else {
                seanXOR ^= candies[i];
                seanSUM += candies[i];
//                cout << "It's sean's : " << candies[i] << " -> " << seanXOR << ":" << seanSUM << endl;
            }
        }
//        cout << "Summary: " << isPatricks.to_string().substr(0, candiesnum) << " -> " << seanXOR << " vs " << patrickXOR << " (" << seanSUM << ")\n";

        if (seanXOR == patrickXOR) {
            return seanSUM;
        }
        for (unsigned i = 0; i < candiesnum; ++i) {
            isPatricks.flip(i);
            if (isPatricks.test(i)) {
                break;
            }
        }
    } while (!isPatricks.test(candiesnum));
    
    return 0;
}

int main(int argc, char **argv)
{
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);
    unsigned int tcnum;
    input >> tcnum;
    for (unsigned int i = 0; i < tcnum; ++i) {
        unsigned int candyNum;
        input >> candyNum;
        vector<unsigned> candies;
        for (unsigned j = 0; j < candyNum; ++j) {
            unsigned candyValue;
            input >> candyValue;
            candies.push_back(candyValue);
        }
        unsigned int retval = 0;
        if (isCryingAvoidable(candies)) {
            sort(candies.begin(), candies.end());
            retval = countMaxValue(candies);
        }
        if (retval > 0) {
            output << "Case #" << i+1 << ": " << retval << endl;
            cout   << "Case #" << i+1 << ": " << retval << endl;
        } else {
            output << "Case #" << i+1 << ": NO" << endl;
            cout   << "Case #" << i+1 << ": NO" << endl;
        }
    }
    input.close();
    output.close();
    return 0;
}

