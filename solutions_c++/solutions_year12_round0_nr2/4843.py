#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int check(int *total,int n,int s,int p)
{
	int fin=0,h,temp;

	for(h=0;h<n;++h)
		{
			temp=*(total+h);
			if(s)
			{
				if((temp-2)%3==0 && (temp-2)>=0) //Lin Eqn: x+2 + 2x = temp =>x=(temp-2)/3
				{
					--s;
					if(   (2 + ((temp-2)/3))  >=p)
					{
						fin+=1;
					}
					goto done;
				}
				else if( ((temp-3)%3)==0 && (temp-3)>=0)  //x + x+1 + x+2= temp  => x=(temp-3)/3
				{
					if( (2+((temp-3)/3)) >=p)
						fin+=1;
					--s;
					goto done;
				}
				else if( ((temp+2)%3)==0 && (temp+2)>=0)  //x + x + x-2= temp  => x=(temp+2)/3
				{
					if( ((temp+2)/3) >=p)
						fin+=1;
					--s;
					goto done;
				}
			}

			non_s:
			{
				if((temp)%3==0)
							{
								if(  (temp/3) >=p)
								{
									fin+=1;
								}
								goto done;
							}
							else if( ((temp-2)%3)==0 && (temp-2)>=0)  //x + x+1 + x+1= temp  => x=(temp-2)/3
							{
								if( (1+((temp-2)/3)) >=p)
									fin+=1;
								goto done;
							}
							else if( ((temp-1)%3)==0 && (temp-1)>=0)  //x + x+1 + x= temp  => x=(temp-1)/3
							{
								if( (1+ ((temp-1)/3)) >=p)
									fin+=1;
								goto done;
							}
			}
			done:
			continue;
		}
		return fin;
}

	int main()
	{
	int num_t,n,s,p,fin_temp,fin_max;
	int total[3];
	int h;
	scanf("%d",&num_t);
	for(int l=1;l<=num_t;++l)
	{
		fin_max=fin_temp=0;

		scanf("%d %d %d",&n,&s,&p);

		for(h=0;h<n;++h)
			scanf("%d",total+h);

		sort(total,total+n);

		do
		{
			fin_temp=check(total,n,s,p);
			if(fin_temp>fin_max)
					fin_max=fin_temp;
			if(fin_max==n)
				break;
		}
		while(next_permutation(total,total+n));

		printf("Case #%d: %d\n",l,fin_max);

	}
	return 0;
}
