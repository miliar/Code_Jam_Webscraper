#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

class ElementList {
    vector<pair<pair<char,char>,char> > formulas;
    vector<pair<char,char> > opposed;
    vector<char> elements;
    
    void push(char c) {
        if(!elements.empty()) {
            for(vector<pair<pair<char,char>,char> >::iterator i=formulas.begin();i!=formulas.end();++i) {
                char other = '\0';
                if(i->first.first == c)
                    other = i->first.second;
                else if(i->first.second == c)
                    other = i->first.first;
                if(elements.back()==other) {
                    elements.pop_back();
                    elements.push_back(i->second);
                    return;
                }
            }
            for(vector<pair<char,char> >::iterator i=opposed.begin();i!=opposed.end();++i) {
                char other = '\0';
                if(i->first == c)
                    other = i->second;
                else if(i->second == c)
                    other = i->first;
                for(vector<char>::iterator j=elements.begin();j!=elements.end();++j) {
                    if(*j==other) {
                        elements.clear();
                        return;
                    }
                }
            }
        }
        elements.push_back(c);
    }
    
public:
    ElementList(string s) {
        stringstream ss(s);
        int c,d,n;
        string buf;
        ss >> c;
        if(c>0)
            formulas.reserve(c);
        for(int i=0;i<c;++i) {
            ss >> buf;
            formulas.push_back(pair<pair<char,char>,char>(pair<char,char>(buf[0],buf[1]),buf[2]));
        }
        ss >> d;
        if(d>0)
        opposed.reserve(d);
        for(int i=0;i<d;++i) {
            ss >> buf;
            opposed.push_back(pair<char,char>(buf[0],buf[1]));
        }
        ss >> n;
        ss >> buf;
        if(n>0)
        elements.reserve(n);
        for(int i=0;i<n;++i) {
            /*
            cout << "Adding " << buf[i] << " to [";
            for(vector<char>::iterator j=elements.begin();j!=elements.end();++j) {
                cout << *j;
                if(j+1 != elements.end())
                    cout << ", ";
            }
            cout << "]" << endl; */
            push(buf[i]);
        }
    }
    const vector<char>& Elements() { return elements; }
};

const int BUFSIZE = 1024;

int main() {
    int t;
    cin >> t;
    cin.ignore(20,'\n');
    char buf[BUFSIZE];
    for(int i=0;i<t;++i) {
        cin.getline(buf,BUFSIZE);
        ElementList el(buf);
        vector<char> list = el.Elements();
        cout << "Case #" << i+1 << ": [";
        for(vector<char>::iterator j=list.begin();j!=list.end();++j) {
            cout << *j;
            if(j+1 != list.end())
                cout << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}
