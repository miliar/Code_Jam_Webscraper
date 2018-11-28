#include <fstream>
#include <stack>
using namespace std;

int tab[105][105];
int bas[105][105];

int main(){
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int n, t=0, h, w, i, j, cont=1, a, b, alt, c, d, cc, dd;
    in>>n;
    
    stack <pair <int, int> >s;
    pair <int, int> ii;
    pair <int, int> jj;
    while (t<n){
          cont=1;
          for (i=0; i<105; i++)
          for (j=0; j<105; j++){
              tab[i][j]=20000;
              bas[i][j]=0;
              }
          
          in>>h>>w;
          for (i=1; i<=h; i++)
          for (j=1; j<=w; j++)in>>tab[i][j];
          
          for (i=1; i<=h; i++)
          for (j=1; j<=w; j++){
              if (bas[i][j]==0)s.push(make_pair(i, j));
              while (!s.empty()){
                    ii=s.top();
                    a=ii.first; b=ii.second;
                    alt=tab[a][b];
                    if (tab[a+1][b]>=alt && tab[a-1][b]>=alt && tab[a][b+1]>=alt && tab[a][b-1]>=alt){
                       while (!s.empty()){
                             jj=s.top(); c=jj.first; d=jj.second; s.pop();
                             bas[c][d]=cont;       
                             }
                       cont++;
                       }
                       
                    else {
                         if (tab[a-1][b]<=tab[a][b-1]){c=a-1; d=b;}
                         else {c=a; d=b-1;}
                         if (tab[c][d]<=tab[a][b+1]){;}
                         else {c=a; d=b+1;}
                         if (tab[c][d]<=tab[a+1][b]){;}
                         else {c=a+1; d=b;}
                         
                         if (bas[c][d]!=0){
                            while (!s.empty()){
                                  jj=s.top(); cc=jj.first; dd=jj.second; s.pop();
                                  bas[cc][dd]=bas[c][d];
                                  }
                            
                            }
                         else {s.push(make_pair(c, d));}
                         
                         }
                       
                    }
              }
          out<<"Case #"<<t+1<<":"<<endl;
          for (i=1; i<=h; i++){
          for (j=1; j<=w; j++){
              char ch='a'+(bas[i][j]-1);
              out<<ch<<' ';
              }
              out<<endl;
          }
          //out<<endl<<endl;
          t++;
          }
    }
