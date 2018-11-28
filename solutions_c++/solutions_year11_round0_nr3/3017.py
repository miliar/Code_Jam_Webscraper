#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

vector<int> values;
int n;
long long maxim = -1;

void rec(int a, int b, long long tvalue, int pos, int ct){
    if (pos == n){
        if ((a^b)==0 and tvalue > maxim and tvalue > 0 and ct > 0){
            maxim = tvalue;
        }
        return;
    }
    rec((a^(values[pos])), b, tvalue+values[pos], pos+1, ct);
    rec(a, (b^(values[pos])), tvalue, pos+1, ct+1);
}

int main(){
    ofstream fout ("out1.out");
    int t;
    cin >> t;
    for (int caso = 1; caso <= t; caso++){
        maxim = -1;
        cin >> n;
        values = vector<int> (n);
        for (int i = 0; i < n; i++) cin >> values[i];
        rec(0,0,0,0, 0);
        fout << "Case #" << caso << ": ";
        if (maxim == -1) fout << "NO";
        else fout << maxim;
        fout << endl;
    }
}
