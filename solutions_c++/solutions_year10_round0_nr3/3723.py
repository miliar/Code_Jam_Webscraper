#include<stdio.h>
#include <queue>
#include<stdlib.h>

using namespace std;

queue<int> Cola;
queue<int>  up;

int main()
{
   int T, R, k, N, g, tmp, lana, aux, cont;
   cont = 1;
   scanf("%d", &T);
   while(T)
   {
      
      lana = 0;
	  tmp = 0;
      scanf("%d %d %d", &R, &k, &N);
	  while(N > 0)
	  {  
		 scanf("%d", &g);
		 Cola.push(g);
		 //printf("Metemos a la cola %d\n", g);
	     N--;
	  }
	  
	  while(R > 0)
	  {
	     //printf("Viaje %d\n", R);
	     tmp = 0;
	     while(tmp + Cola.front() <= k && !Cola.empty())
		 {	
			    aux = Cola.front(); 
				Cola.pop();
				tmp += aux;
				//printf("Metemos al carrito a %d\n", aux);
				up.push(aux);
		 }
		 lana += tmp;
		 while(!up.empty())
		 {
		    Cola.push(up.front());
			up.pop();
		 }
		 R--;
		 
	  }
	  
	  printf("Case #%d: %d\n", cont, lana);
	  while(!Cola.empty())
	  {
	     Cola.pop();  
	  }
      cont++;   
      T--;
   }

   return 0;
}