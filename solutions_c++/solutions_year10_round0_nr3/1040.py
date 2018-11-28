#include<fstream>
using namespace std;

int main()
{
	ifstream cin("\C-small-attempt1.in");
	ofstream cout("\C-small-attempt1.out");
	int t,cn,i,r,k,n,Q[200001];
	int front,rear,sum,cnt,temp;
	cin>>t;
	for(cn=1;cn<=t;cn++)
	{
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
			cin>>Q[i];
		cnt = 0;
		front = 0; rear = n;
		while(r--)
		{
			sum = 0;
			temp = rear;
			while(front<temp && sum+Q[front]<=k)
			{
				sum += Q[front];
				Q[rear++] = Q[front];
				front ++;
			}
			cnt += sum;
		}
		cout<<"Case #"<<cn<<": "<<cnt<<"\n";
	}
}
