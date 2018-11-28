#include <iostream>
#include <string>
#include <vector>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

//*
#include <fstream>
fstream fin ("B-large.in",ios::in);
fstream fout ("output.txt", ios::out);
#define cin fin
#define cout fout
//*/
void ProcessOppose(vector<char> & vec, char ch1,char ch2)
{
    bool bFind1 = false, bFind2 = false;
    for(int i=0; i<vec.size();i++)
        if(vec.at(i) == ch1)
            bFind1 = true;

    for(int i=0; i<vec.size();i++)
        if(vec.at(i) == ch2)
            bFind2= true;

    if(bFind1 == true && bFind2 == true)
        vec.clear();
}
void ProcessCombine(vector<char> & vec, char ch1, char ch2, char combined)
{
    int vecLength = vec.size();
    if(vecLength < 2)
        return;
    if((vec.at(vecLength-1) == ch1 && vec.at(vecLength - 2) == ch2)
        ||(vec.at(vecLength-2) == ch1 && vec.at(vecLength - 1) == ch2))
        {
            vec.pop_back();
            vec.pop_back();
            vec.push_back(combined);
        }
}
void ProcessOppose(vector<char> & vec, string str)
{
    ProcessOppose(vec, str[0], str[1]);
}
void ProcessCombine(vector<char> & vec, string str)
{
    ProcessCombine(vec, str.c_str()[0], str.c_str()[1], str.c_str()[2]);
}

template <class T>
void PrintVector(vector<T> vec)
{
    for(int i=0; i<vec.size();i++)
    {
        cout << vec.at(i) ;
        if(i!=vec.size()-1)
            cout <<", ";
    }

}

//void test()
//{
//    vector<char> vec;
//    vec.push_back('A');
//    vec.push_back('B');
//    vec.push_back('C');
//
//    //ProcessCombine(vec, 'B', 'C', 'D');
//    //PrintVector(vec);
//
//    ProcessOppose(vec, 'A', 'C');
//    PrintVector(vec);
//}



int main()
{

    //test();
    int datanum;
    cin >> datanum;
    string nouse;
    getline(cin, nouse);

    for(int m=0; m<datanum; m++)
    {
        string line;
        getline(cin, line);

        istringstream in(line);

        int combineNum;
        in >> combineNum;
        //cout <<"combine:" <<combineNum<<endl;
        vector<string> combines;
        for(int i=0; i<combineNum; i++)
        {
            string combine;
            in >> combine;
            combines.push_back(combine);
        }

        int opposeNum;
        in >> opposeNum;
        //cout <<"oppose:"<< opposeNum <<endl;
        vector<string> opposes;
        for(int i=0; i<opposeNum; i++)
        {
            string oppose;
            in >> oppose;
            opposes.push_back(oppose);
        }

        int charNum;
        vector<char> buffer;
        in >> charNum;
        //cout <<"charNum:" << charNum <<endl;
        for(int i=0; i<charNum; i++)
        {
            char ch;
            in >> ch;
            buffer.push_back(ch);

            // process combine
            for(int j=0; j<combineNum; j++)
            {
                ProcessCombine(buffer, combines[j]);
            }

            for(int j=0; j<opposeNum; j++)
            {
                ProcessOppose(buffer, opposes[j]);
            }
        }


        cout <<"Case #" << m+1 << ": [";
        PrintVector(buffer);
        cout << "]" << endl;
    }


    return 0;
}



