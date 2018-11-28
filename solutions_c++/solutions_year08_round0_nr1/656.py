#include<cstdio>
#include<string>

using namespace std;

char str[1000];
int T,i,j,I,s,n,mi;
string engine[10000];
int Q[10000],opt[2000];

main(){
  scanf("%d",&T);
  while (T--){
    scanf("%d",&s);gets(str);
    for (i=0;i<s;++i){
      gets(str);
      engine[i]=str;
    }
    scanf("%d",&n);gets(str);
    for (i=0;i<n;++i){
      gets(str);
      for (j=0;j<s;++j)
	if (str==engine[j]){
	  Q[i]=j;
	  //	  printf("%d %d\n",i,j);
	  break;
	}
    }
    for (i=0;i<s;++i) opt[i]=0;
    for (i=0;i<n;++i){
      mi=opt[0];
      for (j=0;j<s;++j)mi<?=opt[j];
      ++mi;
      for (j=0;j<s;++j) opt[j]<?=mi;
      opt[Q[i]]=100000;
    }
    mi=1000000;
    for (i=0;i<s;++i) mi<?=opt[i];
    printf("Case #%d: %d\n",++I,mi);
  }
}
