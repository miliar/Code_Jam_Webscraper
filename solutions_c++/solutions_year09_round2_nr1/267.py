#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;

int l, lpos, cpos;
char line[105][100];
set<string> st;

void check_pos() {
  if (cpos>=strlen(line[lpos])) {
    cpos = 0;
    lpos++;
  }
}

char my_getc() {
  check_pos();
  return line[lpos][cpos++];
}

double my_getf() {
  double d;
  check_pos();
  sscanf(line[lpos] + cpos, "%lf", &d);
  while (line[lpos][cpos]!='0') cpos++;
  while (isdigit(line[lpos][cpos]) || line[lpos][cpos]=='.') cpos++;
  return d;
}

char* my_getstr() {
  static char tmp[100];
  check_pos();
  sscanf(line[lpos]+cpos, "%s", tmp);
  while (line[lpos][cpos]==' ') cpos++;
  while (isalpha(line[lpos][cpos])) cpos++;
  return tmp;
}

void ignore() {
  char ch=0;
  int par =0;
  while (ch!='(') ch = my_getc();
  par++;
  while (par) {
    ch = my_getc();
    if (ch=='(') par++;
    else if (ch==')') par--;
  }
}

double solve(double pos) {
  char ch = 0, *name;
  double w;
  string name_str;
  
  while (ch!='(') ch = my_getc();
  w = my_getf();
  //printf("go w %lf\n", w);
  pos *= w;
  ch=' ';
  //while (ch=='\n' || ch==' ') ch = my_getc();
  name = my_getstr();
  //printf("got %s\n", name);
  if (name[0]==')') return pos;
  else {
  //printf("I am in char %s\n", name);
    //name + 1 = my_getstr();
    //scanf("%s", name+1);
    //name[0] = ch;
    if (name[strlen(name)-1]==')') name[strlen(name)-1] = 0;
    name_str = name;
    if (st.find(name_str) != st.end()) return solve(pos);
    else {
      ignore();
      return solve(pos);
    }
  }
  
}

int main() {
  //FILE *fin=fopen("tree.in", "r"), *fout=fopen("tree.out", "w");
  int i, x, t, n, a, y;
  char name[100], tmp[100];
  string tmp_str;
  
  scanf("%d", &t);
  for (x=1; x<=t; x++) {
    scanf("%d\n", &l);
    for (i=0; i<l; i++) gets(line[i]);
    
    scanf("%d\n", &a);
    printf("Case #%d:\n", x);
    for (y=1; y<=a; y++) {
      scanf("%s %d", name, &n);
      //printf("%s\n", name);
      for (i=1; i<=n; i++) {
	scanf("%s", tmp);
	tmp_str = tmp;
	st.insert(tmp_str);
      }
      lpos = cpos = 0;
      printf("%.7lf\n", solve(1));
      st.clear();
    }
  }
  
  //fclose(fin); fclose(fout);
  return 0;
}
