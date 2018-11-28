#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <list>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int ncases;
  scanf("%d\n", &ncases);
  vector<bool> is_base(300,0);
  is_base['Q'] = 1;
  is_base['W'] = 1;
  is_base['E'] = 1;
  is_base['R'] = 1;
  is_base['A'] = 1;
  is_base['S'] = 1;
  is_base['D'] = 1;
  is_base['F'] = 1;


  for (int j = 0; j < ncases; ++j) {
    vector<int> is_in(300,0);
    map<char, map<char, char> > combine;
    map <char, list<char> > oppose;
    int temp;
    scanf ("%d ", &temp);
    for (int i = 0; i < temp; ++i) {
      char a, b, c;
      scanf("%c%c%c ", &a, &b, &c);
      combine[a][b] = c;
      combine[b][a] = c;
    }
    scanf ("%d ", &temp);
    for (int i = 0; i < temp; ++i) {
      char a, b, c;
      scanf("%c%c ", &a, &b);
      oppose[a].push_back(b);
      oppose[b].push_back(a);
    }
    scanf ("%d ", &temp);
    list<char> output;
    char previous = 'z';
    for (int i = 0; i < temp; ++i) {
      char atual;
      scanf("%c", &atual);
      if (!is_base[atual]) {
        previous = atual;
        output.push_back(atual);
        continue;
      }
      if (combine[atual].count(previous) > 0) {
        is_in[previous]--;
        output.pop_back();
        output.push_back(combine[atual][previous]);
        previous = combine[atual][previous];
      }
      else { 
        output.push_back(atual);
        previous = atual;
        is_in[atual]++;
        list<char>::iterator it;
        for (it = oppose[atual].begin(); it != oppose[atual].end(); ++it) {
          if (is_in[*it] > 0) {
            output.clear();
            previous = 'z';
            is_in['Q'] = 0;
            is_in['W'] = 0;
            is_in['E'] = 0;
            is_in['R'] = 0;
            is_in['A'] = 0;
            is_in['S'] = 0;
            is_in['D'] = 0;
            is_in['F'] = 0;
          }
        }
      }

      /*cout<<" TO NO "<<atual<<": ";
      list<char>::iterator ae;
      for (ae = output.begin(); ae != output.end(); ++ae) {
        cout<< *ae<<" ";
      }
      cout<<endl;*/

    }
    string saida;
    list<char>::iterator it;
    for (it = output.begin(); it != output.end(); ++it) {
      saida += *it;
      saida += ", ";
    }
    saida = saida.substr(0, saida.length() - 2);
    printf("Case #%d: [%s]", j + 1, saida.c_str());
    cout<<endl;
  }
}
