#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

struct chpair
{
    chpair(char ch1, char ch2): c1(ch1), c2(ch2){}
    char c1, c2;
    bool operator<(const chpair& arg) const
    {
        return arg.c1 == c1 ? c2 < arg.c2 : c1 < arg.c1;
    }
};

struct wlist {
    map<chpair, char> comb;
    map<char, set<char> > opp;
    vector<char> lst;
    map<char, int> cnt;
    void put(char next);
    void apply(char next);
    void clear(void);
    void pop(void);
    string print(void);
};

void wlist::put(char next)
{
    lst.push_back(next);
    ++(cnt[next]);
}

void wlist::apply(char next)
{
    if(lst.size() == 0){
        put(next);
        return;
    }
    char ch = lst[lst.size()-1];
    if(comb.find(chpair(next, ch))!=comb.end()){
        pop();
        put(comb[chpair(next, ch)]);
        return;
    }
    if(opp.find(next)!=opp.end()){
        for(set<char>::iterator i = opp[next].begin(); i != opp[next].end();++i){
		    for(size_t j = 0; j < lst.size(); ++j)
    		{
    			if(lst[j]==*i) {
	                clear();
    	            return;
				}
            }
        }
    }
    put(next);
}

void wlist::clear(void)
{
    lst.clear();
    cnt.clear();
}

void wlist::pop(void)
{
    ++(cnt[lst[lst.size()-1]]);
    lst.pop_back();
}

string wlist::print(void)
{
    string ret = "[";
    for(size_t i = 0; i < lst.size(); ++i)
    {
        ret += lst[i];
        if(i != lst.size() - 1) {
            ret += ", ";
        }
    }
    ret += "]";
    return ret;
}

void debprint(wlist& lst)
{
}

void TC(int T)
{
    wlist lst;
    int N = 0, C = 0, D = 0;
    cin >> C;
    for(int i = 0; i < C; ++i) {
        char c1, c2, c3;
        cin >> c1 >> c2 >> c3;
        lst.comb[chpair(c1, c2)] = c3;
        lst.comb[chpair(c2, c1)] = c3;
    }
    cin >> D;
    for(int i = 0; i < D; ++i) {
        char c1, c2;
        cin >> c1 >> c2;
        lst.opp[c1].insert(c2);
        lst.opp[c2].insert(c1);
    }
    cin >> N;
    for(int i = 0; i < N; ++i) {
        char ch;
        cin >> ch;
        lst.apply(ch);
    }
    cout << "Case #" << (T + 1) << ": " << lst.print() << endl;
}

int main(int argc, char **argv)
{
    int N = 0;
    cin >> N;
    for(int i = 0; i < N; ++i) {
        TC(i);
    }
    return 0;
}
