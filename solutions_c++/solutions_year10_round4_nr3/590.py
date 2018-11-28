#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<ctime>
using namespace std;
const int INF = 2147483647;
const double PI = 3.141592653589793;

int z,q,i,j,res,n,a,b,c,d;
bool tab[105][105],tab2[105][105],jest;

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    for (i=0;i<=100;i++) for (j=0;j<=100;j++) tab[i][j]=false;
    scanf ("%d",&n);
    while (n--) {
          scanf ("%d %d %d %d",&a,&b,&c,&d);
          for (i=a;i<=c;i++) for (j=b;j<=d;j++) tab[i][j]=true;
    }
    res = 0;
    while (1) {
          jest = false;
          for (i=1;i<=100;i++) for (j=1;j<=100;j++) 
              if (tab[i][j]) jest=true;
          if (!jest) break;
          res++;
          for (i=1;i<=100;i++) for (j=1;j<=100;j++) 
          if (tab[i][j] && !tab[i-1][j] && !tab[i][j-1]) tab2[i][j]=false;
          else if (!tab[i][j] && tab[i-1][j] && tab[i][j-1]) tab2[i][j]=true;
          else tab2[i][j]=tab[i][j];   
          for (i=1;i<=100;i++) for (j=1;j<=100;j++) tab[i][j]=tab2[i][j];      
    }
    printf("Case #%d: %d\n",q,res);
}
return 0;
}
