#include <iostream>
#include <vector>
using namespace std;
int n;
vector < pair <int, int> > line;
void solve(int test){
    line.erase(line.begin(), line.end());
    int x, y;
    cin >> n;
    for ( int i = 0; i < n; ++i ){
        cin >> x >> y;
        line.push_back(make_pair(x, y));
    }
    int rez = 0;
    for ( int i = 0; i < n; ++i )
        for ( int j = i + 1; j < n; ++j )
            if ( line[i].first < line[j].first && line[i].second > line[j].second ) ++rez;
            else if ( line[i].first > line[j].first && line[i].second < line[j].second ) ++rez;
    cout << "Case #" << test << ": " << rez  << endl;
}
int main(){
    int t;
    cin >> t;
    for ( int i = 1; i <= t; ++i )
    solve(i);
}
