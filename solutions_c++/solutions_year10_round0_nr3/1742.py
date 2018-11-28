#include<cstdio>
int v[1000],r,k,n,cycle_len;

struct ride
{
	int v[1000];
	int len;
	int sum;
} cycle[10000];

//checks if we got the cycle
int isCycle(int index)
{
	int j,ok;
	for(int i=0;i<index;i++)
	{
		if(cycle[i].len==cycle[index].len)
		{
			ok=1;
			for(j=0;j<cycle[i].len;j++)
				if(cycle[i].v[j]!=cycle[index].v[j])
					{
						ok=0;
						break;
					}
			if(!ok) continue;
			return i;
		}

	}
	return -1;
}

int main()
{
	int t,i,ret,left,current_i,j,sum,fix_sum,cycle_sum,len,h;

	FILE *f=fopen("C-small.in","r");
	FILE *g=fopen("C-solve.out","w");
	fscanf(f,"%d",&t);

	for(h=1;h<=t;h++)
	{
		//read test case
		fscanf(f,"%d %d %d",&r,&k,&n);

		for(i=0;i<n;i++)
			fscanf(f,"%d",&v[i]);

		//find the cycle
		cycle_len=0; i=0;
		do
		{
			current_i=i;
			left=k;
			cycle[cycle_len].len=0;
			cycle[cycle_len].sum=0;
			while(left>=v[i])
			{
				left-=v[i];
				cycle[cycle_len].v[cycle[cycle_len].len++]=i;
				cycle[cycle_len].sum+=v[i];
				i++;
				if(i==n) i=0;
				if(i==current_i) break;
			}
			if(r<cycle_len) break;
		} while(ret=isCycle(cycle_len++) == -1); //a cycle has been found
		//the elements between cycle[ret] and cycle[cycle_len-2] forms the cycle
		//elements from cycle[0] to cycle[ret-1] are a fixed sequence which only occurs first time

		sum=0;
		if(r<cycle_len)
		{
			for(i=0;i<r;i++)
				sum+=cycle[i].sum;
		}
		else
		{
			fix_sum=0; //fix part sum
			ret=isCycle(cycle_len-1);

			for(i=0;i<ret;i++)
				fix_sum+=cycle[i].sum;

			cycle_sum=0; //cycle sum
			len=cycle_len-ret-1; // cycle length

			for(i=ret;i<cycle_len-1;i++)
				cycle_sum+=cycle[i].sum;
		
			r-=ret;

			sum=fix_sum;
			sum+=(cycle_sum*(r/len));
		
			for(i=ret;i<ret+(r%len);i++)
				sum+=cycle[i].sum;

		}

		fprintf(g,"Case #%d: %d\n",h,sum);
	}

	fclose(f);
	fclose(g);
	return 0;
}