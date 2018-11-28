#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

template <typename T>
T toType(const string& str)
{
    istringstream iss(str);
    T ret;
    iss >> ret;
    return ret;
}

struct Magicka {
    map<string, char> mCombo;
    map<char, char> mOpposing;
    string mIn;
};

void extractInfo(const string& str, vector<Magicka> &spells)
{
    Magicka magic;
    string tmp;
    int combo = 0, opp = 0, n = 0;
    unsigned int i = 0;
    for(i = 0; str[i] != ' '; ++i)
        tmp += str[i];
    combo = toType<int>(tmp);
    //cout << "\nCombo: " << combo << flush;
    while(combo > 0) {
        i++;
        tmp = str.substr(i, 2);
        magic.mCombo.insert(make_pair<string, char>(tmp, str[i+2]));
        //cout << "\nstring: " << tmp << "\tchar: " << str[i+2] << flush;
        if(str[i] != str[i+1]) {
            tmp = str[i+1];
            tmp += str[i];
            magic.mCombo.insert(make_pair<string, char>(tmp, str[i+2]));
            //cout << "\nstring: " << tmp << "\tchar: " << str[i+2] << flush;
        }
        i += 3;
        --combo;
    }
    tmp = "";
    for(i += 1; str[i] != ' '; ++i)
        tmp += str[i];
    opp = toType<int>(tmp);
    //cout << "\nOpp: " << opp << flush;
    while(opp > 0) {
        i++;
        magic.mOpposing.insert(make_pair<char, char>(str[i], str[i+1]));
        //cout << "\nchar: " << str[i] << "\tchar: " << str[i+1] << flush;
        magic.mOpposing.insert(make_pair<char, char>(str[i+1], str[i]));
        //cout << "\nchar: " << str[i+1] << "\tchar: " << str[i] << flush;
        i += 2;
        --opp;
    }
    for(i += 1; str[i] != ' '; ++i)
        tmp += str[i];
    n = toType<int>(tmp);
    //cout << "\nN: " << n << flush;
    magic.mIn = str.substr((size_t)i+1, n);
    //cout << "\ninstring: " << magic.mIn << flush;
    spells.push_back(magic);
}

string invoke(const Magicka& spell)
{
    string ret = "[", buf;
    map<string, char>::const_iterator mpt;
    map<char, char>::const_iterator cpt;
    pair<char, char> opp;
    pair<string, char> combo;
    vector<char> elem;
    vector<char>::iterator it;
    bool fFlag;

    for(unsigned int i = 0; i < spell.mIn.length(); ++i) {
        if(elem.empty())
            elem.push_back(spell.mIn[i]);
        else {
            // Check for opp
            for(it = elem.begin(), fFlag = false; it < elem.end() && !fFlag; ++it) {
                fFlag = false;
                cpt = spell.mOpposing.find(*it);
                if(cpt != spell.mOpposing.end()) {
                    opp = *cpt;
                    buf = elem.back();
                    buf += spell.mIn[i];
                    mpt = spell.mCombo.find(buf);
                    if(opp.second == spell.mIn[i] && mpt == spell.mCombo.end()) {
                        elem.clear();
                        i++;
                        fFlag = true;
                    }
                }
            }

            buf = elem.back();
            buf += spell.mIn[i];
            mpt = spell.mCombo.find(buf);
            if(mpt != spell.mCombo.end()) {
                combo = *mpt;
                elem.pop_back();
                elem.push_back(combo.second);
            } else
                elem.push_back(spell.mIn[i]);
        }
    }

    if(elem.empty())
        ret += "]";
    else {
        for(it = elem.begin(); it < elem.end(); ++it) {
            ret += *it;
            ret += ", ";
        }
        ret += "\b\b]";
    }

    return ret;
}

int main(int argc, char **argv)
{
    if(argc > 1) {
        vector<Magicka> spells;
        string buffer;
        ifstream in;
        ofstream out;

        in.open(argv[1], ios::in);
        out.open("magicka.out", ios::out);
        getline(in, buffer, '\n');

        while(getline(in, buffer, '\n')) {
            extractInfo(buffer, spells);
        }

        for(unsigned int i = 0; i < spells.size(); ++i)
            cout << "Case #" << i+1 << ": " << invoke(spells[i]) << '\n';
        in.close();
        out.close();

    } else {
        cerr << "\n\n\t\033[1;31mERROR:\033[0m No input files!\n\n";
    }

    return 0;
}
