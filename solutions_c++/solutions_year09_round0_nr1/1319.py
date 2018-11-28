#include<cstdio>
#include<vector>
#include<string>
#include<map>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ (17*5000+47)
int tree[SZ][26];
int root=0;
int tsize=0;
char p[2000];
vector<vector<int > >dsc;
int add(int x,char *a) {
  if(x==0) {
    x=++tsize;
    REP(i,26) tree[x][i]=0;    
  }
  if(*a) {
    int k=*a-'a';
    tree[x][k]=add(tree[x][k],a+1);
  }
  return x;
}
int go(int x,int l) {
  int ans=0;
  if(dsc[l].size()==0) return 1;
  REP(i,dsc[l].size()) {
    int a=dsc[l][i];
    if(tree[x][a]) ans+=go(tree[x][a],l+1);
  }
  return ans;
}
int main() {
  int n,l,d;
  scanf("%d %d %d",&l,&d,&n);
  REP(i,d) {
    scanf("%s",p);
    root=add(root,p);    
  } 
  REP(C,n)  {
    scanf("%s",p);
    dsc=vector<vector<int > >();
    for(int i=0;p[i];++i) {
      if(p[i]=='(') {
	vector<int> tmp;
	for(i++;p[i]!=')';++i) tmp.push_back((int)(p[i]-'a'));
	dsc.push_back(tmp);
      } else dsc.push_back(vector<int>(1,(int)(p[i]-'a')));
    }
    printf("Case #%d: %d\n",C+1,go(root,0));
    


  }
  
}
