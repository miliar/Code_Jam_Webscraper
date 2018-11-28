#include <cstdio>
#include <string>
#include <cstring>
#include <set>
#include <map>
using namespace std;

int nextsearch[131];
int nosearches[131];
int searches[1010];

int main(){
  int n, s, q, k, i, ans, max, pat;
  map <string, int> engines;
  map <string, int> :: iterator it;
  string pal;
  char buf[131];

  scanf("%d", &n);
  for (k = 1; k <= n; k++){
    engines.clear();
    memset(nextsearch, 0, 131*sizeof(int));
    memset(nosearches, 0, 131*sizeof(int));
    memset(searches, 0, 1010*sizeof(int));
    scanf("%d", &s);
    getchar();
    for (i = 0; i < s; i++){
      fgets(buf, 110, stdin);
      pal = buf;
      engines.insert(make_pair(pal, i));
      nextsearch[i] = 2000;
      nosearches[i] = 0;
    }
    scanf("%d", &q);
    getchar();
    for (i = 0; i < q; i++){
      fgets(buf, 110, stdin);
      pal = buf;
      it = engines.find(pal);
      searches[i] = it->second;
      if (nosearches[it->second] == 0)
	nextsearch[it->second] = i;
      nosearches[it->second]++;
    }

    ans = 0;
    while (1){

      //      for (i = 0; i < s; i++){
      //	printf("%d - prox: %d\n", nosearches[i], nextsearch[i]);
      //      }
      //      printf("\n");

      max = 0;
      if (nosearches[max] > 0){
	for (i = 1; i < s; i++){
	  if (nosearches[i] == 0 || nextsearch[i] > nextsearch[max]){
	    max = i;
	    if (nosearches[max] == 0) break;
	  }
	}
      }
      //      printf("escolhi %d\n", max);
      
      if (nosearches[max] == 0) break;
      ans++;
      pat = nextsearch[max];
      nosearches[max]--;
      if (nosearches[max] >= 0){
	memset(nosearches, 0, 131*sizeof(int));
	for (i = pat; i < q; i++){
	  if (nosearches[searches[i]] == 0)
	    nextsearch[searches[i]] = i;
	  nosearches[searches[i]]++;
	}
      }
    }
    printf("Case #%d: %d\n", k, ans);
  }

  return 0;
}
