#include <stdio.h>
#include <stdint.h>
#include <map>
#include <fstream>
#include <cstdlib>

using namespace std;
using std::ifstream;

int main(){



map<char,char> rch;
map<char, char>::iterator it;


static const char *a1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
static const char *a2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
static const char *a3="de kr kd eoya kw aej tysr re ujdr lkgc jv";

static const char *b1="our language is impossible to understand";
static const char *b2="there are twenty six factorial possibilities";
static const char *b3="so it is okay if you want to just give up";

int i=0;
while(a1[i] != '\0'){
  rch[a1[i]]=b1[i];
  i++;
}

i=0;
while(a2[i] != '\0'){
  rch[a2[i]]=b2[i];
  i++;
}

i=0;
while(a3[i] != '\0'){
  rch[a3[i]]=b3[i];
  i++;
}

/* print the mapping */
for ( it=rch.begin() ; it != rch.end(); it++ );
    //printf("%c      ==>     %c \n",(*it).first,(*it).second);



ifstream indata; 

indata.open("input.txt"); // opens the file
if(!indata) { 
  printf("\nCould not open file input.txt");
  exit(1);
}

/* read first line..i.e No of iterations */
int Noiterations=0;
indata >> Noiterations;
int tNoiterations=Noiterations;


string tempo;
getline(indata,tempo);

string A;

while(Noiterations > 0){

printf("Case #%d: ",tNoiterations-Noiterations+1);
/* read and parse file a line. Store it in a string */ 
getline(indata,A);
const char *c=A.c_str();

int i=0; 
while(c[i] != '\0'){
it=rch.find(c[i]);

if(it != rch.end()) printf("%c",rch[c[i]]);
else if(c[i]=='q') printf("z");
else if(c[i]=='z') printf("q");
else printf("%c",c[i]);

i++;
}


Noiterations--;
printf("\n");
}

printf("\n");
return 0;
}



