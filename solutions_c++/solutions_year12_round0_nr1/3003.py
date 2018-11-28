#include <string>
#include <vector>
#include <iostream>
#include <map>
//#include <stdio.h>
//#include <stdlib.h>
using namespace std;


//#define conv(X,Y) printf("ans:%c\n",(((long long)((X)-'a')-(long)atol(argv[2]))%26+26)%26+'a');

int main (int argc, char*argv[]){

  string pre ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";
  string post="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";
  
  
  /*
  map<char, char> table;
  for ( int i=0 ; i<pre.size() && i<post.size() ; i++ )
    table.insert( map<char, char>::value_type(pre[i], post[i]) ); 
 
  map<char, char>::iterator it= table.begin();
  for( ; it!=table.end() ; ++it )
    cout << (*it).first <<","<< (*it).second << endl;
  */
  
  char table[26];
  for ( int i=0 ; i<26 ; i++ )
    table[i]='@';
  for ( unsigned int i=0 ; i<pre.size() && i<post.size() ; i++ )
    if ( 'a'<=pre[i] && pre[i]<='z' )
      table[pre[i]-'a']=post[i];
  /*  
  for ( int i=0 ; i<26 ; i++ )
    cout << (char)(i+'a') <<","<< table[i] << endl;
  */
  int T;
  cin >> T;
  
  char tmp[256];
  vector<string> G;
  cin.getline(tmp, 255);
  for ( int i=0 ; i<T ; i++ ){
    cin.getline(tmp, 255);
    G.push_back(tmp);
  }
  for ( int i=0 ; i<T ; i++ ){
    cout << "Case #" << i+1 << ": " ;
    for ( unsigned int j=0 ; j<G[i].size() ; j++ )
      if ( 'a'<=G[i][j] && G[i][j]<='z' )
	cout << table[G[i][j]-'a'] ;
      else
	cout << ' ' ;
    cout << endl;
  }
  
  
  return 1;
};
