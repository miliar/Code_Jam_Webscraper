#include <map>
#include <deque>
#include <string>
#include <sstream>
#include <utility>
#include <iostream>
using namespace std;

template <typename K, typename V>
bool map_contains(const map<K,V> &m, const K &key)
{
    return m.find(key) != m.end();
}

bool deque_contains(const deque<char> &c, const char &key)
{
    deque<char>::const_iterator end= c.end();
    for (deque<char>::const_iterator it= c.begin(); it != end; ++it)
        if (*it == key) return true;
    return false;
}

string as_string(const deque<char> &d)
{
    if (d.size() == 0) return "[]";
    ostringstream sout;
    sout << "[";
    deque<char>::const_iterator end= d.end();
    deque<char>::const_iterator it= d.begin();
    sout << *it++;
    while (it != end) sout << ", " << *it++;
    sout << "]";
    return sout.str();
}

int main()
{
    istream &in= cin;
    ostream &out= cout;
    int t;
    in >> t;
    for (int i= 0; i < t; i++)
    {
        map<pair<char,char>,char> mappings;
        map<char,char> opposition;
        int c;
        for (in >> c; c > 0; c--)
        {
            string s;
            in >> s;
            mappings[make_pair(s[0], s[1])]= s[2];
            mappings[make_pair(s[1], s[0])]= s[2];
        }

        int d;
        for (in >> c; c > 0; c--)
        {
            string s;
            in >> s;
            opposition[s[0]]= s[1];
            opposition[s[1]]= s[0];
        }

        deque<char> result;
        in >> d;
        string elements;
        in >> elements;
        for (unsigned j= 0; j < elements.length(); j++)
        {
            char next= elements[j];
            if (result.size() > 0)
            {
                char prev= result.back();
                pair<char,char> key(next, prev);
                if (map_contains(mappings, key))
                {
                    result.pop_back();
                    next= mappings[key];
                }
                else 
                {
                    key.first= prev;
                    key.second= next;
                    if (map_contains(mappings, key))
                    {
                        result.pop_back();
                        next= mappings[key];
                    }
                }
            }
            if (map_contains(opposition, next) && deque_contains(result, opposition[next]))
            {
                result.clear();
            } else
            {
                result.push_back(next);
            }
        }
        out << "Case #" << (i+1) << ": " << as_string(result) << endl;
    }
    return 0;
}
