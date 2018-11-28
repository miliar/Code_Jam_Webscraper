#include<cstdio>
#include<cmath>
#include<string>
using namespace std;
int main()
{
  int T,N,K;
  scanf("%d",&T);
  for(int i=1;i<=T;i++){
    int tmp;
    string str = "OFF";
    scanf("%d%d",&N,&K);
    tmp = (int)pow(2.0,(double)N);
    if(K%tmp == tmp-1) str ="ON";
    printf("Case #%d: %s\n",i,str.c_str());
  }
  return 0;
}
