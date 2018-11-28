#include<iostream>
#include<conio.h>
#include<fstream>
#include<sstream>
#include<string>
#include<queue>
#include<math.h>

using namespace std;

#define __int64 long long

template <class Item>
string toStr(Item x) { stringstream m; m << x; return m.str(); }
/*void stringSplit(string str, string delim, vector<string> &results) {
                   int cutAt;
                   while( (cutAt = str.find_first_of(delim)) != str.npos )
                   {
                    if(cutAt > 0)
                    {
                             results.push_back(str.substr(0,cutAt));
                    }
                    str = str.substr(cutAt+1);
                   }
                   if(str.length() > 0)
                    {
                    results.push_back(str);
                    }
}*/
     
int main() {
    ifstream in("A-Small.in");
    ofstream out("A-Small.out");
    int cases = 0;
    in >> cases;
    for (int i=0; i<cases; i++) {
        __int64 N;
        string line;
        in >> N;
        vector<__int64> b1;
        vector<__int64> b2;
        for(int j=0; j<N; j++) {
                __int64 w1, w2;
                in >> w1 >> w2;
                //cout << w1 << ", " << w2 << endl;
                b1.push_back(w1); b2.push_back(w2);
        }
        int inter=0;
        for(int j=0; j<b1.size(); j++) {
                if(b1[j] != b2[j]) {
                       //cout << "Checking: " << b1[j] << ", " << b2[j] << endl;
                       for(int k=0; k<b1.size(); k++) {
                               if(j!=k) {
                                     //cout << "Checking for: " << b1[k] << ", " << b2[k] << endl;                                            
                                     if((b1[j]>b1[k] && b2[k]>b2[j]) || (b1[j]<b1[k] && b2[k]<b2[j]))
                                                    ++inter;
                               }
                       }
                       b1.erase (b1.begin()+j);
                       b2.erase (b2.begin()+j);
                }
        }
        out << "Case #" << i+1 << ": " << (inter) << endl;
        //cout << inter << endl;
    }
    //getch();
    out.close();
    in.close();
    return 0;
}
