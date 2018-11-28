#include <iostream>
#define MAX 55
using namespace std;
char pl[MAX][MAX];
int x, y;
bool solve() {
    for(int i=0; i<x; i++)
        for(int j=0; j<y; j++) {
	  if(pl[i][j] == '#') {
	      for(int a=0; a<2; a++)
		for(int b=0; b<2; b++)
		    if(pl[i+a][j+b] != '#')
		        return false;
	      pl[i][j]    = '/';
	      pl[i][j+1]  = '\\';
	      pl[i+1][j]  = '\\';
	      pl[i+1][j+1]= '/';
	  }
        }
    return true;
}
int main() {
    int t;
    cin >> t;
    for(int z=1; z<=t; z++) {
 
        cin >> x >> y;
        for(int i=0; i<MAX; i++)
	  for(int j=0; j<MAX; j++)
	      pl[i][j] = '.';
        for(int i=0; i<x; i++)
	  for(int j=0; j<y; j++)
	      cin >> pl[i][j];
        cout << "Case #" << z << ":\n";
        if(!solve())
	  cout << "Impossible\n";
        else {
	  for(int i=0; i<x; i++) {
	      for(int j=0; j<y; j++)
		cout << pl[i][j];
	      cout << '\n';
	  }
        }
    }
    return 0;
}