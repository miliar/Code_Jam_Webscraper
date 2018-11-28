#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <map>
#include <fstream>

using namespace std;

map <int, int> M;

struct list {
    list *edge [1000];
    list() {
         for(int i = 0; i < 1000; ++i)
           edge[i] = NULL;
    }
};

int get_hash(string s){
    
    int ret = 0;
    for(int i = 0; i < s.length(); ++i)
      ret = (ret * 1171 + s[i]);
    return ret;
}

int GLOB = 0;
list root;

ifstream in( "A-large.IN" );
FILE *out  = fopen( "sol.txt", "w" );

void read_in(){
     
     char c; int key;
     string s, got; in >> s;
     
     list *pok = &root; s += '/';
     for(int i = 1; i < s.length(); ++i){
        if( s[i] == '/' ){
            key = get_hash(got);

            int koji;
            if( M.find(key) == M.end() ) koji = GLOB, M[key] = GLOB++;
            else koji = M[key];
            
            if( pok -> edge[koji] == NULL ) 
                  pok -> edge[koji] = new list();
                  
            pok = pok -> edge[koji];
            got = "";
            continue;
        }     
        got += s[i];
     }
};

int main(){
    
    int T;
    in >> T;
    
    for(int t = 1; t <= T; ++t ){
    
    M.clear(); GLOB = 0;
    int n, m, key, sol = 0;
    in >> n >> m;
   
    root = list ();
    
    for(int i = 0; i < n; ++i)read_in();
    
    string path, dir; 
    for(int i = 0; i < m; ++i){
       
       in >> path; path += '/';
       list *pok = &root;
       for(int j = 1; j < path.length(); ++j){
            if( path[j] == '/' ){

               key = get_hash(dir);

               int koji;
               if( M.find(key) == M.end() )koji = GLOB, M[key] = GLOB++;
               else koji = M[key];

               if( pok -> edge[koji] == NULL ){
                   pok -> edge[koji] = new list();
                   ++ sol;
               }
               pok = pok -> edge[koji]; 
               dir = "";
               continue;
            }
            dir += path[j];
       }    
    }
    fprintf(out,"Case #%d: %d\n", t,  sol );
  }
    system("pause");
    return 0;
}
