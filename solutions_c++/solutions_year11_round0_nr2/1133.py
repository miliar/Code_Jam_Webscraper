#include <iostream>
#include<stdio.h> 
#include <string>
using namespace std;
bool op[26][26];
char co[26][26];
void work()
{
  int i,j,k;
  string lc;
  char t1,t2;
  memset(op,0,sizeof(op));
  memset(co,0,sizeof(co));
  scanf("%d",&k);
  for(i=1;i<=k;i++){
    cin>>lc;
	co[lc[0]-'A'][lc[1]-'A']=co[lc[1]-'A'][lc[0]-'A']=lc[2];
  }
  scanf("%d",&k);
  for(i=1;i<=k;i++){
    cin>>lc;
    op[lc[0]-'A'][lc[1]-'A']=op[lc[1]-'A'][lc[0]-'A']=true;
  }
  cin>>k>>lc;
  string ans("");
  ans+=lc[0];
  for(i=1;i<k;i++){
    ans+=lc[i];
	while(ans.length()>1){
	  t1=ans[ans.length()-1]-'A';
	  t2=ans[ans.length()-2]-'A';
	  if(co[t1][t2]){
	    ans.erase(ans.length()-2,2);
	    ans+=co[t1][t2];
      }
      else break;
    }
    for(j=0;j<ans.length();j++){
      if(op[ans[j]-'A'][ans[ans.length()-1]-'A']){
	    ans = "";break;
	  }
    }
  }
  if(ans.length()>0){
    for(i=0;i<ans.length()-1;i++){
	   cout<<ans[i]<<", ";
    }
    cout<<ans[ans.length()-1]<<"]\n";
  }
  else cout << "]\n";
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int i = 1 ; i <= t ; i++){
	  printf("Case #%d: [",i); 
	  work();}
	return 0;
}
