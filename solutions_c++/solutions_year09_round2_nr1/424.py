#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<cmath>

using namespace std;

#define PB push_back


class node{
public:
  double weight;
  int nextl;
  int nextr;
  string ledge;
  node(double a=0.0,int b=-1,int k=-1,string str=""){
    weight=a; nextl=b; ledge=str; nextr=k;
  }
};

int idx;
vector<node> nodes;
char *p;
double conv(string str){
  double ret=0.0;
  double num=1.0;
  for(int i=0;i<str.size();i++){
    num *= 0.1;
    ret += num*(str[i]-'0');
  }
  return ret;
}

int parse(){
  int now = idx;
  idx++;
  if( *p != '(') exit(1);

  p++;
  char to = *p;
  p+=2;

  string num="";
  while(isdigit(*p)){
    num+=*p;
    p++;
  }
  double f=conv(num);
  f += (double)(to-'0');
  nodes[now].weight=f;


  if(*p!=')'){
    string animal="";
    while(isalpha(*p)){
      animal+=*p;
      p++;
    }
    nodes[now].ledge=animal;
    nodes[now].nextl=parse();
    nodes[now].nextr=parse();
    if(*p!=')')exit(1);
    p++;
  }
  else {
    nodes[now].nextl=-1;
    nodes[now].nextr=-1;
    p++;
  }
  return now;
}

int main(){
  char cstr[2000000];
  string strs;
  int L,A,n;
  cin>>n;
  for(int i=1;i<=n;i++){
    idx=0;
    strs="";
    cin>>L;
    cin.ignore();
    for(int j=0;j<L;j++){
      string tmp;
      getline(cin,tmp);
      for(int k=0;k<tmp.size();k++){
	if( tmp[k] != ' ' && tmp[k] !='\n'){
	  strs+=tmp[k];
	}
      }
    }
    strcpy(cstr,strs.c_str());
    p=cstr;
    nodes.clear();
    nodes.resize(300);
    parse();
  

    string animal;
    string feature;
    cin>>A;
    printf("Case #%d:\n",i);
    for(int j=0;j<A;j++){
      int t;
      vector<string> features;
      cin>>animal;
      cin>>t;
      for(int k=0;k<t;k++){
	cin>>feature;
	features.PB(feature);
      }
      double ans=1.0;
      int now=0;
      while(1){
	ans*=nodes[now].weight;
	if( nodes[now].nextl==-1)break;

	bool flg=false;
	for(int i=0;i<features.size();i++){
	  if(nodes[now].ledge==features[i]){
	    flg=true;
	    break;
	  }
	}
	if(flg){
	  now=nodes[now].nextl;
	}
	else now=nodes[now].nextr;
      }
      printf("%.7lf\n",ans);
    }
  }
  return 0;
}
