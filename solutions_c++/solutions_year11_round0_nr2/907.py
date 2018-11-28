//      Magicka.cpp
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

void compressSpell(string & spell, const vector<string> & comboElements) {
    const unsigned spellSize = spell.length();
    if (spellSize < 2) return;
    //cout << "compressSpell: " << spell;
    const unsigned elemSize = comboElements.size();
    for (unsigned i = 0; i < elemSize; ++i) {
        char elem_a = comboElements[i][0];
        char elem_b = comboElements[i][1];
        char elem_n = comboElements[i][2];
        if ((spell[spellSize-2] == elem_a && spell[spellSize-1] == elem_b) ||
                (spell[spellSize-2] == elem_b && spell[spellSize-1] == elem_a)) {
            spell[spellSize-2] = elem_n;
            spell.resize(spellSize-1);
            //cout << " -> " << spell << " (" << elem_a << " and " << elem_b << " is combined to " << elem_n << ")" << endl;
            return;
        }
    }
    //cout << " hasn't changed." << endl;
}

void cleanSpell(string & spell, const vector<string> & antiElements) {
    const unsigned spellSize = spell.length();
    if (spellSize < 2) return;
    //cout << spell << ": ";
    const unsigned elemSize = antiElements.size();
    for (unsigned i = 0; i < elemSize; ++i) {
        char elem_a = antiElements[i][0]; //cout << "elem_a = " << elem_a << ", ";
        char elem_b = antiElements[i][1]; //cout << "elem_b = " << elem_b << ", ";
        bool elem_a_found = spell.find(elem_a) != string::npos; //cout << "elem_a_found = " << elem_a_found << ", ";
        bool elem_b_found = spell.find(elem_b) != string::npos; //cout << "elem_b_found = " << elem_b_found << ", ";
        if (elem_a_found && elem_b_found) {
            spell.clear();
            //cout << "Spell cleared" << endl;
            return;
        }
        //cout << endl;
    }
}

string resolveSpell(const vector<string> & combine, const vector<string> & oppose, const string & spell) {
    const unsigned spellLen = spell.length();
    string spellRes;
    for (unsigned pos = 0; pos < spellLen; ++pos) {
        spellRes += spell[pos];
        //cout << "new spell = [" << spellRes << "]" << endl;
        compressSpell(spellRes, combine);
        cleanSpell(spellRes, oppose);
    }
    return spellRes;
}

string formatSpell ( const string & text) {
    string result = "[";
    for (unsigned i = 0; i < text.length(); ++i) {
        if (i != 0) result += ", ";
        result += text[i];
    }
    result += "]";
    return result;
}

int main(int argc, char **argv)
{
    fstream input, output;
    input.open ("input.txt", fstream::in);
    output.open ("result.txt", fstream::out);
    unsigned int tcnum;
    input >> tcnum;
    for (unsigned int i = 0; i < tcnum; ++i) {
        unsigned int elementNum;
        input >> elementNum;
        vector<string> combinedElements;
        for (unsigned j = 0; j < elementNum; ++j) {
            string tmp;
            input >> tmp;
            //cout << "combElem = " << tmp << endl;
            combinedElements.push_back(tmp);
        }

        unsigned int opposeNum;
        input >> opposeNum;
        vector<string> antiElements;
        for (unsigned j = 0; j < opposeNum; ++j) {
            string tmp;
            input >> tmp;
            //cout << "antiElem = " << tmp << endl;
            antiElements.push_back(tmp);
        }

        unsigned spellLength;
        input >> spellLength;
        string spell;
        input >> spell;
        
        string result = formatSpell(resolveSpell(combinedElements, antiElements, spell));

        output << "Case #" << i+1 << ": " << result << endl;
        cout   << "Case #" << i+1 << ": " << result << endl;
    }
    input.close();
    output.close();
    return 0;
	return 0;
}

