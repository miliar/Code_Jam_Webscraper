#include<cstdio>
#include<queue>
using namespace std;
queue<int> global,q1,q2;
long int count,res[1000];
void function()
{
	int push,v1,v2,cont;
	int curro=1,currb=1;
	count=0;
	if(!q1.empty())
	{	
	v1=q1.front();
	q1.pop();
	}
	else
	v1=1;
	if(!q2.empty())
	{
	v2=q2.front();
	q2.pop();
	}
	else
	v2=1;
	while(!global.empty())
	{
		push=global.front();
		global.pop();
		cont=1;
		while(cont==1)
		{
			count++;
			if(push==1)
			{
				if(v1==curro)
				{
					if(!q1.empty())
					{
					v1=q1.front();
					q1.pop();
					}
					cont=0;
				}
				else if(v1>curro)
					curro++;
				else
					curro--;
				if(v2>currb)
					currb++;
				else if(v2<currb)
					currb--;	
			
			}
			if(push==2)
			{
				if(v2==currb)
				{
					if(!q2.empty())
					{
					v2=q2.front();
					q2.pop();
					}
					cont=0;
				}
				else if(v2>currb)
					currb++;
				else
					currb--;
				if(v1>curro)
					curro++;	
				else if(v1<curro)
					curro--;
			
		
			}
		}
	}
	return;
	//printf("%d\n",count);	
}

int main()
{
	int num_cases,cas,n,i,v;
	char c;
	scanf("%d",&num_cases);
	for(cas=1;cas<=num_cases;cas++)
	{
		
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf(" %c %d",&c,&v);
			if(c=='O')
			{
			global.push(1);
			q1.push(v);
			}
			else
			{
			global.push(2);
			q2.push(v);
			}
						
		}
	function();
	res[cas]=count;
	}
	for(i=1;i<=num_cases;i++)
		printf("Case #%d: %ld\n",i,res[i]);
	return 0;
}
