#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
const int base=10009;

int dic[110][30];
char ss[1000],ww[1000];
int c,ls,n,ans,k;
int sum[30];
int f[30],jc[30];
vector<int> dv[110];

void get_ans(int now,int lim,int st) {
  if (now==lim+1) {

    //    for (int i=1;i<=lim;i++) printf(" %d",f[i]);
    //printf("\n");

    int tmp=1,ta=0;

    memset(sum,0,sizeof(sum));
    for (int i=1;i<=lim;i++)
      for (int j=0;j<dv[f[i]].size();j++) sum[dv[f[i]][j]]+=dic[f[i]][dv[f[i]][j]];

    for (int k=0;k<ls;k++) {
      if (ss[k]=='+') {
	ta=(ta+tmp)%base;
	tmp=1;
      } else {
	tmp=(tmp*sum[ss[k]-'a'])%base;
      }
    }

    ta=(ta+tmp)%base;
    //    printf("ta %d\n",ta);

    int tmp1=1,bs=jc[lim];
    for (int i=2;i<=lim;i++) {
      if (f[i]==f[i-1]) tmp1++; else {
	bs=bs/jc[tmp1];
	tmp1=1;
      }
    }
    bs=bs/jc[tmp1];
    ta=(ta*bs)%base;
    ans=(ta+ans)%base;
    return;
  }
  for (int i=st;i<=n;i++) {
    f[now]=i;
    get_ans(now+1,lim,i);
  }
}

int main() {
  int c,C=0;
  jc[1]=1;
  for (int i=2;i<=10;i++) jc[i]=jc[i-1]*i;
  for (scanf("%d",&c);c>0;c--) {
    scanf("%s%d",ss,&k);
    ls=strlen(ss);
    scanf("%d",&n);
    memset(dic,0,sizeof(dic));
    for (int i=1;i<=n;i++) {
      scanf("%s",&ww);
      int lw=strlen(ww);
      for (int j=0;j<lw;j++) dic[i][ww[j]-'a']++;
      dv[i].clear();
      for (int j=0;j<26;j++)
	if (dic[i][j]!=0) dv[i].push_back(j);
    }
    printf("Case #%d:",++C);
    for (int i=1;i<=k;i++) {
      ans=0;
      memset(f,0,sizeof(f));
      get_ans(1,i,1);
      printf(" %d",ans);
    }
    printf("\n");
  }
}
