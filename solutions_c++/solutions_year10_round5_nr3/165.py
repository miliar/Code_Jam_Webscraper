#include<cstdio>
#include<map>

using namespace std;

int main(void)
{
  map<int, int> vendedores;
  map<int, int>::iterator it;
  int t, caso = 1, c, v, p, f, nm;
  long long int m;
  
  scanf("%d", &t);
  
  while(caso <= t)
  {
    scanf("%d", &c);
    vendedores.clear();
    f = 0;
    m = 0;
    
    for(int i = 0; i < c; i++)
    {
      scanf("%d %d", &p, &v);
      
      if(v >= 2) f = 1;
      
      if(vendedores.find(p) != vendedores.end()) vendedores[p] += v;
      else vendedores[p] = v;
    }
    
    while(f == 1)
    {
      f = 0;
      
      for(it = vendedores.begin(); it != vendedores.end(); ++it)
      {
	if(it->second <= 1) continue;
	
	f = 1;
	
	nm = it->second / 2;
	m += nm;
	
	if(it->second % 2 == 0) it->second = 0;
	else it->second = 1;
	
	if(vendedores.find((it->first - 1)) != vendedores.end()) vendedores[(it->first - 1)] += nm;
	else vendedores[(it->first - 1)] = nm;

	if(vendedores.find((it->first + 1)) != vendedores.end()) vendedores[(it->first + 1)] += nm;
	else vendedores[(it->first + 1)] = nm;
      }
    }
    
    printf("Case #%d: %lld\n", caso, m);
    caso++;
  }
  
  
  
  
  
  return 0;
}