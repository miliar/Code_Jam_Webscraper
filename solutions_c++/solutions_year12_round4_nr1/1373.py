#include <iostream>
#include <queue>

using namespace std;

int T,N;
unsigned long d[10000],l[10000],D;
bool reachable;

void run(unsigned long dd, unsigned long ll, int nn)
{
	if (reachable)
		return;
	for (int i=nn+1;i<N;i++)
	{
		//if (ll*ll>(d[i]-dd)*(d[i]-dd)+l[i]*l[i])
		//if (l[i]>=d[i]-dd && dd+ll>=d[i])
		if (dd+ll>=d[i])
		{
			if (dd+ll>=D)
			{
				reachable = true;
				return;
			}
			else
			{
				if (d[i]-dd<l[i])
					run(d[i],d[i]-dd,i);
				else
					run(d[i],l[i],i);
			}
		}
		else
		{
			return;
		}
	}
	if (dd+ll>=D)
	{
		reachable = true;
		return;
	}
}

int main(int argc, char *argv[])
{
	int i,j,k;



	cin>>T;
	for (i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		cin>>N;
		for (j=0;j<N;j++)
		{
			cin>>d[j]>>l[j];
		}
		cin>>D;

		reachable = false;
		run(d[0],d[0],0);

		if (reachable)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}

	return 0;
}