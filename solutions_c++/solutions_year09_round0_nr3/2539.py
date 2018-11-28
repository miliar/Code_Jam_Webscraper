#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>
#include <cstdio>

using namespace std;

typedef vector<int> liste;

const int longmax = 19;
const string motif = "welcome to code jam";

int gen(int position, int last_lettre, string mot, vector< liste> tab)
{
    //cout << "pos: " << position << " " << last_lettre << " mot:"<< mot << endl;
    int nb = 0;
    if(position < longmax)
    {
        for(int i = 0; i < tab[position].size(); i++)
        {
            if( position == 0 || last_lettre < tab[position][i] )
            {
                ostringstream m;
                m << tab[position][i];
                nb += gen(position+1, tab[position][i], mot + " " +  m.str(), tab);
            }
        }
    }
    else
    {
        //cout << "**" << mot << endl;
        return 1;
    }
    return nb;
}



int main(int argc, char** argv) {


    int N;
    cin >> N;
    //cin.clear();
    string tmp;
    getline(cin, tmp);
    
    string phrase = "welcom tdja";
    char cphrase[] = "welcom tdja";
    for (int i = 0; i < N; i++)
    {
        string in;
        getline(cin, in);
        //getline(cin, in);
        //cin >> in;
        //cout << "->" << in << "<-" << endl;

        
        map<char, liste> tab;

        int count = 0, cnt = 0;
        //cout << "size " <<  in.size() << endl ;
        for(int j = 0; j < in.size(); j++)
        {
            //if (phrase.find(in[j]))
            if ( strchr(cphrase, in[j]) )
            {
                tab[in[j]].push_back(j);
                //cout << "+" << j << ":" << in[j] << endl;
                cnt++;
            }


            //cout <<  in[j] << tab[in[j]].size() << endl;
        }

        //test
//        for (int j = 0; j < tab['e'].size(); j++)
//            cout << tab['e'].at(j) << endl;
//


        vector <liste> tab_final;
        for (int i = 0; i < motif.size(); i++)
        {
            tab_final.push_back(  tab[motif[i]] );
        }
        
        
        int res = gen(0, 0, "", tab_final);
	// Case #1: 0001
        //cout << "Case #" << i << ": " <<  res << endl;
	printf("Case #%d: %04d\n", i+1, res);
    }

    

    return (EXIT_SUCCESS);
}






//        for(int l1 = 0; l1 < tab['w'].size(); l1++)
//            for(int l2 = 0; l2 < tab['e'].size(); l2++)
//                for(int l3 = 0; l3 < tab['l'].size(); l3++)
//                    for(int l4 = 0; l4 < tab['c'].size(); l4++)
//                        for(int l5 = 0; l5 < tab['o'].size(); l5++)
//                            for(int l6 = 0; l6 < tab['m'].size(); l6++)
//                                for(int l7 = 0; l7 < tab['e'].size(); l7++)
//                                    for(int l8 = 0; l8 < tab[' '].size(); l8++)
//                                        for(int l9 = 0; l9 < tab['t'].size(); l9++)
//                                            for(int l10 = 0; l10 < tab['o'].size(); l10++)
//                                                for(int l11 = 0; l11 < tab[' '].size(); l11++)
//                                                    for(int l12 = 0; l12 < tab['c'].size(); l12++)
//                                                        for(int l13 = 0; l13 < tab['o'].size(); l13++)
//                                                            for(int l14 = 0; l14 < tab['d'].size(); l14++)
//                                                                for(int l15 = 0; l15 < tab['e'].size(); l15++)
//                                                                    for(int l16 = 0; l16 < tab[' '].size(); l16++)
//                                                                        for(int l17 = 0; l17 < tab['j'].size(); l17++)
//                                                                            for(int l18 = 0; l18 < tab['a'].size(); l18++)
//                                                                                for(int l19 = 0; l19 < tab['m'].size(); l19++)
//                                                                                {
//                                                                                    tab['w'].at(l1);
//                                                                                    count++;
//                                                                                }
//                                                                                    //int a =0;
