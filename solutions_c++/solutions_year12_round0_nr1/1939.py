#include <iostream>
#include <fstream>
#include <map>
#include <set>

using namespace std;

typedef map<char, char> Rmap;

Rmap rmap;

void buildRmap() {
  char from[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
      "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
      "de kr kd eoya kw aej tysr re ujdr lkgc jv"
      "y qeez";
  char to[] = "our language is impossible to understand"
      "there are twenty six factorial possibilities"
      "so it is okay if you want to just give up"
      "a zooq";
  char *cf = from;
  char *ct = to;

  while (*cf != '\0') {
    rmap[*cf] = *ct;
    cf++;
    ct++;
  }
}

void run(istream& in, ostream& ou, int i) {
  char buf[110];
  char *c = buf;
  in.getline(buf, 110);
  ou << "Case #" << i <<": ";
  while (*c != '\0') {
    ou << rmap[*c];
    c++;
  }
  ou<<endl;
}

int main(int argc, char** argv) {
  buildRmap();

  ifstream in(argv[1]);
  // ofstream ou(argv[2]);

  int cases;
  in >> cases;

  // discard the 1st line.
  char buf[110];
  in.getline(buf, 110);

  for (int i = 0; i < cases; i++) {
    run(in, cout, i+1);
  }
  // ou.close();
}
