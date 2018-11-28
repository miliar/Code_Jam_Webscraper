#include<cstdio>
#include<iostream>
#include<map>
#include<string>
#include<vector>

using namespace std;


struct data{
  bool f;
  map<string, data> n;
  data(){
    f=false;
  };
};

int main(){
  int T;
  scanf("%d\n",&T);
  for(int t=1;t<=T;t++){
    int N,M;
    scanf("%d %d\n",&N,&M);
    data dic;
    dic.f=true;
    data *p;

    for(int i=0;i<N;i++){
      string str;
      getline(cin,str);
      string::iterator a=str.begin();
      p=&dic;
      for(string::iterator j=str.begin()+1;j<str.end();j++){
	if(*j=='/'){
	  string tmp(a,j);
	  (p->n[tmp]).f=true;
	  p=&(p->n[tmp]);
	  a=j;
	}
      }
      string tmp(a,str.end());
      (p->n[tmp]).f=true;
      p=&(p->n[tmp]);
    }

    int ans=0;
    for(int j=0;j<M;j++){
      string str;
      getline(cin,str);     
      string::iterator a=str.begin();
      p=&dic;
      for(string::iterator j=str.begin()+1;j<str.end();j++){
	if(*j=='/'){
	  string tmp(a,j);
	  if((p->n).find(tmp)!=(p->n).end()){
	    p=&(p->n[tmp]);
	  }else {
	    (p->n[tmp]).f=true;
	    p=&(p->n[tmp]);
	    ans++;
	  }
	  a=j;
	}
      }
      string tmp(a,str.end());
      if(!(p->n[tmp]).f){
	(p->n[tmp]).f=true;
	p=&(p->n[tmp]);
	ans++;
      }
    }
    printf("Case #%d: %d\n",t,ans);
  }
  return 0;
}
