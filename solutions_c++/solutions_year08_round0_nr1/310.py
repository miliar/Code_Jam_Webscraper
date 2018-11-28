/*
  $Id: seng.cc,v 1.1 2008/07/17 18:04:08 chris Exp chris $
*/

#include <iostream>
#include <sstream>
#include <map>

using std::string;
using std::cin;
using std::cerr;

static const unsigned MAX_ENGINES=200;

/* Did I mention I don't like globals? If I only had time... */

static inline
string get_line(void)
{
  string a;
  getline(cin,a);
  return a;
}

unsigned get_integer(void) {
  std::istringstream iss(get_line());
  unsigned a; iss>>a;
  return a;
}

int main(void)
{
  unsigned number_of_cases = get_integer();

  for(unsigned case_no=1; case_no<=number_of_cases; case_no++) {
    unsigned no_engines = get_integer();

    std::map<string,unsigned> eno;
    eno.clear();
    for(unsigned i=0; i<no_engines; i++) 
      eno[ get_line() ] = i;

    unsigned free_engines=no_engines;
    bool eng_map[MAX_ENGINES];
    unsigned switches=0;
    unsigned queries = get_integer();
    for(unsigned i=0; i<no_engines; i++) eng_map[i]=1;
    while(queries--) {
      unsigned u = eno[get_line()];
      if(eng_map[u]) {
	eng_map[u]=0;
	free_engines--;
	if(free_engines==0) {
	  for(unsigned i=0; i<no_engines; i++) eng_map[i]=1;
	  eng_map[u]=0;
	  free_engines=no_engines-1;
	  switches++;
	}
      }
    }
    std::cout << "Case #" << case_no << ": " << switches << std::endl;
  }
}
    
