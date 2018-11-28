# include <iostream>
using namespace std;
# include <stdio.h>
int main()
{int cases,count=1,i,j;
long long int no,size,limit,sum,pay,cap;
long long int group[10000];
scanf("%d",&cases);
while(cases--)
{j=0;
pay=0;
	scanf("%lld",&no);
	scanf("%lld",&limit);
	scanf("%lld",&size);
sum=0;
for(i=0;i<size;i++)
{
scanf("%lld",&group[i]);
sum+=group[i];
}
i=0;

	while(i<no)
	{
		cap=0;
		if(sum<=limit)
		{
			cap+=sum;
		}
		else
		{
			while(1)
			{
				if(cap+group[j%size]<=limit)
				{
					cap+=group[j%size];

					j++;
					//printf("here %d",j);
				}
				else
				break;
            }
		}

		pay+=cap;
		i++;
	}




	cout<<"Case #"<<count<<":"<<pay<<"\n";
	count++;

}

}
