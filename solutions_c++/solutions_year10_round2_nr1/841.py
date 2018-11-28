#include <string>
#include <map>
#include <cstdio>
#include <cstdlib>

using namespace std;

struct Dir {
	Dir*& operator[](string str){return directories[str];}
	std::map<string, Dir*> directories;
};

int main(int argc, char** argv){
  unsigned int tests, i;
  scanf("%d", &tests);
  for (i=0;i<tests;i++){
    Dir root;
    unsigned int there, todo, j;
    scanf("%d %d", &there, &todo);
   
    for (j=0;j<there;j++){
      Dir* currdir = &root;
      string dir;
      char ch = 0;
      while (ch != '/') 
	ch = getchar();
      while (ch != '\r' && ch != '\n') {
	ch = getchar();
	while (ch != '/' && ch != '\r' && ch != '\n'){
	  dir += ch;
	  ch = getchar();
	}
	if (!currdir->operator[](dir))
	  currdir->operator[](dir) = new Dir;
	currdir = currdir->operator[](dir);
      }

    }

    unsigned int number = 0;
    for (j=0;j<todo;j++){
      Dir* currdir = &root;
      string dir;
      char ch = 0;
      while (ch != '/') 
	ch = getchar();
      while (ch != '\r' && ch != '\n') {
	ch = getchar();
	while (ch != '/' && ch != '\r' && ch != '\n'){
	  dir += ch;
	  ch = getchar();
	}
	if (!currdir->operator[](dir)){
	  currdir->operator[](dir) = new Dir;
	  number++;
	}
	currdir = currdir->operator[](dir);
      }



      
    }
printf("Case #%i: %i\n", i+1, number);
  }

  return 0;
}
