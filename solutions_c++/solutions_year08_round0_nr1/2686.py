#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int se, sq;
vector<string> engines(110);

int appearances[110], sum, x, x_prev;

int main(int argc, char *argv[])
{
	int Q;
	char temp[200];
	
	scanf("%d\n", &Q);
	for(int q=0; q<Q; q++)
	{		
		x=0;
		sum=0;
		for(int i=0;i<110;i++) appearances[i]=0;
		
		scanf("%d\n", &se);
		for(int r=0; r<se; r++)
		{
			scanf("%[0-9a-zA-Z ]\n", &temp);
			engines[r]=temp;
			
		}
		
		scanf("%d\n", &sq);
		for(int r=0; r<sq; r++)
		{
			scanf("%[0-9a-zA-Z ]\n", &temp);
			
			for(int i=0;i<se;i++)
			{
				if(!engines[i].find(temp))
				{
					if(appearances[i]==x)
					{
						appearances[i]++;
						sum++;
						if(sum == se)
						{
							sum=1;
							x++;
							appearances[i]++;
						}
					}
				}
			}
		}
		
		//printf("Case #%d: %d\n",q+1,x==0?0:1);
		printf("Case #%d: %d\n",q+1,x);
	}
	
    return EXIT_SUCCESS;
}
