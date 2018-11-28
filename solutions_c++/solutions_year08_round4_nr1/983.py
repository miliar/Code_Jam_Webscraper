#include <iostream>
using namespace std;
const int MAXN = 2000,INF=4000;
int leafNode[MAXN],value[MAXN],G[MAXN],C[MAXN];
int memo[MAXN][3];

int is_leaf(int node)
{
   return leafNode[node];
}


int rec(int curNode, int parity)
{

   if(is_leaf(curNode)) {
      if(parity==value[curNode]) return 0;
      return INF;
   }

   int &ret = memo[curNode][parity];

   if(ret!=-1) return ret;

   ret=INF;
   if(C[curNode]) {
      for(int i=0;i<2;i++) for(int j=0;j<2;j++) {
         if((i&j)==parity) {
            int cur=rec(curNode*2,i)+rec(curNode*2+1,j)+(G[curNode]!=1);
            ret=min(ret,cur);
         }
      }
      for(int i=0;i<2;i++) for(int j=0;j<2;j++) {
         if((i|j)==parity) {
            int cur=rec(curNode*2,i)+rec(curNode*2+1,j)+(G[curNode]!=0);
            ret=min(ret,cur);
         }
      }
   }
   else {
      if(G[curNode]) {
         for(int i=0;i<2;i++) for(int j=0;j<2;j++) {
            if((i&j)==parity) {
               int cur=rec(curNode*2,i)+rec(curNode*2+1,j);
               ret=min(ret,cur);
            }
         }


      }
      else {
            for(int i=0;i<2;i++) for(int j=0;j<2;j++) {
               if((i|j)==parity) {
                  int cur=rec(curNode*2,i)+rec(curNode*2+1,j);
                  ret=min(ret,cur);
               }
            }
      }
   }

   return ret;


}


int main()
{
   freopen("A-small-attempt0.in","r",stdin);
   freopen("test.out","w",stdout);
   int N;
   cin>>N;
   for(int tc=1;tc<=N;tc++) {
      memset(leafNode,0,sizeof(leafNode));
      memset(memo,-1,sizeof(memo));

      int M,V;
      cin>>M>>V;
      for(int i=1;i<=(M-1)/2;i++) {
         cin>>G[i]>>C[i];
      }
      for(int i=((M-1)/2)+1;i<=M;i++) {
         leafNode[i]=1;
         cin>>value[i];
      }

      int ret=rec(1,V);
      cout<<"Case #"<<tc<<": ";
      if(ret==INF) cout<<"IMPOSSIBLE"<<endl;
      else cout<<ret<<endl;


   }

   return 0;
}
