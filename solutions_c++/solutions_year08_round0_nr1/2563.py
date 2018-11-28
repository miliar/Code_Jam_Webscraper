#include<iostream>
#include<vector>
using namespace std;
#define pb push_back
#define INF 99999 

int main(){
  int N;
  scanf("%d\n",&N);
  for(int no=0;no<N;no++){
    int S;
    scanf("%d\n",&S);
    vector<string> searcheng;
    searcheng.clear();
    string temp;
    while(S--){
      getline(cin,temp);
      searcheng.pb(temp);
    }
    int Q;
    scanf("%d\n",&Q);
    
    vector<string> queries;
    queries.clear();
    while(Q--){
      getline(cin,temp);
      queries.pb(temp);
    }
    Q=queries.size();
    S=searcheng.size();
    if(Q==0 || S==0){
      printf("Case #%d: %d\n",no+1,0);
      continue;
    }
    int cost[105];
    int oldcost[105];
    cost[0]=0; 
    for(int i=0;i<S;i++){
      if(queries[0]==searcheng[i])cost[i]=INF;
      else cost[i]=0;
      oldcost[i]=cost[i];
    }
    for(int i=1;i<Q;i++){
      for(int j=0;j<S;j++){
	if(queries[i]==searcheng[j])cost[j]=INF;
	else{
	 int costmin=oldcost[j];
	 for(int k=0;k<S;k++)costmin=costmin<(oldcost[k]+1)?costmin:(oldcost[k]+1);
	 cost[j]=costmin;
	}
      }
      for(int j=0;j<S;j++)oldcost[j]=cost[j];
    }
    int ret=cost[0];
    for(int i=1;i<S;i++)ret=ret>cost[i]?cost[i]:ret;
    printf("Case #%d: %d\n",no+1,ret);
  }
  return 0;
}
