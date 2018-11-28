#include <iostream>

using namespace std;

int main()
{
	int T, i, j;
	cin>>T;
	
	for (i = 0; i < T; i++)
	{
		int N, S, p, temp, num=0;
		cin>>N>>S>>p;
		
		for (j = 0; j < N; j++)
		{
			cin>>temp;
			if(p == 0)
				num++;
			else if(p == 1 && temp >0)
				num++;
			else if(temp < p)
				continue;
			else if((temp == p+p-2+p-2 || temp == p+p-1+p-2) && S>0)
			{
				num++;
				S--;
			}
			else if(temp > (3*p) - 3)
			{
				num++;
			}
					
			
		}
		cout<<"Case #"<<i+1<<": "<<num<<endl;
	}
	return 0;
}
