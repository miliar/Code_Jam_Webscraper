#include <cstdio>
#include <vector>

using namespace std;

int t;
int cas;
int n;
int onow;
int bnow;
int ans;

struct Node
{
	int color;
	int step;
};

vector <Node> order;


int sub(int x,int y)
{
	if(x > y)
		return x - y;
	else
		return y - x;
}



void init()
{
	int i;
	char tc;
	int td;
	ans = 0;
	bnow = onow = 1;
	order.clear();
	scanf("%d",&n);

	for(i = 1;i <= n;i++)
	{
		scanf(" %c %d",&tc,&td);
		Node tmp ;
		tmp.color = tc;
		tmp.step = td;
		order.push_back(tmp);
	}
}


int cal(char clo,int pos)
{
	int res = 0;
	if(clo == 'O')
	{
		res += sub(onow,pos);
		res ++;
		onow = pos;
		
	}
	else
	{
		res += sub(bnow,pos);
		res ++;
		bnow = pos;
	}

	return res;

}

void work()
{
	vector <Node>::iterator it;
	Node tmp;
	char precolor = 'x';
	int precost = 0;
	int cost;
	int leiji = 0;
	for(it = order.begin();it != order.end();it ++)
	{
		cost = cal((*it).color,(*it).step);
		if((*it).color != precolor)
		{
			if(leiji >= cost)
			{
				ans ++;
				leiji = 1;
			}
			else
			{
				ans += cost - leiji;
				leiji = cost - leiji;
			}
		//	leiji = cost - leiji;

		}
		else
		{
			leiji += cost;
			ans += cost;
		}

		printf("ans = %d\n",ans);
		precost = cost;
		precolor = (*it).color;
	
	}


}


int main()
{

	FILE *fout;
	fout = fopen("out.txt","wt");
	scanf("%d",&t);
	for(cas = 1;cas <= t;cas++)
	{
		init();
		work();
		printf("Case #%d: %d\n",cas,ans);
		fprintf(fout,"Case #%d: %d\n",cas,ans);
	}	

	return 0;
}
