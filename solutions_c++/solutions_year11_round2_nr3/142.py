///@file main.cpp
///@author Marcus Henry Ewert
///@date 2011-05-07


#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

int colors[2100];

int maxcol;

struct Poly{
  void addindex(int i){
    indices.insert(i);
  }

  bool hasindex(int i){
    return indices.count(i) != 0;
  }

  Poly * split(int a, int b){
    if(a > b){
      int temp = b;
      b = a;
      a = temp;
    }
    Poly * p = new Poly();
    set<int>::iterator iter;
    set<int> keepers;
    for(iter = indices.begin(); iter != indices.end(); iter++){
      if(*iter >= a && *iter <= b){
        p->addindex(*iter);
      }
      if(! (*iter > a && *iter < b)){
        keepers.insert(*iter);
      }
    }
    indices.clear();
    for(iter = keepers.begin(); iter != keepers.end(); iter++){
      addindex(*iter);
    }
    return p;
  }

  int remainingColors(){
    int ret = 0;
    set<int>::iterator iter;
    char * c = new char[maxcol];
    for(int i= 0; i < maxcol; i++)
      c[i] = 1;
    for(iter = indices.begin(); iter != indices.end(); iter++){
      if(colors[*iter] != 0){
        c[colors[*iter]-1] = 0;
      }
    }
    for(int i= 0; i < maxcol; i++)
      ret+=c[i];
    delete [] c;
    return ret;
  }

  int size(){
    return indices.size();
  }

  int freecolor(){
    int i = 1;
    while(true){
      char c = false;
      set<int>::iterator iter;
      for(iter = indices.begin(); iter != indices.end(); iter++){
        if(colors[*iter] == i){
          c= true;
          break;
        }
      }
      if(!c)
        return i;
      i++;
      if(maxcol < i)
        return 1;
    }
    return 0;
  }

  void color1(){
    set<int>::iterator iter;
    for(iter = indices.begin(); iter != indices.end(); iter++){
      if(colors[*iter] == 0){
        colors[*iter] = freecolor();
        return;
      }
    }
  }

  set<int> indices;

};

int main(int argc, char ** argv){
  int trials;
  cin >> trials;
  for(int trial = 1; trial <= trials; trial++){
    for(int i = 0; i < 2100; i++){
      colors[i] = 0;
    }
    int n, m;
    cin >> n;
    cin >> m;
    vector<Poly *> polies;
    Poly * p = new Poly();
    for(int i=1; i <=n; i++){
      p->addindex(i);
    }
    polies.push_back(p);

    vector<int> us;
    for(int i = 0; i < m; i++){
      int u;
      cin >> u;
      us.push_back(u);
    }
    for(int i = 0; i < m; i++){
      int v;
      cin >> v;
      int u = us[i];
      vector<Poly *>::iterator piter;
      for(piter = polies.begin(); piter != polies.end(); piter++){
        Poly * p = *piter;
        if(p->hasindex(u) && p->hasindex(v)){
          polies.push_back(p->split(u,v));
          break;
        }
      }
    }

    
    int min = n+1;
    vector<Poly *>::iterator piter;
    for(piter = polies.begin(); piter != polies.end(); piter++){
      Poly * p = *piter;
      if(p->size() < min)
        min = p->size();
    }
    maxcol = min;

    for(int i = 0; i < n; i++){
      int mincs = n+1;
      Poly * minp = NULL;
      vector<Poly *>::iterator piter;
      for(piter = polies.begin(); piter != polies.end(); piter++){
        Poly * p = *piter;
        int prc = p->remainingColors();
        if(prc != 0 && prc < mincs){
          minp = p;
          mincs = prc;
        }
      }
      if(minp == 0){
        for(int i = 1; i <= n; i++){
          if(colors[i] == 0)
            colors[i] =1;
        }
        break;
      }else{
        minp->color1();
      }
    }
   
    cout << "Case #" << trial << ": " << min << endl;
    cout << colors[1];
    for(int i = 2; i <= n; i++){
      cout << " " << colors[i];
    }
    cout << endl;

    for(piter = polies.begin(); piter != polies.end(); piter++){
      Poly * p = *piter;
      delete p;
    }
  }
}
