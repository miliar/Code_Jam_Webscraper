#include <iostream>
#include <set>
using namespace std;

int C;
int N;
int Q;
int casee;
int switches;
set<string> used;

int main() {
   string s;
   cin >> C;
   casee = 1;
   while (C--) {
     cin >> N;
     getline(cin,s);
     
     int n(N);
     while (n--) {
       getline(cin,s);
     }
       
     switches = 0;	     
     used.clear();
     
     cin >> Q;
     getline(cin,s);
     
     int q(Q);
     while (q--) {
       getline(cin,s);
       if (used.size() == N-1 && used.find(s)==used.end()) {
         switches ++;
	 used.clear();
       }
       used.insert(s);       
     }
     
    cout<<"Case #"<<casee<<": "<<switches<<endl;  
    casee++;     
   }
   return 0;
} 

