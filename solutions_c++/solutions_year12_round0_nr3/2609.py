#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int main() 
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
    int T,i,j,k;

	scanf("%d", &T);
	for(i=1; i<=T; i++)
	{
		int A,B,res=0,div=1, len=0;
		scanf("%d%d",&A,&B);
		j = A;
		while (j)
		{
			len++;
			j /= 10;
			div *= 10;
		}

		div /= 10;

		for(j=A;j<=B;j++)
		{
			int n,m,shiftn,arr[10] = {0},count=0;
			n=j;
			for(k=1;k<=len-1;k++,n=shiftn)
			{
				shiftn = (n%div)*10 + (n/div);
				if(shiftn<=j || shiftn > B) continue;
				int ii;
				int tag = 0;

				for(ii=1;ii<=k && arr[ii];ii++)
				{
						if(arr[ii]==shiftn)
						{
							tag = 1;
							break;
						}
				}

				if(tag==0)
				{
					arr[ii] = shiftn;
					count++;
				}
			}
			res+=count;
		}
		printf("Case #%d: %d\n", i, res);
	}
    return 0;
}