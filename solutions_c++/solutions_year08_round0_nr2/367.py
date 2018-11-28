#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
inline int c2i(char c){ return c - '0';}
int get_time(istream& cin){
    string tstr;
    cin >> tstr;
    return (c2i(tstr[0]) * 10 + c2i(tstr[1])) * 60 + c2i(tstr[3]) * 10 + c2i(tstr[4]);
}
bool cmp(const pair<int, pair<int, int> >& a, const pair<int, pair<int, int> >& b){
    return a.first < b.first || a.first == b.first && a.second.first + a.second.second > b.second.first + b.second.second;
}
vector< pair< int, pair<int, int> > > timetable;
int main(){
    //ifstream cin("B-large.in");
    //ofstream cout("out.txt");
    int ncase, T, NA, NB;
    cin >> ncase;
    for(int tcase = 1; tcase <= ncase; ++ tcase){
        cout << "Case #" << tcase << ": ";
        cin >> T >> NA >> NB;
        timetable.clear();
        for(int i = 0; i < NA; ++ i){
            timetable.push_back(make_pair(get_time(cin), make_pair(-1, 0)));
            timetable.push_back(make_pair(get_time(cin) + T, make_pair(0, 1)));
        }
        for(int i = 0; i < NB; ++ i){
            timetable.push_back(make_pair(get_time(cin), make_pair(0, -1)));
            timetable.push_back(make_pair(get_time(cin) + T, make_pair(1, 0)));
        }
        sort(timetable.begin(), timetable.end(), cmp);
        int A = 0, B = 0, CA = 0, CB = 0;
        for(vector< pair< int, pair<int, int> > >::iterator it = timetable.begin(); it != timetable.end(); ++ it){
            if (CA + it->second.first < 0) ++ A, ++ CA;
            if (CB + it->second.second < 0) ++ B, ++ CB;
            CA += it->second.first;
            CB += it->second.second;
        }
        cout << A << ' ' << B << endl;
    }
    return 0;
}
