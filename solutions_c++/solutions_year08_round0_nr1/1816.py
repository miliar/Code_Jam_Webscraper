#include <iostream>
#include <fstream>
#include <cstring>
#include <map>

using namespace std;

int case_N, engine_S, quiry_Q, switch_num, true_flag;
string qry_name[1000], sTmp;
map<string,bool> eng_flag;

ifstream fin;
ofstream fout;

int main()
{
    //fin.open("A.in");
    fin.open("A-large.in");
    fout.open("A-large.out");
    
    fin >> case_N;
    for (int n = 1; n <= case_N; ++n)
    {
        /*
         *  INPUT
         */
        eng_flag.clear();
        fin >> engine_S;
        getline(fin, sTmp, '\n');
        for (int i = 0; i < engine_S; ++i) 
        {
            getline(fin, sTmp,'\n');
            eng_flag.insert(make_pair(sTmp, true));
        }
        fin >> quiry_Q;
        getline(fin, sTmp, '\n');
        for (int i = 0; i < quiry_Q; ++i)  getline(fin, qry_name[quiry_Q -1 - i],'\n');
        
        /*
         *  OUTPUT
         */
        switch_num = 0;
        true_flag = engine_S;
        sTmp = eng_flag.begin()->first;
        //fout << "#0 choice: " << sTmp << endl;
        for (int i = 0; i < quiry_Q; ++i)
        {
            //fout << "Encounter :" << qry_name[i] << endl;
            if (qry_name[i] == sTmp)
            {
                true_flag--;
                eng_flag[sTmp] = false;
                if (true_flag > 0) 
                {
                    map<string, bool>::iterator iter = eng_flag.begin();
                    while (iter->second == false) iter++;
                    sTmp = iter->first;
                    //fout << "#1 choice: " << sTmp << endl;
                } else {
                    switch_num++;
                    map<string, bool>::iterator iter;
                    for(iter = eng_flag.begin(); iter != eng_flag.end(); ++iter) {
                             if (iter->first != sTmp) iter->second = true;
                    } 
                    true_flag = engine_S - 1;
                    
                    iter = eng_flag.begin();
                    while (iter->first == sTmp) iter++;
                    sTmp = iter->first;
                    //fout << "#2 choice: " << sTmp << endl;
                }
            } else {
                if (eng_flag[qry_name[i]] == true) {
                    //fout << qry_name[i] << " turns false" << endl;
                    eng_flag[qry_name[i]] = false;
                    true_flag--;
                }
            }
        }
        fout << "Case #" << n << ": " << switch_num << endl;
    }    
    fin.close();
    fout.close();
    return 0;
} 
