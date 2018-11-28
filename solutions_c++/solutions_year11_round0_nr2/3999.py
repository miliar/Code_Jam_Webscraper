#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream in;
	string filename;
    getline(cin, filename);
    in.open(filename.c_str());
    
    ofstream out;
    out.open("output.txt");

    int t, c, d, n;
    in >> t;
    for(int i = 0; i < t; i++) {
        in >> c;
        map<string, char> combinations;
        string mix;
        for(int j = 0; j < c; j++) {
            in >> mix;
            char a = mix[0];
            char b = mix[1];
            char c = mix[2];
            string ab;
            ab += a; ab += b;
            string ba;
            ba += b; ba += a;
            
            combinations[ab] = c;
            combinations[ba] = c;
        }

        in >> d;
        vector<string> oppose;
        string opp;
        for(int j = 0; j < d; j++) {
            in >> opp;
            string other;
            other += opp[1];
            other += opp[0];
            oppose.push_back(opp);
            oppose.push_back(other);
        }

        in >> n;
        string elements;
        in >> elements;
        char prev;
        vector<char> result;
        for(int j = 0; j < n; j++) {
            if(!result.empty()) {
                string two;
                two += prev;
                two += elements[j];
                map<string, char>::iterator it = combinations.find(two);
                vector<string>::iterator it_op = find(oppose.begin(), oppose.end(), two);
                bool is_opp = false;
                for(int woo = 0; woo < result.size(); woo++) {
                    string ugh;
                    ugh += result[woo];
                    ugh += elements[j];
                    if(find(oppose.begin(), oppose.end(), ugh) != oppose.end())
                        is_opp = true;
                }

                if(it == combinations.end()) {
                    if(!is_opp) {
                        result.push_back(elements[j]);
                        prev = elements[j];
                    }
                    else
                        result.clear();
                }
                else {
                    result.pop_back();
                    result.push_back(it->second);
                    prev = it->second;
                }
            }
            else {
                result.push_back(elements[j]);
                prev = elements[j];
            }
        }
        ostringstream oss;
        oss << "Case #" << i+1 << ": ";
        if(result.empty())
            oss << "[]" << endl;
        else {
            string res;
            res += result[0];
            for(int k = 1; k < result.size(); k++) {
                res += ", ";
                res += result[k];
            }
            oss << "[" << res << "]" << endl;
        }
        out << oss.str();
    }
    in.close();
    out.close();
	return 0;
}
