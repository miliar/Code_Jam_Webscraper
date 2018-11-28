#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>


using namespace std;
typedef unsigned long long ullong;

typedef pair<ullong, ullong> pairVal;
typedef map<ullong, ullong> mapVal;

struct GCase
{
    int N;
    vector<ullong> S;

    bool EqualSum()
    {
        sort(S.begin(), S.end());
        //vector<vector<ullong>> T;
        //T.resize (1000000000000);
        //set<ullong> sums;
        map<ullong, ullong> sums;
        //sums.insert(0, 0);
        //T.resize(1000000000000);
        for (int i = 0; i < N; ++i)
        {
            ullong ele = S[i];
            vector<pairVal> newEle;
            mapVal::iterator iter = sums.begin();
            //newEle.push_back(pairVal(ele,0));
            if (sums.find(ele) != sums.end())
            {
                mapVal::iterator it = sums.find(ele);
                ullong t = it->second;
                cout << ele << endl;
                cout << ele-t << ' ';
                while ( t != 0)
                {
                    it = sums.find(it->second);
                    cout << it->first-it->second << ' ';
                    t = it->second;
                }
                return true;
                /*cout << "sum " << ele << endl;
                return true;*/
            }
            else
                sums.insert(pairVal(ele,0));

            for (; iter != sums.end(); ++iter)
            {
                if (iter->first == ele)
                    continue;

                ullong val = iter->first + ele;
                if (sums.find(val) != sums.end())
                {
                    cout << ele << ' ';
                    mapVal::iterator it1 = sums.find(iter->first);
                    cout << it1->first - it1->second << ' ';
                    ullong m = it1->second;
                    while ( m != 0)
                    {
                        it1 = sums.find(it1->second);
                        cout << it1->first-it1->second << ' ';
                        m = it1->second;
                    }

                    cout << endl;
                    mapVal::iterator it = sums.find(val);
                    cout << it->first - it->second << ' ';
                    ullong t = it->second;
                    while ( t != 0)
                    {
                        it = sums.find(it->second);
                        cout << it->first-it->second << ' ';
                        t = it->second;
                    }
                    return true;
                }
                else
                {
                    newEle.push_back(pairVal(val, iter->first));
                }
            }
            for (int j = 0; j < newEle.size(); ++j)
                sums.insert(newEle[j]);
        }

        return false;
    }
};

int g_nCases;
vector<GCase*> g_cases;

void read_input(char* filename)
{
    ifstream fin (filename);
    if (!fin)
    {
        cerr << "Can't open the file " << filename << endl;
        exit(-1);
    }

    fin >> g_nCases;
    for (int i = 0; i < g_nCases; ++i)
    {
        GCase* gc = new GCase;
        // do sth
        fin >> gc->N;
        for (int j = 0; j < gc->N; ++j)
        {
            ullong t;
            fin >> t;
            gc->S.push_back(t);
        }
        g_cases.push_back(gc);
    }
    fin.close();
}

int main(int argc, char**argv)
{
    //read_input("test.in");
    read_input("C-small-attempt2.in");
    //read_input("A-small-attempt0.in");
    //read_input("A-large.in");

    ofstream fout("A.out");
    for (int i = 0; i < g_nCases; ++i)
    {
        //g_cases[i]->debugOutput();
        cout << "Case #" << i+1 << ": " << endl;
        if (g_cases[i]->EqualSum())
            cout << endl ;
        else
            cout << "Impossible" << endl;
        //g_cases[i]->genOutput();
        //cout << g_cases[i]->output << endl;
        //for (int j = 0; j < g_cases[i]->d_size; ++j)
        //{
        //    fout << g_cases[i]->RPI(j) << endl;
        //    /*cout << g_cases[i]->WP(j) << endl;*/
        //    //cout << g_cases[i]->OWP(j) << endl;
        //    //cout << g_cases[i]->OOWP(j) << endl;
        //}
        //int minSteps = calMinSteps(g_BScases[i]);
        //<< minSteps << endl;
    }
    fout.close();
    return 0;
}
