#include <stdio.h>
#include <queue>

#define input "input.in"
#define output "output.out"

using namespace std;

queue<long> MyCoada;
queue<long> CoadaAux;

long n,x,CntTeste,r,k,rez;

int main()
{	
	freopen(input,"r",stdin);
	freopen(output,"w",stdout);

	scanf("%d",&CntTeste);

	for (long t=1;t<=CntTeste;t++)
	{
		while (MyCoada.empty()==false)
			MyCoada.pop();

		scanf("%ld %ld %ld",&r,&k,&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%ld",&x);
			MyCoada.push(x);
		}		

		rez=0;

		for (int i=1;i<=r;i++)
		{
			int sum=0;			

			while (MyCoada.empty()==false && sum+MyCoada.front()<=k)
			{	
				sum+=MyCoada.front();
				CoadaAux.push(MyCoada.front());
				MyCoada.pop();
			}		

			while (!CoadaAux.empty()) 
			{
				MyCoada.push(CoadaAux.front());
				CoadaAux.pop();
			}

			rez+=sum;
		}

		printf("Case #%ld: %ld\n",t,rez);
	}

	return 0;
}