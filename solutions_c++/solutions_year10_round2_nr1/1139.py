#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
  int t, n, m, creados;
  string dir;
  cin >> t;
  for(int i=1; i<=t; i++) {
    cin >> n >> m;
    creados = 0;
    set< string > dirs;

    for(int d=1; d<=n; d++) {
      cin >> dir;
      //      cout << "actual: " << dir << endl;
      dirs.insert(dir);
    }

    for(int d=1; d<=m; d++) {
      cin >> dir;
      //      cout << "nuevo: " << dir << endl;
      string subdir = "/";
      string::iterator c = dir.begin();
      c++;
      for(; c<dir.end(); c++) {
	if(*c  == '/') {
	  if(dirs.count(subdir) == 0) {
	    dirs.insert(subdir);
	    //	    cout << "crear: " << subdir << endl;
	    creados++;
	  }
	}
	subdir.push_back(*c);
      }

      if(subdir != "/") {
	  if(dirs.count(subdir) == 0) {
	    dirs.insert(subdir);
	    //	    cout << "crear: " << subdir << endl;
	    creados++;
	  }
      }


    }
    cout << "Case #" << i << ": " << creados << endl;
  }
  return 0;
}

/*
para crear a,b,c hay que crear a y a/b 

Crear( d1..dn)
  cant = 0
  para i de 1 a n
     si no existe d1..di
       cant++
       agregar d1...di

*/


