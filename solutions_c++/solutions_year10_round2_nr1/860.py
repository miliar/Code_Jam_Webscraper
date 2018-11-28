#include <stdio.h>
#include <vector>
#include <string>
#include <set>


using namespace std;


void parse_dir_name(char *n, vector<set<string> > &dirs)
{
  string sofar;
  char buf[100];
  int dirlevel = 0;
  char *p = n;

  //printf("parsing the dir name %s\n", n);

  do {
    p++;
    if(*p == '/' || *p == 0) {
      memcpy(buf, n, p - n);
      buf[p-n] = 0;
      dirs[dirlevel++].insert(string(buf));
      //printf("Added %s to level %d\n", buf, dirlevel);
    }
    
  } while(*p);
}

int main() 
{
  int cases;

  scanf("%d", &cases);
  
  for(int i=0;i< cases; i++) {
    int exist, make;
    vector<set<string> > dirs(100);
    scanf("%d%d", &exist, &make);
    //printf("exist = %d, make = %d\n", exist, make);
    for(int j=0;j<exist;j++) {
      char dirname[100];
      scanf("%s", dirname);
      
      // parse dir name
      parse_dir_name(dirname, dirs);
    }
    int total_dirs = 0;
    for(int j=0;j<dirs.size();j++) {
      total_dirs += dirs[j].size();
    }

    //printf("Found %d dirs before\n", total_dirs);
    // new dirs
    for(int j=0;j<make;j++) {
      char dirname[100];
      scanf("%s", dirname);
      
      // parse dir name
      parse_dir_name(dirname, dirs);
    }
    
    int added_dirs =0;
    for(int j=0;j<dirs.size();j++) {
      added_dirs += dirs[j].size();
    }
    

    printf("Case #%d: %d\n", i+1, added_dirs - total_dirs);
  }

  return 0;
}
