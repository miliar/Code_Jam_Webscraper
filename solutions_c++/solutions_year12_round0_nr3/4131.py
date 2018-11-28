#include<stdio.h>
#include<math.h>
#include<hash_map>
int num_bit(int num)
{
	
	if(num==0)return 0;
	int n_bit=1,temp;
	temp=num/10;
	while(temp)
	{
		n_bit++;
		temp=temp/10;
	}
	return n_bit;
}

int process(int num,int max,int bit)
{
	int out=0;
	int temp=num;
	int low,high;
	stdext::hash_map<int,int> hash;
	for(int i=1;i<bit;i++)
	{
		low=temp%10;
		high=temp/10;
		temp=low*pow(double(10),bit-1);
		temp=temp+high;	
		if(temp<=max && temp>num && !hash[temp])
		{
			out++;
			hash[temp]=1;
		}
	}
	hash.clear();
	return out;
}

void main()
{
	FILE* file,*output;
	file=fopen("data\\C-small-attempt0.in","rb");
	output=fopen("data\\C-small-attempt0.in.output","wt");
	int n_count,n_A,n_B,n_bit;
	fscanf(file,"%d",&n_count);
	for(int i=0;i<n_count;i++)
	{
		fscanf(file,"%d",&n_A);
		fscanf(file,"%d",&n_B);
		n_bit=num_bit(n_A);
		int n_num=0;
		for(int j=n_A;j<=n_B;j++)
		{			
			n_num+=process(j,n_B,n_bit);
		}
		fprintf(output,"Case #%d: %d\n",i+1,n_num);
	}


	fclose(output);
	fclose(file);
}