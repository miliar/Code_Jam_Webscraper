#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int k, len;
char str[50005], s[50005];
vector<int> v;

void makeString()
{
  for(int i=0;i<len;i+=k)
    for(int j=0;j<k;j++)
      s[i+j] = str[i+v[j]];
}

int calc()
{
  int p=0;
  int ret=0;
  while(p<len) {
    ret++;
    int u=p+1;
    while(u<len && s[u]==s[p]) u++;
    p=u;
  }
  return ret;
}

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    scanf("%d",&k);
    scanf("%s",str);
    v.clear();
    for(int i=0;i<k;i++)
      v.push_back(i);
    int res=1<<29;
    len=strlen(str);
    do {
      makeString();
      int tmp=calc();
      res=min(res,tmp);
    } while(next_permutation(v.begin(),v.end()));
    printf("Case #%d: %d\n", t, res);
  }
  return 0;
}
