#include <string>
#include <cmath>
#include <queue>
#include <set>
#define MAX 8
using namespace std;
int N;
struct state
{
    int d;
    string s;
    state(int a, string b)
    {
        d =a ;
        s = b;
    }
};
string mat[MAX];
bool done(string s)
{
    for(int i = 0; i< N;i++)
      for(int j = i+1;j<N;j++)
       {
           if(mat[s[i] - '0'][j] =='1')return false;
       }
    return true;
}
int bfs(string s)
{
    queue<state> q;
    set<string> seen;
    seen.insert(s);
    q.push(state(0, s));

    while(!q.empty())
    {
        state cur = q.front(); q.pop();
        int cd= cur.d;
        string cs = cur.s;
        if(done(cs)){return cd; }
        for(int i=0;i<N-1;i++)
        {
            string ns = cs;
            swap(ns[i], ns[i+1]);
            if(seen.find(ns) == seen.end())
            {
                seen.insert(ns);
                q.push(state(cd +1, ns));
            }
        }
    }
    return -1;
}
int T;
char in[50];
int main()
{
   string begin ="012345678";
   scanf("%d", &T);
   for(int c = 1;c<=T;c++)
   {
        scanf("%d", &N);
        for(int i=0;i<N;i++)
        {
            scanf("%s", in);
            mat[i] = (string) in;
        }
        printf("Case #%d: %d\n",c, bfs(begin));
   }
}
