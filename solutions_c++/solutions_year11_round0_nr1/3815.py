#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct ButType
{
    bool d_type; // true for orange, false for blue
    int d_number;
    ButType(bool type, int number): d_type(type), d_number(number) {}
};

struct ButSeq
{
    vector<ButType*> d_butlist;
};

int g_nBSCases;
int g_curBot;
vector<ButSeq*> g_BScases;

void read_input(char* filename)
{
    ifstream fin (filename);
    if (!fin)
    {
        cerr << "Can't open the file " << filename << endl;
        exit(-1);
    }

    fin >> g_nBSCases;
    for (int i = 0; i < g_nBSCases; ++i)
    {
        int nButtons;
        char chTmp;
        int nTmp;
        ButSeq* bs = new ButSeq;
        fin >> nButtons;
        for (int j = 0; j < nButtons; ++j)
        {
            fin >> chTmp >> nTmp;
            if (chTmp == 'O')
                bs->d_butlist.push_back(new ButType(true, nTmp));
            else if (chTmp == 'B')
                bs->d_butlist.push_back(new ButType(false, nTmp));
        }
        g_BScases.push_back(bs);
    }
    fin.close();
}

int getTar(const ButSeq* bs, bool bType)
{
    for (int i = (g_curBot+1); i < bs->d_butlist.size(); ++i)
    {
        if (bs->d_butlist[i]->d_type == bType)
            return bs->d_butlist[i]->d_number;
    }
    return -1;
}

int calMinSteps (const ButSeq* bs)
{
    g_curBot = -1;
    int minSteps = 0;
    int oPos = 1, bPos = 1;
    int oTar = getTar(bs, true);
    int bTar = getTar(bs, false);
    int oMin = abs(oTar - oPos);
    int bMin = abs(bTar - bPos);
    while (g_curBot != bs->d_butlist.size()-1)
    {
        if (bs->d_butlist[g_curBot+1]->d_type)
        {
            minSteps += (oMin + 1);
            bMin -= (oMin + 1);

            ++g_curBot;
            if (bMin < 0)
                bMin = 0;
            oTar = getTar(bs, true);
            if (oTar < 0)
                oMin = 0;
            else
                oMin = abs(oTar - bs->d_butlist[g_curBot]->d_number);
        }
        else
        {
            minSteps += (bMin + 1);
            oMin -= (bMin+1);
            
            ++g_curBot;
            if (oMin < 0)
                oMin = 0;
            bTar = getTar(bs, false);
            if (bTar < 0)
                bMin = 0;
            else
                bMin = abs( bTar - bs->d_butlist[g_curBot]->d_number);
        }
    }
    cout << minSteps << endl;
    return minSteps;
}

int main(int argc, char**argv)
{
    read_input("A-large.in");

    ofstream fout("a_large.out");
    for (int i = 0; i < g_nBSCases; ++i)
    {
        int minSteps = calMinSteps(g_BScases[i]);
        fout << "Case #" << i+1 << ": " << minSteps << endl;
    }
    fout.close();
    return 0;
}