
#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

#define REP(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases){
    int nJobs;
    cin >> nJobs;
    
    vector<int> jobs[2];
    vector<int> which;
    
    REP(iJob, nJobs){
      string s;
      int pos;
      cin >> s >> pos;
      if(s[0] == 'O'){
	which.push_back(0);
	jobs[0].push_back(pos);
      }else if(s[0] == 'B'){
 	which.push_back(1);
	jobs[1].push_back(pos);
      }else{
	assert(false);
      }
    }
    
    jobs[0].push_back(1);
    jobs[1].push_back(1);
    
    int pos[2] = {1, 1};
    int job[2] = {0, 0};
    int ans = 1;

    for(int iJob = 0; ; ans++){
      int next = which[iJob];
      
      if(pos[1-next] < jobs[1-next][job[1-next]]){
	pos[1-next]++;
      }else if(pos[1-next] > jobs[1-next][job[1-next]]){
	pos[1-next]--;
      }else{
	//
      }
      
      if(pos[next] < jobs[next][job[next]]){
	pos[next]++;
      }else if(pos[next] > jobs[next][job[next]]){
	pos[next]--;
      }else{
	iJob++;
	job[next]++;
	if(iJob == nJobs)
	  break;
      }
    }
    
    printf("Case #%d: %d\n", iCase+1, ans);
  }
  return 0;
}
