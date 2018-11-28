#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
typedef pair<char, char> PC;

string displayVector(vector<char>& v){
    string s = "[";
    for (vector<char>::iterator it = v.begin(); it!=v.end(); it++){
        s += *it;
        s += ", ";
    }
    return s.substr(0,s.length()-2) + "]";
}

bool findAssoc(vector<pair<PC, char> >& a, char elem1, char elem2, char& res){
    for (vector<pair<PC, char> >::iterator it = a.begin(); it!= a.end(); it++){
        if (min((it->first).first,(it->first).second)==min(elem1,elem2)
            && max((it->first).first,(it->first).second)==max(elem1,elem2)){
            res = it->second;
            return true;
        }
    }
    return false;
}

bool findOppose(vector<PC>& o, vector<char>&v){
    char first = v[v.size()-1];
    for (vector<PC>::iterator it = o.begin(); it!= o.end(); it++){
        if (first == it->first){
            if (find(v.begin(), v.end()-1, it->second)!= v.end()-1)
                return true;
        }else if (first == it->second){
            if (find(v.begin(), v.end()-1, it->first)!= v.end()-1)
                return true;
        }
    }
    return false;
}

int main() {
    int t = 0;
    cin>>t;
    for (int i=0; i<t ; i++) {
        vector<char> inp,final;
        vector<pair<PC, char> > assoc;
        vector<PC> oppose;

        int t1, t2;
        cin>>t1;
        for (int j=0; j<t1; j++){
            string temp;
            cin>>temp;
            assoc.push_back(make_pair(make_pair(temp[0],temp[1]),temp[2]));
        }
        cin>>t2;
        for (int j=0; j<t2; j++){
            string temp;
            cin>>temp;
            oppose.push_back(make_pair(temp[0],temp[1]));
        }
        cin>>t1;
        for (int k=0; k<t1; k++){
            char tmp;
            cin>>tmp;
            final.push_back(tmp);
            if(final.size()>1){
                char res;
                int sz = final.size();
                if (findAssoc(assoc, final[sz-2], final[sz-1],res)){
                    final.resize(sz-2);
                    final.push_back(res);
                }else if(findOppose(oppose, final)){
                    vector<char> a;
                    swap(final, a);
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<displayVector(final)<<endl;
    }
    return 0;
}
