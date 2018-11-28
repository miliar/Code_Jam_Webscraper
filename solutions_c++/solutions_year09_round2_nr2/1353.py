#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
	int i,cases,num,med;
	int list[100],sz;
	
	scanf("%d",&cases);
	
	for(int k=1;k<=cases;k++)
	{
		scanf("%d",&num);
		int temp=num;
		sz=0;
		list[sz++]=0;
		while(num)
		{
			list[sz++]=num%10;
			num/=10;
		}
		sort(list,list+sz);
		
		while(1)
		{
			next_permutation(list,list+sz);
			med=0;
			for(i=0;i<sz;i++) med=10*med+list[i];
			
			if(med==temp)
			{
				next_permutation(list,list+sz);
				med=0;
				for(i=0;i<sz;i++) med=10*med+list[i];
				break;
			}
		}
		printf("Case #%d: %d\n",k,med);
	}

	return 0;
}
	
	
	
