#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<numeric>
using namespace std;
int t,c,d,n;
string s;
main(){
  cin>>t;
  for(int tt=1;tt<=t;tt++){
    cin>>c;
    char next[30][30]={};
    while(c--){
      cin>>s;
      next[s[0]-'A'][s[1]-'A']=s[2];
      next[s[1]-'A'][s[0]-'A']=s[2];
    }
    bool op[30][30]={};
    cin>>d;
    while(d--){
      cin>>s;
      op[s[0]-'A'][s[1]-'A']=true;
      op[s[1]-'A'][s[0]-'A']=true;
    }
    cin>>n>>s;
    string cur;
    bool a[30]={};
    for(int i=0;i<s.size();i++)if(cur.size()&&next[cur[cur.size()-1]-'A'][s[i]-'A'])cur[cur.size()-1]=next[cur[cur.size()-1]-'A'][s[i]-'A'];else{
      for(int j=0;j<cur.size();j++)if(op[cur[j]-'A'][s[i]-'A']){cur="";goto fail;}
      cur+=s[i];
fail:;
    }

    printf("Case #%d: [",tt);
    for(int i=0;i<cur.size();i++){
      if(i)printf(", ");
      printf("%c",cur[i]);
    }
    puts("]");
  }
}

