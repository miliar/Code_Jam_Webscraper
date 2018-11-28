# include <list>
# include <algorithm>
# include <numeric>
# include <sstream>
# include <iostream>
# include <iomanip>
# include <cstdio>
# include <cmath>
# include <cstdlib>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <deque>
# include <stack>
# include <vector>
# include <cstring>
# include <fstream>

typedef long long int lli;
typedef unsigned long long ull;

using namespace std;

int main()
{
char a[27],b[201];
strcpy(a,"yhesocvxduiglbkrztnwjpfmaq");
int n,j;
scanf("%d",&n);
getchar();
for(int i=1;i<=n;i++)
{
  j=0;
  cin.getline(b,201);
  while(b[j]!='\0')
  {
    if(b[j]==' '){j++;continue;}
    b[j]=a[(int)(b[j]-'a')];
    j++;
  }
  printf("Case #%d: %s\n",i,b);
}
return 0;
}


