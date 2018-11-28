#include<cstdio>
#include<algorithm>
#include<map>
using namespace std;

typedef pair<int,int> P;
map<P, bool> M;

bool rec(int a, int b){
  if(a == 0 || b== 0) return false;
  if(M.find(P(a, b)) != M.end())
    return !M[P(a,b)];
  
  bool ans = false;
  if(a < b) swap(a, b);
  if(a > b){
    ans = ans || rec(a%b, b);
    if(a > a%b + b) ans = ans || rec(a%b+b, b);
  }

  M[P(a,b)] = ans;
  return !ans;
}

int main(){
  int T;
  scanf("%d", &T);
  
  for(int ca = 0; ca < T; ca++){

    int a1,a2,b1,b2;
    scanf("%d%d%d%d",&a1, &a2, &b1, &b2);

    int ans = 0;
    for(int i = a1; i <= a2; i++)
      for(int j = b1; j <= b2; j++)
	if(!rec(i, j)) ans++;

    printf("Case #%d: %d\n",ca+1, ans);
    
  }
}
