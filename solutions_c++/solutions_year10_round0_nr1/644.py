#include<iostream>
using namespace std;
int cas;
int main()
{

	int cc=0,n,k,s;
//	 freopen("C://A-small-attempt0.in","r",stdin);
 //   freopen("C://out.txt","w",stdout);
	scanf("%d",&cas);
	while(cas--)
	{
		cc++;

		scanf("%d%d",&n,&k);
      
		s=(1<<n);
        s=k%s;
        if(s==((1<<n)-1))
        {
           printf("Case #%d: ON\n",cc);
			
        }
        else
        {
             printf("Case #%d: OFF\n",cc);
        }
	}
	return 0;
}




