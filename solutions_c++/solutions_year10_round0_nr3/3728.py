#include <iostream>
#include <queue>
using namespace std;
int main()
{
	queue<int>a;
	int n=1,T,K,R,N,i,g,money,m,j;
	freopen("g:\\C-small-attempt1.in","r",stdin);
	freopen("g:\\input.txt","w",stdout);
	cin>>T;
	while(n!=T+1)
	{
		money=0;
		cin>>R>>K>>N;
		for(i=0;i<N;i++)
		{
			cin>>m;
			a.push(m);
		}
		i=0;
		while(i<R)
		{
			g=0;
			j=0;
			while(j<N)
			{
				
				m=a.front();
				g+=m;
				if(g<=K)
				{
					a.pop();
					j++;
					a.push(m);
					money+=m;
				}
				else break;
			}
			i++;
		}
		cout<<"Case #"<<n<<": "<<money<<endl;
		n++;
		while(!a.empty())
			a.pop();
	}
	return 1;
}