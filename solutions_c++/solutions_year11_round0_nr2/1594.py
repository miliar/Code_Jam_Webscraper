#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
using namespace std;

class List{
public:
    List(const string& s, const set< pair<char, char> > &_os,
         const map< pair<char, char>, char > &_cm):
        str(s), oppo_pair(_os), comb_trip(_cm) {}
    
    bool checkOpps(char a, char b){
        return oppo_pair.find(make_pair(a,b)) != oppo_pair.end() ||
            oppo_pair.find(make_pair(b,a)) != oppo_pair.end();
    }
    
    bool checkComb(char a, char b, char& c){
        map< pair<char, char>, char>::const_iterator im1 = comb_trip.find(make_pair(a,b));
        map< pair<char, char>, char>::const_iterator im2 = comb_trip.find(make_pair(a,b));

        if(im1 != comb_trip.end()) { c = im1->second; return true;}
        if(im2 != comb_trip.end()) { c = im2->second; return true;}
        return false;
    }
    

    void invoke(){
        for(size_t i=0; i<str.length(); ++i){
            res.push_back(str[i]);
            int len = res.length();
            if(len <=1) continue;
            char a = res[len-2];
            char b = res[len-1];
            char c;
            if(checkComb(a, b, c)){
                res[len-2] = c;
                res.erase(len-1, 1);
                //                cout << "com: " << a << ' '<<b <<' '<<c << "  " << res << endl;
            }
            for(size_t i=0; i<res.length(); ++i){
                if(checkOpps(res[i], res[res.length()-1])){
                    //res = res.substr(0, i);
                    res.clear();
                    //      cout <<"clr : " << res << endl;
                    break;
                }
            }
        }
        //        cout <<"Res:" <<  res << endl;
    }

    friend ostream& operator << (ostream& os, const List&);
private:
    string res;
    const string& str;
    const set< pair<char, char> >& oppo_pair;
    const map< pair<char, char>, char>& comb_trip;
};

ostream& operator <<(ostream& os, const List& l){
    os << '[';    
    for(int i=0; i<(int)l.res.length()-1; ++i){
        os << l.res[i] <<", ";
    }
    if(l.res.length() !=0) os<<l.res[l.res.length()-1];
    os << ']';
}

int main(int argc, char** argv)
{
    if(argc < 3) {
        cerr << "Usage: ./a input-file-name output-file-name" << endl;
        return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int case_num;
    fin >> case_num;
    for(int k=0; k<case_num; ++k){
        map< pair<char, char>, char> comb_mp;
        set< pair<char, char> > oppo_set;

        int comb_num, oppo_num, str_len;
        fin >> comb_num;
        for(int i=0; i<comb_num; ++i){
            char a, b, c;
            fin >> a >> b >> c;
            comb_mp[make_pair(a,b)] = c;
            comb_mp[make_pair(b,a)] = c;
        }
        fin >> oppo_num;
        for(int i=0; i<oppo_num; ++i){
            char a, b;
            fin >> a >> b;
            oppo_set.insert(make_pair(a,b));
            oppo_set.insert(make_pair(b,a));
        }
        string str;
        fin >> str_len >> str;

        List l(str, oppo_set, comb_mp);
        l.invoke();
        fout << "Case #" << k+1 <<": " << l << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
