/*
 * File:   main.cpp
 * Author: Sagar
 *
 * Created on May 7, 2011, 11:22 AM
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

/*
 *
 */
int main(int argc, char** argv) {
    int T,C,D,N;

    cin >> T;
    map <pair<char,char>, char> combine;
    map <pair<char,char>, char>::iterator c_itr;

    vector <pair <char, char> > oppose;
    vector <pair<char, char> >::iterator o_itr;
    string str;

    for(int index = 1; index <= T ;index++)
    {
        cin >> C;
        for(int i=0;i<C;i++)
        {
            string s;
            cin >> s;
            combine.insert(pair <pair<char,char>, char> (pair<char,char>(s[0],s[1]), s[2]));
            combine.insert(pair <pair<char,char>, char> (pair<char,char>(s[1],s[0]), s[2]));
        }
        cin >> D;
        for(int i=0;i<D;i++)
        {
            string s;
            cin >> s;
            oppose.push_back(pair<char,char>(s[0],s[1]));
            oppose.push_back(pair<char,char>(s[1],s[0]));
        }
        cin >> N;
        cin >> str; //String
        vector<char> result;
        for(int i=0;i<N;i++)
        {
            result.push_back(str[i]);
            c_itr = combine.find(make_pair<char,char>(*(result.end()-1),*(result.end()-2)));
            if(c_itr != combine.end())
            {
                result.erase(result.end()-1);
                result.erase(result.end()-1);
                result.push_back((*c_itr).second);
            }
            else {
                for(int j=0;j<result.size()-1;j++){
                    o_itr = find(oppose.begin(),oppose.end(),make_pair<char,char>(result[j], result[result.size()-1]));
                    if(o_itr != oppose.end()){
                        result.clear();
                        break;
                    }
                }
            }
               
        }

        cout << "Case #" << index << ": [";
        for(int i=0;i<result.size();i++) {
            cout << result[i];
            if(i+1 < result.size())
                cout << ", ";
        }
        cout << "]\n";
        combine.clear();
        oppose.clear();
        result.clear();
    }
    return 0;
}

