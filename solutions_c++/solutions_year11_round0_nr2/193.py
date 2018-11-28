#include <iostream>
#include<stdio.h> 
#include <string>
using namespace std;
bool op[26][26];
char co[26][26];
void work()
{
  int i,j,k;
  string tmp;
  char t1,t2;
  memset(op,0,sizeof(op));
  memset(co,0,sizeof(co));
  scanf("%d",&k);
  for(i=1;i<=k;i++){
    cin>>tmp;
	co[tmp[0]-'A'][tmp[1]-'A']=co[tmp[1]-'A'][tmp[0]-'A']=tmp[2];
  }
  scanf("%d",&k);
  for(i=1;i<=k;i++){
    cin>>tmp;
    op[tmp[0]-'A'][tmp[1]-'A']=op[tmp[1]-'A'][tmp[0]-'A']=true;
  }
  cin>>k>>tmp;
  string ans("");
  ans+=tmp[0];
  for(i=1;i<k;i++){
    ans+=tmp[i];
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
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int i = 1 ; i <= t ; i++){
	  printf("Case #%d: [",i); 
	  work();}
	return 0;
}
