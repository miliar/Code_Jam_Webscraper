#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;
bool iswin(int L,int S)
{
	//printf("%d %d\n",L,S);
	if(S==0)
		return 1;
	
	if(S+(L%S)!=L)
		if(!iswin(S+(L%S),S))
			return 1;
	if(!iswin(S,L%S))
		return 1;
	return 0;
	
}

int main()
{
	
	int T;
	scanf("%d",&T);
	int A1,A2,B1,B2;
	for(int t=1;t<=T;t++)
	{
		scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
		int count=0;
		for(int A=A1;A<=A2;A++)
			for(int B=B1;B<=B2;B++)
			{
				int L=max(A,B);
				int S=min(A,B);
				
				if(iswin(L,S))
					count++;
				
			}
		
		printf("Case #%d: %d\n",t,count);
		
	}
}