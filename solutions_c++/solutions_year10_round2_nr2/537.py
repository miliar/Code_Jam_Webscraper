#include <iostream>

using namespace std;

int tc,N,K,B,T;
int ch[60];
int v[60];
int ans,sel;

int main()
{
 cin >> tc;
 for(int tt=0;tt<tc;tt++)
 {
  cin >> N >> K >> B >> T;
  ans = 0;
  
  for(int i=0;i<N;i++) cin >> ch[i];
  
  //fast forward
  for(int i=0;i<N;i++) {cin >> v[i]; ch[i] += (v[i]*T);}
  
  //Sort
  for(int i=0;i<K;i++)
  {
   //Greedy, Find Rightmost possible chick
   sel = -1;
   for(int ii=0;ii<N-i;ii++) if(ch[ii]>=B) sel = ii;
   
   if(sel==-1)
   {
    ans = -1;
    break;
   }
   else
   {
    for(int ii=sel;ii<N;ii++)
    {
     if(ii==N-1 || ch[ii+1]>=B) break;
     int temp = ch[ii+1];
     ch[ii+1] = ch[ii];
     ch[ii] = temp;
     ans++;
    }
   }
  }
  
  cout << "Case #" << tt+1 << ": ";
  if(ans==-1) cout << "IMPOSSIBLE"; else cout << ans;
  cout << endl;
 }
}
