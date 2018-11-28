#include <iostream>
#include <map>
#include <list>
#include <set>
#include <utility>

using namespace std;

string implode(const string &glue, const list<char> &pieces);

int main()
{
    int t, c, d, n;
    map<pair<char, char>, char> combine_map;
    map<pair<char, char>, char>::iterator combine_map_it;
    map<char, set<char> > oppose_map;
    map<char, set<char> >::iterator oppose_map_it;
    list<char> curr_list;
    string buf;

    cin >> t;
    for (int z = 1; z <= t; z++) {
        combine_map.clear();
        oppose_map.clear();
        curr_list.clear();

        // combine
        cin >> c;
        for (int za = 0; za < c; za++) {
            cin >> buf;
            combine_map.insert(make_pair(make_pair(buf[0], buf[1]), buf[2]));
            combine_map.insert(make_pair(make_pair(buf[1], buf[0]), buf[2]));
        }
        // oppose
        cin >> d;
        for (int za = 0; za < d; za++) {
            cin >> buf;
            oppose_map[buf[0]].insert(buf[1]);
            oppose_map[buf[1]].insert(buf[0]);
        }
        cin >> n;
        cin >> buf;
        for (size_t i = 0; i < buf.size(); i++) {
            combine_map_it = combine_map.find(make_pair(curr_list.back(), buf[i]));
            if (combine_map_it != combine_map.end()) {
                curr_list.pop_back();
                curr_list.push_back(combine_map_it->second);
            } else {
                oppose_map_it = oppose_map.find(buf[i]);
                bool opposed = false;
                if (oppose_map_it != oppose_map.end()) {
                    for (list<char>::const_iterator it = curr_list.begin();
                            it != curr_list.end(); ++it) {
                        if (oppose_map_it->second.find(*it) != oppose_map_it->second.end()) {
                            curr_list.clear();
                            opposed = true;
                            break;
                        }
                    }
                }
                if (!opposed) {
                    curr_list.push_back(buf[i]);
                }
            }
        }
        // output
        cout << "Case #" << z << ": [" << implode(", ", curr_list) << "]" << endl;
    }
}

string implode(const string &glue, const list<char> &pieces)
{
    string a;
    int leng = pieces.size();
    int i = 0;
    for(list<char>::const_iterator it = pieces.begin();
            it != pieces.end();
            ++it, ++i)
    {
        a += *it;
        if (i < leng - 1)
            a += glue;
    }
    return a;
}
