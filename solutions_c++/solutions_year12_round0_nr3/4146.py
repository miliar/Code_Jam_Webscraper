#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int A,B;
int count;
bool used[2000005];

void getLeagle(int num)
{
	int i = 10;

	while(num/i)
	{
		int front = num/i;
		int back = num%i;

		if(back*10 >= i)
		{
			int length = 1;
			int temp = front;
			while(temp)
			{
				temp /=10;
				length = length*10;
			}

			int result = back*length + front;
			if(result <= B && result > num)
			{
				if(!used[result])
				{
					used[result] = true;
					count++;
				}
			}
		}

		i = i*10;
	}
}

int main()
{
	freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
	int cases;
	cin>>cases;
	for(int i = 1;i<=cases; i++)
	{
		count = 0;
		
		cin>>A>>B;
		for(int j = A;j<=B;j++)
		{
			memset(used,0,sizeof(used));
			getLeagle(j);
		}

		cout<<"Case #"<<i<<": "<<count<<endl;


	}
	return 0;
}