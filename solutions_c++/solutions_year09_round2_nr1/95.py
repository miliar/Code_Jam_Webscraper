#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<set>
using namespace std;
string s;
int pos;
struct tree {
  tree *left,*right;
  double p;
  bool leaf;
  string name;
  tree() {
    leaf=0;
    while(s[pos]!='(')pos++;
    pos++;
    sscanf(s.c_str()+pos,"%lf",&p);
    while(s[pos]==' ')pos++;
    while(s[pos]!=' '&&s[pos]!=')')pos++;
    while(s[pos]==' ')pos++;
    if(s[pos]==')'){pos++;leaf=1;return;}
    while(s[pos]>='a'&&s[pos]<='z')name+=s[pos++];
//  printf(": %s\n",name.c_str());
    left=new tree();
    right=new tree();
    while(s[pos]!=')')pos++;
    pos++;
  }

};
main(){
  int t;scanf("%d",&t);for(int tt=1;tt<=t;tt++){
    printf("Case #%d:\n",tt);
    s="";
    char buf[1000];
    int cnt;scanf("%d\n",&cnt);while(cnt--){
      gets(buf);
      s+=buf;
    }
    pos=0;
//    puts(s.c_str());
    tree r;
    scanf("%d",&cnt);while(cnt--){
        double p=1;
        int len;
        scanf("%*s %d",&len);
        set<string> s;
        while(len--){
          scanf("%s",buf);
          s.insert(buf);
        }
        tree *cur=&r;
        while(1){
          p*=cur->p;
          if(cur->leaf)break;
          if(s.count(cur->name))cur=cur->left;else cur=cur->right;
        }
        printf("%.8lf\n",p);
    }
  }
}

