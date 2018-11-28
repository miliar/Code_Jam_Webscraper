#include<iostream>
using namespace std;

int ch[51200];
int  g[51200];
int  v[51200];
int n; //number of points
int leaf;

int dfs(int p,int goal)
{
	int result=-1,t1,t2;
	if(p>=leaf)
	{
		if(v[p]==goal)
			return 0;
		return -1;
	}
	t1=dfs(p*2,goal);
	t2=dfs(p*2+1,goal);
	if(g[p]==1)
	{
		if(goal==0)
		{
			if(t1>=0 &&(result<0 ||t1<result) )
				result=t1;
			if(t2>=0 &&( result<0 || t2<result) )
				result=t2;
			return result;
		}
		else 
		{
			if(t1>=0 && t2>=0 )
				result=t1+t2;
			if(ch[p])
			{
				if(t1>=0 && (result<0 ||t1+1 <result ) )
					result=t1+1;
				if(t2>=0 && (result<0 ||t2+1<result) )
					result =t2+1;
			}
			return result;
		}

	}
	else
	{
		if(goal==0)
		{
			if(t1>=0 && t2>=0 )
				result=t1+t2;
			if(ch[p])
			{
				if(t1>=0 && (result<0 || t1+1<result))
					result=t1+1;
				if(t2>=0 && (result<0 || t2+1<result) )
					result=t2+1;
			}
			return result;
		}
		else
		{
			if(t1>=0 )
				result=t1;
			if(t2>=0 && (result<0 || t2<=result) )
				result=t2;
			return result;
		}
	}
	cout<<"ERROR"<<endl;
	return 0;
}




int main()
{

	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int i,j,k,num,seq,result,goal;
	cin>>num;
	for(seq=1;seq<=num;seq++)
	{
		cin>>n>>goal;
		for(i=1;i<=(n-1)/2;i++)
			scanf("%d %d",&g[i],&ch[i]);
		for(i=(n-1)/2+1;i<=n;i++)
			scanf("%d",&v[i]);
		leaf=(n-1)/2+1;
		result=dfs(1,goal);
		printf("Case #%d: ",seq);
		if(result<0)
			printf("IMPOSSIBLE\n");
		else printf("%d\n",result);
	}
	return 0;
}

