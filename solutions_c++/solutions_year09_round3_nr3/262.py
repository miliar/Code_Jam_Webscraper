#include<iostream>
#include<algorithm>
# define MAXINT 1e9
using namespace std;
/*
int main()
{
	int p,q,n,i,j,k,z,ans,left,right;
	
	scanf("%d",&n);
	int arr[100];
	for(z=1;z<=n;z++)
	{
		ans=0;
		
		scanf("%d%d",&p,&q);
		left=1;
		right=p;
		for(i=0;i<q;i++)
		{
			scanf("%d",&arr[i]);
		}
		i=0;
		j=q-1;
		while(i<=j)
		{
			ans+=right-left;
			if(arr[i]-left>right-arr[j])
			{
				left=arr[i]+1;
				i++;
			}
			else
			{
				right=arr[j]-1;	
				j--;
			}
		}
		printf("Case #%d: %d\n",z,ans);
	}
}*/
















int main()
{
	int p,q,n,i,j,k,z,ans,left[101],right[101],sum;
	int fact;
	scanf("%d",&n);
	int arr[100];
	for(z=1;z<=n;z++)
	{
		ans=MAXINT;
		
		scanf("%d%d",&p,&q);
		fact=1;
		for(i=0;i<q;i++)
		{
			scanf("%d",&arr[i]);
			
			fact*=(i+1);
		}
		for(i=0;i<fact;i++)
		{
			sum=0;
			for(j=0;j<q;j++)
			{
				left[arr[j]]=1;
				right[arr[j]]=p;
			}
			for(j=0;j<q;j++)
			{
				sum+=right[arr[j]]-left[arr[j]];
				for(k=0;k<q;k++)
				{
					if(k!=j)
					{
						if(arr[k]<arr[j])
						{
							right[arr[k]]=min(right[arr[k]],arr[j]-1);
						}
						else
						{
							left[arr[k]]=max(left[arr[k]],arr[j]+1);
						}
					}
				}
			}
			if(sum<ans)
				ans=sum;
			next_permutation(arr,arr+q);
		}
		printf("Case #%d: %d\n",z,ans);
	}
}

