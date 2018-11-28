#include <iostream>
#include <list>
#include <vector>
#include <set>
#include <fstream>
#include <string>
#include <map>

using namespace std;


int main()
{
    //ofstream output ("B-small.out");
    ofstream output ("B-large.out");
    //ifstream input ("B-small-attempt3.in");
    ifstream input ("B-large.in");
    int t;

    input >> t;
    
    for (int i=0; i < t; i++)
    {
        list<char> s_list;
        vector<char> q_vect;
        set<string> o_set;
        map<string, char> c_map;
        int record[26];
        for (int j=0; j<26; j++)
            record[j] = 0;

        int c;
        input >> c;
        for (int j=0; j<c; j++)
        {
            string temp;
            input >> temp;
            string temp2;
            temp2.push_back(temp[0]);
            temp2.push_back(temp[1]);
            c_map[temp2] = temp[2];
            string temp3;
            temp3.push_back(temp[1]);
            temp3.push_back(temp[0]);
            c_map[temp3] = temp[2];
        }

        int d;
        input >> d;
        for (int j=0; j<d; j++)
        {
            string temp;
            input >> temp;
            o_set.insert(temp);
                    }

        int n;
        input >> n;
        {
            string temp;
            input >> temp;
            for (int j=0; j<temp.length(); j++)
            {
                s_list.push_back(temp[j]);
            }
        }

        output << "Case #"<<i+1<<": ";
        while(!s_list.empty())
        {
            char temp = s_list.front();
            s_list.pop_front();

            if ( q_vect.empty() )
            {
                q_vect.push_back(temp);
                record[temp-'A'] ++;
                continue;
            }
            char temp2 = q_vect.back();
            string temp_s;
            temp_s.push_back(temp);
            temp_s.push_back(temp2);
            map<string, char>::iterator it;
            it = c_map.find(temp_s);
            if ( it != c_map.end())
            {
                if (record[temp2-'A'] > 0)
                    record[temp2-'A'] --;
                q_vect.pop_back();
                q_vect.push_back(it->second);
                record[it->second - 'A'] ++;
                continue;
            }

            temp_s.clear();
            temp_s.push_back(temp2);
            temp_s.push_back(temp);
            it = c_map.find(temp_s);
            if ( it != c_map.end())
            {
                if (record[temp2-'A'] > 0)
                    record[temp2-'A'] --;
                q_vect.pop_back();
                q_vect.push_back(it->second);
                record[it->second - 'A'] ++;
                continue;
            }

            set<string>::iterator iit;
            bool found = false;
            for (iit = o_set.begin(); iit != o_set.end(); iit++)
            {
                if ( (*iit)[0] == temp && record[(*iit)[1] - 'A'] > 0)
                {
                    q_vect.clear();
                    for(int j=0; j<26; j++)
                    {
                        record[j] = 0;
                    }
                    found = true;
                    break;
                }

                if ( (*iit)[1] == temp && record[(*iit)[0] - 'A']  > 0 )
                {
                    q_vect.clear();
                    for(int j=0; j<26; j++)
                    {

                        record[j] = 0;
                    }
                    found = true;
                    break;
                }
            }

            if ( !found)
            {
                q_vect.push_back(temp);
                record[temp-'A'] ++;
            }
            
        }
        
        output << "[";
        for(int j = 0; j<q_vect.size(); j++)
        {
            if ( j==0)
            {
                
                output << q_vect[j];
                continue;
            }

            output <<", "<<q_vect[j];
        }
        output<<"]"<<endl;
    }
    return 0;
}

        
      
