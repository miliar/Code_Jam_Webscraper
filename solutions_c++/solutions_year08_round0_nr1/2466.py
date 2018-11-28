#include <string>
#include <map>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>

using namespace std;


int getInt(FILE *in)
{
   char buffer [1024];

   fgets(buffer,sizeof(buffer),in);
   // strip trailing whitspaces
   char *ptr = buffer + strlen(buffer) -1;
   while ( ( *ptr == '\r' || *ptr == '\n' || isspace(*ptr)) && ptr != buffer ) ptr --; 
   ptr[1] = 0;
   return atoi(buffer);
}
const char * getStr(FILE *in)
{
   static char buffer [1024];
   fgets(buffer,sizeof(buffer),in);
   // strip trailing whitspaces
   char *ptr = buffer + strlen(buffer) -1;
   while ( (*ptr == '\r' || *ptr == '\n' || isspace(*ptr) ) && ptr != buffer ) ptr --; 
   ptr[1]=0;
   return buffer;
}

/*
 * Saving the universe .. using greedy approach
 *  At anytime, choose next engine such that switch is 
 *  not needed anytime soon.
 */

struct ltstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) < 0;
  }
};

int  countSwitchesFast (  vector<int>  strings,  // Sequence of strings
					  int count)             // strings are 0 .. count-1
{

  vector<bool>  seen(count);
  int           seen_count = 0;
  
  int retCnt = 0;

  for(int i = 0 ; i < count ; i ++ ) seen[i] = false;
  seen_count = 0;
    
  for( unsigned j = 0 ;  j < strings.size() ; j ++ ) {
    int str = strings[j];
    if ( seen[str] == true )  continue;
    if ( count - seen_count > 1  ) {
        seen[str] = true;
        seen_count++;
        continue;
    } 
    retCnt ++;
    for(int i = 0 ; i < count ; i ++ ) seen[i] = false;
    seen_count = 1;
    seen[str] = true;
   }    
   return retCnt;    
}

void doCase( int cn, FILE *in)
{
	map<const char *, int, ltstr>   intern;
#define INTERN(str)  ( intern.find(str)==intern.end() ? () : intern[str] )

	int  numEngines = getInt(in);
	
	for( int i = 0 ; i < numEngines ; i ++ ) {
		const char * name = getStr(in);
		intern[strdup(name)] = intern.size();
	}

	int  numStrings = getInt(in);
	vector<int>   strings(numStrings);
	for( int i = 0 ; i < numStrings ; i ++ ) {
		const char * name = getStr(in);
		strings[i] = intern[name];
	}
    int i = countSwitchesFast(strings,intern.size());
	printf("Case #%d: %d\n",cn,i);	  

	for( map<const char *, int, ltstr>::const_iterator i = intern.begin();
		 i != intern.end(); ++i)
		 free((void*)((*i).first));
}

	
int
main(int Argc, char **Argv)
{
    //FILE *in = fopen(Argv[1],"r");
	FILE *in = fopen("C:\\Vardhan\\Contests\\GoogleCodeJam\\SavingTheUniverse\\inp3.txt","r");
 
    int numCases = getInt(in);
	for ( int i = 0 ; i < numCases ; i ++ ) 
		doCase(i+1,in);
}
