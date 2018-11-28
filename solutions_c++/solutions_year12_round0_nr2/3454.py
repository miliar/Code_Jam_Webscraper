#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int m,n,s,p,sum,liczba=0;
	scanf("%d\n",&m);
	for(int i=0; i<m; i++)
	{
		liczba=0;
		scanf("%d %d %d",&n,&s,&p);
		for(int j=0; j<n; j++)
		{
			bool czy=false;
			scanf("%d",&sum);
			if( (sum % 3 == 0) && (sum/3 >= p))
				czy=true;		
			else
			if((sum % 3 == 2) && ((sum+1)/3>=p))
				czy=true;
			 else
			if((sum %3 ==1) && ((sum+2)/3>=p))
				czy=true;
			if(czy==false && s>0)
			{
				if((sum % 3 == 0) && ((sum+3)/3>=p) && ((sum+3)/3>=2))
				{
					czy=true;
					--s;
				} else
				if((sum % 3 == 1) && ((sum+2)/3>=p) && ((sum+2)/3>=2))
				{
					czy=true;
					--s;
				} else
				if((sum % 3 ==2 ) && ((sum+4)/3>=p) && ((sum+4)/3>=2))
				{
					czy=true;
					--s;
				}
			}
			
			if(czy==true)
				++liczba;
		}
		printf("Case #%d: %d\n",i+1,liczba);
	}
		return 0;
}
