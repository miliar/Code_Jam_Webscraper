#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<iostream>
#include<string>
using namespace std;
struct nodo{
  string nombre;
  vector<int> hijos;
  nodo(){}
  nodo(string nom){
     nombre = nom;
  }
};

vector<nodo> nodos;


int insertaArbol(string line){
  line[0]='*';
  int pos = 1;
  int act = 0;
  int cnt = 0;
  int posF;
  int idx;
  string sub;
  
  //cout << "Tratamos de insertar " << line << endl;
  while (pos < line.size()){
    posF = line.find('/',pos);
    if (posF == string::npos){
      sub = line.substr(pos);
      pos = line.size();
    }
    else {
      sub = line.substr(pos,posF - pos);
      pos = posF + 1;
    }
    //cout << "token " << sub << endl;
    idx = -1;
    for (int i=0; i < nodos[act].hijos.size(); ++i){
      if (nodos[ nodos[act].hijos[i] ].nombre == sub) idx = nodos[act].hijos[i];
    }
    
    if (idx < 0){
      //cout << "no encontrado" << endl;
      nodos.push_back(nodo(sub));
      nodos[act].hijos.push_back(nodos.size() - 1);
      cnt++;
      act = nodos.size() - 1;
    }
    else {
      //cout << "encontrado" << endl;
      act = idx;
    }
  }
  return cnt;
}

int main(){
   int N,M;
   int runs;
   string line; 
  cin >> runs;
  for (int k=0; k < runs; ++k){
    cout << "Case #" << k + 1<<": ";
    nodos.clear();
    nodos.push_back(nodo(""));
    cin >> N >> M;
    getline(cin,line);
    for (int i=0; i < N; ++i){
	getline(cin,line);
	insertaArbol(line);
    }
    int cnt = 0;
    for (int i=0; i < M; ++i){
      getline(cin,line);
      cnt += insertaArbol(line);
    }
    cout << cnt << "\n";
  }
  return 0;
}