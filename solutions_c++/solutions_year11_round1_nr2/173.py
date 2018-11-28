#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned short us;
typedef unsigned char uc;

int n;
char map[256];
char ord[27];
char dict[10000][12];
char len[10000];

char dis[10000][10000];

int score(int w, int pos)
{
  int m=100, match=0;
  for(int i=0;i<n;i++) if(dis[w][i]>pos && dis[w][i] < m) m=dis[w][i];
  for(int i=0;i<len[w];i++) if(map[dict[w][i]]==m) match=1;
  if (m==100) return 0;
  fprintf(stderr,"Simulating %s at %d: guess=%c\n",dict[w],pos,ord[m]);
  return !match + score(w,m);
}

main()
{
  int cases;
  cin >> cases;
  for(int loop=1; loop<=cases; loop++)
  {
    printf("Case #%d:",loop);
    int m; cin>>n>>m;
    for(int i=0;i<n;i++) { scanf("%s",dict[i]); len[i]=strlen(dict[i]); }
    for(int j=0;j<m;j++)
    {
      scanf("%s",ord);
      for(int i=0;i<26;i++) map[ord[i]]=i;

      for(int i=0;i<n;i++) for(int j=i+1;j<n;j++)
      {
        if (len[i]!=len[j]) { dis[i][j]=dis[j][i]=0; continue; }
        dis[i][j]=100;
        for(int l=0;l<len[i];l++) if (dict[i][l]!=dict[j][l])
        {
          dis[i][j]=min(dis[i][j],min(map[dict[i][l]], map[dict[j][l]]));
        }
        dis[j][i] = dis[i][j];
      }

      int m=-1, best=-1;
      for(int i=0;i<n;i++) { int t=score(i,-1);
fprintf(stderr, "%s: %d\n",dict[i],t);
if (t>m) {m=t;best=i; } }
      printf(" %s",dict[best]);
    }
    puts("");
  }
}
