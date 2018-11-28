#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int cac[1000][100];

int do_solve(vector<int> q,int S,int qNum,int sNum){
  if(qNum<0) return 0;
  
  if(cac[qNum][sNum]!=-1) return cac[qNum][sNum];
  
  int min=INT_MAX;
  if(q[qNum]==sNum)
    min=-2;
  else
  for(int i=0;i<S;i++){
    int tmp=do_solve(q,S,qNum-1,i);
    if(tmp==-2) continue;
    if(i==sNum){
      if(tmp<min) min=tmp;
    }
    else {
      if( (tmp+1)<min) min=tmp+1;
    }
  }
  
  cac[qNum][sNum]=min;
  return min;

}

int solve(vector<int> q,int S){
  
  // init cac
  //memset(cac,0,1000*100*sizeof(int));
  for(int i=0;i<100000;i++){*(&cac[0][0]+i)=-1;}

  int min=INT_MAX;
  for(int i=0;i<S;i++){
    int tmp=do_solve(q,S,q.size()-1,i);
    if(tmp!=-2 && tmp < min) min=tmp;
  }

  return min;
}

vector<int> convertNumber(vector<string> engines,vector<string> q){

  vector<int> ans;
  int S=engines.size();
  for(int i=0;i<q.size();i++){
    int j;
    for(j=0;j<S;j++){
      if(engines[j]==q[i]) break;
    }
    ans.push_back(j);
  }
  return ans;
}

int main(int argc,char** argv){

  int N;
  scanf("%d",&N);

  for(int i=0;i<N;i++){
    int S,Q;
    scanf("%d",&S);
    vector<string> engines;
    vector<string> q;
    char tmp[200];
      gets(tmp);
    for(int j=0;j<S;j++){
      char tmp[200];
      //scanf("%s",tmp);
      gets(tmp);
      string tmpStr(tmp);
      engines.push_back(tmpStr);
      //cout<<tmp<<"\n";
    }

    scanf("%d",&Q);
    gets(tmp);
    for(int j=0;j<Q;j++){
      char tmp[200];
      //scanf("%s",tmp);
      gets(tmp);
      string tmpStr(tmp);
      q.push_back(tmpStr);
    }

    //cout<<"Engines size="<<engines.size()<<" Query size= "<<Q<<"\n";
    vector<int> qNo=convertNumber(engines,q);
    //for(int j=0;j<qNo.size();j++) cout<<qNo[j]<<"\n";
    //cout<<"\n";
    int switches=solve(qNo,S);
    printf("Case #%d: %d\n",i+1,switches);
  }
  
}
