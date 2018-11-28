#include<iostream>

using namespace std;

int main()
{
int i,j,k,found,match,t,h,n;
char temps[25],nums[25],temp;

cin>>t;
for(h=1;h<=t;h++)
{
found=0;
i=0;
scanf("%s",nums);
while(nums[i]!='\0')
	i++;
//cout<<i;
for(j=i-1;j>0;j--)
{
	if(nums[j-1]<nums[j])
	{
		if(nums[j-1] == '0')
		{
			for(k=i-1;;k--)
			if(nums[k] !='0')
				{temp=nums[j-1];
			nums[j-1]=nums[k];
			nums[k]=temp;
			break;
			}
			//reversenum(nums,j,i-1);
			for(k=j;k<=i-1;k++)
				temps[i-1+j-k]=nums[k];
			for(k=j;k<=i-1;k++)
				nums[k]=temps[k];
		}
		else
		{//cout<<"ok"<<j;
			
			temp=nums[j-1];
			for(k=i-1;;k--)
			if(nums[k] > temp)
				{
					temp=nums[j-1];
					nums[j-1]=nums[k];
					nums[k]=temp;
					break;
				}
			for(k=j;k<=i-1;k++)
				temps[i-1+j-k]=nums[k];
			for(k=j;k<=i-1;k++)
				nums[k]=temps[k];
/*
			if(temps[i-1] > temp)
			{
				match=1;	
				for(k=j+1;k<=i;k++)
				{	
					if(match==0)
						nums[k-1]=temps[k-1];
					if((temps[k] < temp)&&(match==1))
						nums[k-1]=temps[k];
					else if((temps[k] >temp)&&(match==1))
						{nums[k-1]=temp; match=0;}
				
				}
			}
			else
			{
				for(k=j+1;k<i;k++)
					nums[k-1]=temps[k];
				nums[i-1]=temp;
			}*/
			//printf("%s",nums);
		}
		found=1;
		break;
	}
}

if(found == 0)
{
	for(k=0;k<=i-1;k++)
		temps[i-k]=nums[k];
	k=1;
	while(temps[k]=='0')
		k++;
	temps[0]=temps[k];
	temps[k]='0';
	for(k=0;k<=i;k++)
		nums[k]=temps[k];
	nums[i+1]='\0';
}

printf("Case #%d: %s\n",h,nums);
}
}
