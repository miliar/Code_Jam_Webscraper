#include<stdio.h>
#include<vector>
#include<math.h>
#include<stdlib.h>
using namespace std;

int tests, n, ret;
vector<int> seq[2];
int pos[2], job[2];

void get_next_job(int arg) {
  job[arg]++;
  while(job[arg] < n && seq[0][job[arg]] != arg)
    job[arg]++;
}

int main() {
  scanf("%d",&tests);
  for(int t=1;t<=tests;t++) {
    scanf("%d",&n);
    seq[0].clear(); seq[1].clear();
    for(int i=0;i<n;i++) {
      char c[2]; int val;
      scanf("%s %d",&c,&val);      
      if(c[0] == 'O')
        seq[0].push_back(0);
      else
        seq[0].push_back(1);
      seq[1].push_back(val);
    }   
            
    ret = 0;
    pos[0] = pos[1] = 1;
    job[0] = job[1] = -1;
    get_next_job(0);
    get_next_job(1);
    
    while(job[0] != n || job[1] != n) {
      if(job[0] < job[1]) {
        int move = abs(pos[0]-seq[1][job[0]])+1;
        ret += move;
        pos[0] = seq[1][job[0]];
        get_next_job(0);
        if(job[1] == n)
          continue;
        if(pos[1] < seq[1][job[1]])
          pos[1] += min(move, seq[1][job[1]] - pos[1]);
        else
          pos[1] -= min(move, pos[1] - seq[1][job[1]]);
        
      }
      else {
        int move = abs(pos[1]-seq[1][job[1]])+1;
        ret += move;
        pos[1] = seq[1][job[1]];
        get_next_job(1);
        if(job[0] == n)
          continue;
        if(pos[0] < seq[1][job[0]])
          pos[0] += min(move, seq[1][job[0]] - pos[0]);
        else
          pos[0] -= min(move, pos[0] - seq[1][job[0]]);        
      }
    }
    printf("Case #%d: %d\n",t,ret);
  }
  return 0;  
}
            
      
    
    
      
    
    
