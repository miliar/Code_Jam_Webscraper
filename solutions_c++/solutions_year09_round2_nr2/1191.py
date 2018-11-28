#include <iostream>
#include <string>
#include <fstream>
using namespace std;

#define LL long long
string in;
LL i,j,n,T;

ifstream fin("in.txt");
ofstream fout("out.txt");

void next(string &a) {
     if (a.size() < 2) {
        a.insert(a.begin() + 1,'0');
        return;
        }
     
     for (LL i=a.size()-2;i>=0;i--) {
         sort(a.begin() + i + 1, a.end());
         for (LL j=i+1;j<a.size();j++)
             if (a[i] < a[j] && (a[j] != '0' || i)) {
                swap( a[i], a[j] );
                sort(a.begin() + i + 1, a.end());      
                return;
                }
         }
     LL k;
     sort(a.begin(),a.end());
     if (a[0] == '0')
        for (k=1;k<a.size();k++)
            if (a[k] != '0') {
               swap(a[0],a[k]);
               break;
               }
     a.insert(a.begin() + 1,'0');
     }

int main() {
    fin >> T;
    
    for (LL t=1;t<=T;t++) {
        fin >> in;
        cout << "Case #" << t << ": " << in << endl;
        next(in);
        fout << "Case #" << t << ": " << in << endl;
        }
    cout << "Gotovo!" << endl;
    system("pause");
}
