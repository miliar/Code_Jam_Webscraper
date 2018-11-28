/* Song Qiang
 */ 

#include <cmath>

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits>
#include <list>


using namespace std;

int
main(int argc, const char **argv)
{
    ifstream in(argv[1]);
        
    int T;
    in >> T;

    for (size_t t = 0; t < T; ++t)
    {
        vector<vector<char> > combine(26, vector<char>(26, '\0'));
        vector<vector<bool> > oppose(26, vector<bool>(26, false));

        int C;
        in >> C; 
        for (size_t i = 0; i < C; ++i)
        {
            string str;
            in >> str;
//            cerr << str << "\t" << str[0] - 65 << "\t" << str[1] - 65 << "\t" << str[2] << endl;
            combine[str[0] - 65][str[1] - 65] = str[2];
            combine[str[1] - 65][str[0] - 65] = str[2];
        }

/////
//        cerr << "check 1: "<< "OK" << endl;
/////


        int D;
        in >> D; 
        for (size_t i = 0; i < D; ++i)
        {
            string str;
            in >> str;
//            cerr << str << "\t" << str[0] - 65 << "\t" << str[1] - 65 << endl;
            oppose[str[0] - 65][str[1] - 65] = true;
            oppose[str[1] - 65][str[0] - 65] = true;
        }

/////
//        cerr << "check 2: "<< "OK" << endl;
/////

        list<char> elements;
        int N;
        in >> N; 
        for (size_t i = 0; i < N; ++i)
        {
            char ch;
            in >> ch;
//            cerr <<  ch << "\t" << ch - 65 << "\t";
            if (elements.size() > 0 && combine[ch - 65][elements.back() - 65] != '\0')
            {
//                cerr << elements.back() << ch << " --> " << combine[ch - 65][elements.back() - 65] << "\t";
                
                elements.back() = combine[ch - 65][elements.back() - 65];
//                cerr << elements.back() << endl;
            }
            else
                elements.push_back(ch);
            
            // char opposition
            list<char>::iterator itr;
            for (itr = elements.begin(); itr != elements.end(); itr++)
                if (oppose[*itr - 65][elements.back() - 65])
                {
                    elements.clear();
                    break;
                }
        }

        
        cout << "Case #" << t+1 << ": ";
        if (elements.size() == 0)
            cout << "[]" << endl;
        else
        {
            cout << "[";
            int n = elements.size();
            list<char>::iterator itr = elements.begin();
            for (size_t j = 0; j < n - 1; ++j)
            {
                cout << *itr << ", ";
                ++itr;
            }
            cout << elements.back() << "]"<< endl;
        }
    }
  
    return EXIT_SUCCESS;
}
