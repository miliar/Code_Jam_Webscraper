#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

struct Node {
   double prob;
   string feature;
   Node *si;
   Node *no;
};

void llegir_arbre(Node &n) {
   char c;
   cin >> c;
   cin >> n.prob;
//    cerr << "nou node amb probabilitat " << n.prob << endl;
   if (n.prob == 0.0)
      return;
   cin >> c;
   if (c == ')') {
      n.feature = "";
      return;
   }
   n.feature = "";
   n.feature += c;
   while (cin.peek() >= 'a' and cin.peek() <= 'z') {
      cin >> c;
      n.feature += c;
   }
//    cerr << "i amb feature " << n.feature << endl;
   n.si = new Node;
   llegir_arbre(*n.si);
   n.no = new Node;
   llegir_arbre(*n.no);
   cin >> c;
}

set<string> qualitats;

double prob(Node &n, double porto) {
   porto *= n.prob;
   if (n.feature == "")
      return porto;
   if (qualitats.find(n.feature) != qualitats.end())
      return prob(*n.si, porto);
   return prob(*n.no, porto);
}

int main() {
   cout.setf(ios::fixed);
   cout.precision(7);
   int t;
   cin >> t;
   for (int tt=1; tt<=t; ++tt) {
      cout << "Case #" << tt << ":" << endl;
      int N;
      cin >> N;
      Node arbre;
      llegir_arbre(arbre);
      cin >> N;
      for (int i=0; i<N; ++i) {
         string nom;
         cin >> nom;
         int n;
         cin >> n;
         qualitats.clear();
         string s;
         for (int i=0; i<n; ++i) {
            cin >> s;
            qualitats.insert(s);
         }
         cout << prob(arbre, 1.0) << endl;
      }
   }
}