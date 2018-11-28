#include<cstdio>
#include<climits>
#include<cstring>
#include<iostream>
#include<new>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<string>
#include<cctype>
#include<fstream>
#include<new>
#include<string>
#include<cstring>
using namespace std;

vector<int> start;
vector<int> end;
int length;
int result;

// input parameters
 int L, D, N;

struct Node {
       char ch;
       vector<Node*> childs;
       };

struct trie {
       Node *root; // no character at this
       trie() {
           try {
           root = new Node;
           }
           catch( bad_alloc xa ) {
                printf("Error\n");
                }
           }
       
       void insert( string word ) {
                  
                  Node *node = root;
                  for( int i = 0; i<word.size(); i++ ) {
                     int ch = word[i]; int j = 0;
                     while( j<node->childs.size() && ch>node->childs[j]->ch )
                          j++;
                     if( j==node->childs.size() ) {
                       Node *child;
                       try {
                       child = new Node;
                       }
                       catch( bad_alloc xa ) {
                            printf("Error\n");
                            }
                       
                       child->ch = ch;
                       node->childs.push_back( child );
                       node = node->childs[j];
                       }
                     else if( node->childs.size()!=0 && ch==node->childs[j]->ch )
                            node = node->childs[j];
                     else if( j==0 ) {
                            Node *child;
                            try {
                            child = new Node;
                            }
                            catch( bad_alloc xa ) {
                                 printf("Error\n");
                                 }
                            child->ch = ch;
                            
                            vector<Node*>::iterator it = node->childs.begin();
                            node->childs.insert( it, 1, child );
                            node = node->childs[j];          
                            }
                     else {
                       Node *child;
                       try {
                       child = new Node;
                       }
                       catch( bad_alloc xa ) {
                            printf("Error\n");
                            }
                       child->ch = ch;
                            
                       vector<Node*>::iterator it = node->childs.begin();
                       it += j; node->childs.insert( it, 1, child );
                       node = node->childs[j];
                       }
                     }
                  }
                            
       bool find( vector<char> word ) {
                Node *node = root; int i=0;
                for( i = 0; i<word.size(); i++ ) {
                   char ch = word[i]; int j = 0;
                   while( j<node->childs.size() && ch>node->childs[j]->ch ) 
                        j++;
                   if( j == node->childs.size() )
                     break;
                   else if( ch==node->childs[j]->ch )
                          node = node->childs[j];
                   else 
                     break;
                   }
                if( i<word.size() ) return false;
                else return true;
                }
       }T;
  
void findWords( vector<char> word, string words, int s_no ) {
              if( s_no==L ) {
                if( T.find( word ) ) // check in the trie
                  result++;
                }
              else {
                for( int i = start[s_no]; i<=end[s_no]; i++ ) {
                   vector<char> o_word; for( int j = 0; j<word.size(); j++ ) o_word.push_back( word[j] );
                   char ch = words[i]; o_word.push_back( ch );
                   if( T.find( o_word ) ) findWords( o_word, words, s_no+1 );
                   }
                }
              }
               
int main() {
    ifstream in("A-large.in");
    if( !in.is_open() ) {
      cout << "error\n";
      return 1;
      }
 
    ofstream out("output_small.in");
    if( !out.is_open() ) {
      cout << "error\n";
      return 1;
      }
   
    in >> L >> D >> N;
    for( int i = 0; i<D; i++ ) { 
       string word; in >> word;
       T.insert( word );
       }
    int cases = 1;
    while( cases<=N ) {
         start.clear(); end.clear();
        
         string words; in >> words;
         length = words.size();
         // making up the end and the start points
         int loop = 0; while( loop<words.size() && words[loop]!='(' ) loop++;
         if( loop<words.size() ) { 
           for( int i = 0; i<length; i++ ) {
              if( words[i]=='(' ) {
                start.push_back( i+1 );
                int j = i; while( j<length && words[j]!=')' ) j++;
                end.push_back( j-1 ); i = j; 
                }
              else {
                start.push_back( i );
                end.push_back( i );
                }
              }
           }
         result = 0; vector<char> word;           
         if( start.size()!=0 && end.size()!=0 ) findWords( word, words, 0 );
         else {
          for( int i = 0; i<words.size(); i++ ) word.push_back( words[i] );
          if( T.find( word ) ) result++;
          }
         out << "Case #" << cases << ": " << result << "\n";
         cases++;
         }
    in.close(); out.close();  
    return 0;  
    }

