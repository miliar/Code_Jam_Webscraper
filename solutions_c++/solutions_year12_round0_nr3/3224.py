#include <iostream>
using namespace std;

int pow(int a,int b)
{
	int r=1;
	for(int i=0;i<b;i++)
		r*=a;
	return r;
}
int HowLong(int a)
{
	int digits = 0; while (a != 0) { a /= 10; digits++; }
	return digits-1;
}
void main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int N,A,B,answer = 0;
	scanf("%d",&N);

	for(int Case=0;Case<N;Case++)
	{
		scanf("%d %d",&A,&B);
		int howLong = HowLong(A);
		int generated;
		for(int i=A;i<=B;i++)
		{
			int tail,head,k,dontUse = 0;
			for(int j=0;j<howLong;j++)
			{
				k=pow(10,j+1);
				tail = i%k;
				if(tail/pow(10,j) !=0)
				{
					head = i/k;
					generated = tail*pow(10,howLong-j)+head;
					if(generated > i && generated<=B && generated != dontUse)
					{
						dontUse = generated;
						answer++;
					}
				}

			}
		}

		printf("Case #%d: %d\n",Case+1,answer);
		answer = 0;
	}
}