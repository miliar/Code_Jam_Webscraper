#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

FILE * fout = fopen ("A-small.out", "w");
ifstream fin ("A-small-attempt2.in");

struct menu{
       char name[500];
}dir[1000];

bool equal (char a[], char b[]){
     int i;
     for (i = 0; a[i]; i ++){
         if (a[i] != b[i]) return false;
     }
     if (a[i] != b[i]) return false;
     return true;
}

void work (){
     int m, n;
     fin >> n >> m;
     int count = 0;
     string in;
     for (int i = 0; i < n; i ++){
         fin >> in;
         int l = 0;
         char name[100];
         while (in[l]){
                  int t = l;
                  l ++;
                  for (int s = 0; s < l; s ++){
                      name[s] = in[s];
                  }
                  while (in[l] != '/' && in[l]){
                        name[l] = in[l];
                        l ++;
                  }
                  name[l] = 0;
                  bool exist = false;
                  for (int j = 0; j < count; j ++){
                      if (equal (dir[j].name, name)){
                         exist = true;
                         break;
                      }
                  }
                  if (!exist){
                     int h = 0;
                     while (name[h]){
                           dir[count].name[h] = name[h];
                           h ++;
                     }
                     dir[count].name[h] = 0;
                     count ++;
                  }
         }
     }
     int need = 0;
     for (int i = 0; i < m; i ++){
         fin >> in;
         int l = 0;
         char name[10];
         while (in[l]){
                  int t = l;
                  l ++;
                  for (int s = 0; s < l; s ++){
                      name[s] = in[s];
                  }
                  while (in[l] != '/' && in[l]){
                        name[l] = in[l];
                        l ++;
                  }
                  name[l] = 0;
                  //cout << name << endl;
                  bool exist = false;
                  for (int j = 0; j < count; j ++){
                      if (equal (dir[j].name, name)){
                         exist = true;
                         break;
                      }
                  }
                  if (!exist){
                     int h = 0;
                     while (name[h]){
                           dir[count].name[h] = name[h];
                           h ++;
                     }
                     dir[count].name[h] = 0;
                     count ++;
                     need ++;
                  }
         }
     }
     fprintf (fout, "%d\n", need);
     fflush (fout);
     return;
}

int main (){
    int s;
    fin >> s;
    //cout << s;
    for (int i = 0; i < s; i ++){
        fprintf (fout, "Case #%d: ", i + 1);
        fflush (fout);
        work ();
    }
    return 0;
}
