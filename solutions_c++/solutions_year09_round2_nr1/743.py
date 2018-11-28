// CodeJam 2009 - Round1B_A
// Autor: Benjamín de la Fuente Ranea

#include <Windows.h>
#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//-------------------------------------------------------------------------
void log(const char* fmt, ...)
{
    const unsigned MAX_LINE_BUFFER = 512;
    char    buf[MAX_LINE_BUFFER];			// Is supposed that MAX_LINE_BUFFER characters are enough.
    va_list arg;
    va_start(arg, fmt);
    vsprintf_s<MAX_LINE_BUFFER>(buf, fmt, arg);
    va_end(arg);
    printf(buf);
    OutputDebugStr(buf);
}

//-------------------------------------------------------------------------
struct TDecisionTree
{
    TDecisionTree() : pFirst(NULL), pSecond(NULL), feature("")   {}

    double p;
    string feature;

    TDecisionTree* pFirst, *pSecond;
};

//-------------------------------------------------------------------------
TDecisionTree* readTree(ifstream& fin)
{
    char c;
    fin >> c;
    while (c == ' ' || c == ')') fin >> c;

    TDecisionTree* pCurTree = NULL;
    if (c == '(')
    {
        pCurTree = new TDecisionTree;
        char feature[256];
        fin >> pCurTree->p;
        fin >> feature;
        if (feature[0] != ')')
        {
            pCurTree->feature = feature;

            pCurTree->pFirst = readTree(fin);
            pCurTree->pSecond = readTree(fin);
        }
    }

    return pCurTree;
}

//-------------------------------------------------------------------------
double traverseTree(TDecisionTree* pCurTree, vector<string>& features)
{
    double percent = pCurTree->p;
    if (!pCurTree->feature.empty())
    {
        vector<string>::const_iterator iter = find(features.begin(), features.end(), pCurTree->feature);
        if (iter != features.end())
            return percent * traverseTree(pCurTree->pFirst, features);
        else
            return percent * traverseTree(pCurTree->pSecond, features);
    }
    return percent;
}

//-------------------------------------------------------------------------
int main(int argc, const char* argv[])
{
    if (argc != 3)
    {
        log("Error: Usage %s [INPUT_FILE] [OUTPUT_FILE]\n", argv[0]);
        return 1;
    }

    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    unsigned N;
    fin >> N;

    TDecisionTree* pCurTree = NULL;
    for (unsigned n = 0; n < N; ++n)
    {
        unsigned L, l = 0;
        fin >> L;
        pCurTree = readTree(fin);
        char c;
        fin >> c;
        while (c == ' ' || c == ')' || c == '\n') fin >> c;
        fin.putback(c);

        fout << "Case #" << n+1 << ":" << endl;

        unsigned A;
        fin >> A;
        for (unsigned a = 0; a < A; ++a)
        {
            char animal[256];
            fin >> animal;
            unsigned nFeatures;
            fin >> nFeatures;
            vector<string> features;
            features.reserve(nFeatures);
            for (unsigned f = 0; f < nFeatures; ++f)
            {
                char feature[256];
                fin >> feature;
                features.push_back(feature);
            }

            fout.setf(ios_base::fixed);
            fout.precision(7);
            double val = traverseTree(pCurTree, features);
            fout << val << endl;
        }
    }

    fout.close();

    return 0;
}
