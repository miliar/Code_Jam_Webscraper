#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

char gg[6000][20];
char word[100];
vector< vector<char> > data;
int l;

bool ok(char val,char pos) {
     int i;
     for (i=0;i<data[pos].size();i++)
         if (val==data[pos][i]) return true;
     return false;
}

bool count(int m) {
    int i;
    for (i=0;i<l;i++) {
        if (ok(gg[m][i],i)) continue;
        return false;
    }
    /*for (i=0;i<l;i++)
        printf ("%c",gg[m][i]);
    printf ("\n");*/
    return true;
}

int main() {
    int d,n,i,j,k,pos,res;
    char c;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf ("%d%d%d",&l,&d,&n);
    for (i=0;i<d;i++) {
        for (j=0;j<l;j++) {
            while (scanf ("%c",&c)==1) {
                  if (c<97 || c>122) continue;
                  gg[i][j] = c;
                  break;      
            }
        }
    } 
    for (i=0;i<n;i++) {
        data.clear(); data.resize(l); 
        j = 0; pos = 0; res = 0;
        while (scanf ("%c",&c)==1) {
              if (c=='(') {
                 j++;
                 while (scanf ("%c",&c)==1) {
                       if (c==')') break;
                       if (c<97 || c>122) continue;
                       data[pos].push_back(c);
                       j++;                          
                 } 
              }
              else if (c<97 || c>122) continue;
              else data[pos].push_back(c);
              j++; pos ++;
              if (pos==l) break;
        }
        for (j=0;j<d;j++) res += count(j);
        printf ("Case #%d: %d\n",i+1,res);
    }
    return 0;   
}
