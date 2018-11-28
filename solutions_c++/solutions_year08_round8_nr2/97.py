#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

#define MAX_I 10000
#define MAX_N 305

void input(void);
void solve(void);

int n, m;
int A[MAX_N];
int B[MAX_N];
int C[MAX_N];
map <string, vector <int> > id;
vector <vector <int> > Z;
int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  char buf[333];
     
  id.clear();
  
  scanf("%d", &n);
  for(int i = 0; i < n; i++) {
    int a, b;
    scanf(" %s %d %d", buf, &a, &b);
    A[i] = a;
    B[i] = b;
    id[buf].push_back(i);
  }
}

void solve(void)
{
  Z.clear();
  for(map <string, vector <int> >::iterator it = id.begin(); it != id.end(); it++) 
    Z.push_back(it->second);
    
  
  int ans = -1;
  
  m = Z.size();
  for(int i = 0; i < m; i++)
    for(int j = i; j < m; j++)
      for(int k = j; k < m; k++) {
        vector <pair <int, int> > temp;
        
        for(vector <int>::iterator it = Z[i].begin(); it != Z[i].end(); it++) 
          temp.push_back(make_pair(A[*it], B[*it]));
          
        for(vector <int>::iterator it = Z[j].begin(); it != Z[j].end(); it++) 
          temp.push_back(make_pair(A[*it], B[*it]));
          
        for(vector <int>::iterator it = Z[k].begin(); it != Z[k].end(); it++) 
          temp.push_back(make_pair(A[*it], B[*it]));
          
        sort(temp.begin(), temp.end());
        
        int last = 0;
        int pos = 0;
        int cnt = 0;
        priority_queue <int> Q;
        for( ; ; ) {
          while(pos < temp.size() && temp[pos].first <= last + 1) { Q.push(temp[pos].second); pos++; }
          if(Q.empty()) break;
          cnt++;
          last = Q.top(); 
          Q.pop();
          if(ans != -1 && cnt > ans) break;
          if(last >= MAX_I) { ans = cnt; break; }
          if(pos >= temp.size()) break;
        }
      } 
      
    printf("Case #%d: ", case_cnt++);
    if(ans == -1) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
}


    

