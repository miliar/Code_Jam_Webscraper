#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>

#include <cassert>
#include <cstdio>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)

using namespace std;

const int nil=1<<24;

struct node{
  int val;
  int isand;
  bool changeable;
  int chno[2];
};

int left(int n){
  return 2*n;
}
int right(int n){
  return 2*n+1;
}

void compute(vector<node> &tree,int n,int root=1){
  node &a=tree[root];

  if(n<right(root)){
    a.chno[a.val]=0;
    a.chno[(a.val+1)%2]=nil;
  }
  else{
    compute(tree,n,left(root));
    compute(tree,n,right(root));

    if(a.isand){
      a.chno[0]=
	((tree[left(root)].chno[0]+tree[right(root)].chno[0])<?
	 (tree[left(root)].chno[0]+tree[right(root)].chno[1])<?
	 (tree[left(root)].chno[1]+tree[right(root)].chno[0])<?nil);
      a.chno[1]=(tree[left(root)].chno[1]+tree[right(root)].chno[1]<?nil);
    }
    else{
      a.chno[1]=
	((tree[left(root)].chno[1]+tree[right(root)].chno[1])<?
	 (tree[left(root)].chno[0]+tree[right(root)].chno[1])<?
	 (tree[left(root)].chno[1]+tree[right(root)].chno[0])<?nil);
      a.chno[0]=(tree[left(root)].chno[0]+tree[right(root)].chno[0]<?nil);
    }
    
    if(a.changeable){

      if(!a.isand){
	a.chno[0]<?=1+
	  ((tree[left(root)].chno[0]+tree[right(root)].chno[0])<?
	   (tree[left(root)].chno[0]+tree[right(root)].chno[1])<?
	   (tree[left(root)].chno[1]+tree[right(root)].chno[0])<?nil);
	a.chno[1]<?=(tree[left(root)].chno[1]+tree[right(root)].chno[1]<?nil);
      }
      else{
	a.chno[1]<?=1+
	  ((tree[left(root)].chno[1]+tree[right(root)].chno[1])<?
	   (tree[left(root)].chno[0]+tree[right(root)].chno[1])<?
	 (tree[left(root)].chno[1]+tree[right(root)].chno[0])<?nil);
	a.chno[0]<?=(tree[left(root)].chno[0]+tree[right(root)].chno[0]<?nil);
      }
      
    }
    
  }
  //cout << root << ' ' << a.val << ' ' << a.chno[0] << ' ' << a.chno[1] << endl;
}

main(){
  int CT;
  cin >> CT;
  REP(C,CT){
    cout << "Case #" << C+1 << ": ";

    int n,v;
    cin >> n >> v;
    vector<node> tree(n+1);
    REP(i,(n-1)/2){
      cin >> tree[i+1].isand >> tree[i+1].changeable;
    }
    REP(i,(n+1)/2){
      cin >> tree[(n-1)/2+i+1].val;
    }

    compute(tree,n);

    if(tree[1].chno[v]>=nil)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << tree[1].chno[v] << endl;
  }
}
