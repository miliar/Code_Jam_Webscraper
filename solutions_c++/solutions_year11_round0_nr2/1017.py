#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for(int z = 1; z <= t; z++) {
        int convert[26][26];
        bool destroy[26][26];

        memset(convert, -1, sizeof convert);
        memset(destroy, 0, sizeof destroy);

        int c;
        cin >> c;
        for(int i = 0; i < c; i++) {
            string tmp;
            cin >> tmp;
            convert[tmp[0]-'A'][tmp[1]-'A'] = tmp[2]-'A';
            convert[tmp[1]-'A'][tmp[0]-'A'] = tmp[2]-'A';
        }

        int d;
        cin >> d;
        for(int i = 0; i < d; i++) {
            string tmp;
            cin >> tmp;
            destroy[tmp[0]-'A'][tmp[1]-'A'] = true;
            destroy[tmp[1]-'A'][tmp[0]-'A'] = true;
        }

        string elements, sz;
        cin >> sz >> elements;

        vector<int> list;
        for(unsigned int i = 0; i < elements.size(); i++) {
            list.push_back(elements[i] - 'A');

            while(list.size() >= 2 &&
                  convert[list[list.size()-1]][list[list.size()-2]] != -1) {
                list[list.size()-2] = convert[list[list.size()-1]][list[list.size()-2]];
                list.pop_back();
            }

            for(unsigned int i = 0; i < list.size(); i++)
                for(unsigned int j = i+1; j < list.size(); j++)
                    if(destroy[list[i]][list[j]])
                        list.clear();
        }

        cout << "Case #" << z << ": [";
        for(unsigned int i = 0; i < list.size(); i++) {
            if(i) cout << ", ";
            cout << (char)(list[i] + 'A');
        }
        cout << "]" << endl;
    }
}
