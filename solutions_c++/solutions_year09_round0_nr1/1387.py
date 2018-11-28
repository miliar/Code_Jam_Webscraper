#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

#define MAXN 15
#define LL long
string let[MAXN];
LL i,j,n,m,t,sol(0),T;
string in;

ifstream fin("A.in");
ofstream fout("A.out");

struct trie {
       map<char, trie*> path;
       char val;
       trie(){}
       trie(char c):val(c){}
       };

trie *root = new trie('-');

void build_trie(string &str) {
     trie *curr = root;
     LL i;
     for (i=0;i<str.size();i++) {
         if (curr->path.count(str[i]) == 0) curr->path[str[i]] = new trie(str[i]);
         curr = curr->path[str[i]];
         }
     if (curr == NULL) curr = new trie(in[i-1]);
     }

void dfs(LL pos, trie *ptr) {
     
     if (pos == m) {
        sol++;
        return;
        }
     
     //cout << "Pos: " << pos << "   ptr->val: " << ptr->val << endl;
     //system("pause");
     
     for (LL i=0;i<let[pos].size();i++)
         if (ptr->path.count( let[pos][i] )) dfs(pos + 1, ptr->path[ let[pos][i] ]);
     }

int main() {
    fin >> m >> n >> T;
    for (i=0;i<n;i++) {
        fin >> in;
        build_trie(in);
        }
    
    for (LL t=0;t<T;t++) {
        cout << "Case #" << t + 1 << ": " << endl;
        fin >> in;
        
        for (i=0;i<m;i++) let[i].resize(0);
        sol = 0;
        
        bool br = false;
        for (i=0,j=0;i<in.size();i++) {
            if (in[i] == '(') {
               br = true;
               continue;       
               }
            if (in[i] == ')') {
               br = false;
               j++;
               continue;       
               }
            let[j].push_back(in[i]);
            if (!br) j++;
            }
            
        trie *tmp = root;
        dfs(0,tmp);

        fout << "Case #" << t + 1 << ": " << sol << endl;
        }
    cout << "DONE!" << endl;
    system("pause");
}
