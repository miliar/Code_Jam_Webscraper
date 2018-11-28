
#ifndef SAVING_UNIVERSE_CASE_H__
#define SAVING_UNIVERSE_CASE_H__

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class SavingUniverseCase
{
private:
        vector<string> m_engine_vec;
        vector<string> m_query_vec;
        istream & GetStrVec (istream & is, vector<string> &str_vec);
        ostream & PutStrVec (ostream & os, const vector<string> &str_vec)const;

public:
        SavingUniverseCase();
        friend istream & operator >> (istream & is, SavingUniverseCase & saving_universe_case);
        friend ostream & operator << (ostream & os, const SavingUniverseCase & saving_universe_case);
        int Solve(string& result);
};

#endif
