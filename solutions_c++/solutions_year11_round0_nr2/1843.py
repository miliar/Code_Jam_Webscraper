/* 
 * File:   magicka.cc
 * Author: lewy
 *
 * Created on 7 maj 2011, 10:02
 */

#include <cstdio>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int hashuj(char a, char b){
  return 1000 * a + b;
}

void myErase(multiset<int> &set, int el){
  set.erase(set.find(el));
}

void clearTable(int tab[]){
  for(int i = 0; i < 1000; ++i){
    tab[i] = 0;
  }
}
int main()
{
  vector<int> wynik(1000);
  int d;
  scanf("%d", &d);
  for(int k = 1; k <= d; ++k){
    
    
    int tab[1000];
    clearTable(tab);
    
    multiset<int> op[300];
    map<int, char> tr;
    //multiset<int> l;
    vector<int> lista;
    
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i){
      string s;
      cin >> s;
      tr[hashuj(s[0], s[1])] = s[2];
      tr[hashuj(s[1], s[0])] = s[2];
    }
    int m;
    scanf("%d", &m);
    for(int i = 0; i < m; ++i){
      string s;
      cin >> s;
      op[s[0]].insert(s[1]);
      op[s[1]].insert(s[0]);
    }
    
    string in;
    int nic;
    cin >> nic;
    cin >> in;
    //cout << "oto wejscie: " << in << endl;
    for(int i = 0; i < in.size(); ++i){
      char c = in[i];
      
      if(lista.size() == 0){
        //l.insert(c);
        ++tab[c];
        lista.push_back(c);
        continue;
      }
      if(tr.count(hashuj(c, lista.back()))){
        char o = tr[hashuj(c, lista.back())];
        //myErase(l, lista.back());
        --tab[lista.back()];
        lista.pop_back();
        lista.push_back(o);
        //l.insert(o);
        ++tab[o];
        //cout <<  "wstawiam : " << o << " cos " << l.count('E') << endl;
      }
      else{
        bool res = false;
        for(multiset<int>::iterator v = op[c].begin(); v != op[c].end(); ++v){
          int el = (*v);
          if(tab[el]){
            res = true;
            break;
          }
        }
        //vector<int>::iterator it;
        /*it = set_intersection(l.begin(), l.end(), op[c].begin(), op[c].end(), 
                wynik.begin());
            */
        if(res){
          //l.clear();
          clearTable(tab);
          lista.clear();
        }
        else{
          lista.push_back(c);
          //l.insert(c);
          ++tab[c];
        }
      }
    }
    
    cout << "Case #" << k << ": [";
    for(int i = 0; i < lista.size(); ++i){
      if(i == 0)
        cout << (char)lista[i];
      else{
        cout << ", " << (char)lista[i];
      }      
    }
    cout << "]" << endl;
  }
  return 0;
}

