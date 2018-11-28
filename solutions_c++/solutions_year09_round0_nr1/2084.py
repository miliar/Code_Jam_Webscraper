#include <vector>
#include <string>
#include <set>
using namespace std;

#define MAX 65536

#define fori(a,b) for(a=0;a<b;a++)

set<char>* toSuperPal( char *ptr, int L ) {
  set<char> *tmp = new set<char>[L];
  int i=0;
  while(*ptr!='\0') {
    if( *ptr == '(' ) {
      ptr++;
      while( *ptr != ')' ) 
        tmp[i].insert( *ptr++ );
    } 
    else
      tmp[i].insert( *ptr );

    ptr++;
    i++;
  }
  return tmp;
}

int main() {
  int i,L,D,N,num,K=1;
  scanf("%d %d %d",&L,&D,&N);
  vector<string> v;
  char lin[MAX];
  while( D-- ) {
    scanf("%s",lin);
    v.push_back( string(lin) );
  }
  while( N-- ) {
    scanf("%s",lin);
    set<char> *sp = toSuperPal( lin, L );
    num=0;

    fori( i, v.size() ) {
      bool correct = true;
      for( int j=0; correct && j<L; j++ )
        correct = (sp[j].find(v[i][j])!=sp[j].end());
      if( correct ) num++;
    }
    printf("Case #%d: %d\n",K++,num);
  }
  return 0;
}
