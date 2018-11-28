#include <iostream>
#include <cstring>
using namespace std;

#define SIZE 5000+10
#define MAX 500+10

int L,D,N;
char dict[SIZE][SIZE], token[MAX];
bool valid[SIZE];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    int t,i,j,k,len,tk,count;
    char ch,ctok[28];		//current token
    
    scanf("%d %d %d",&L,&D,&N);		//header input
    
    for(i=1;i<=D;i++)				//input dictionary
    {
    	scanf("%s",dict[i]);
    	//printf("%s\n",dict[i]);
	}
	//printf("\n\n");
    for(t=1;t<=N;t++)				//testcases
    {
		memset(valid,1,sizeof(valid));
		scanf("%s",token);
		tk=0;
		count=0;
		for(i=0;i<L;i++)		//for each token
		{
			//get the current token
			if(token[tk]!='(')
			{
				ctok[0] = token[tk];
				ctok[1] = '\0';
				len = 1;
				tk++;
			}
			else
			{
				tk++;
				k=0;
				while(token[tk]!=')')
				{
					ctok[k] = token[tk];
					tk++;
					k++;
				}
				ctok[k] = '\0';
				tk++;
				len = strlen(ctok);
			}
			//printf("current token %s\n",ctok);
			
			//find position
			for(j=1;j<=D;j++)
			{
				if(!valid[j])
					continue;
				ch = dict[j][i];		//i'th char of j'th word
				for(k=0;k<len;k++)
				{
					if(ctok[k]==ch)
						break;
				}	
				if(k==len)
				{
					valid[j]=false;
					count++;
					//printf("false : %s\n",dict[j]);
				}
			}
		}
		printf("Case #%d: %d\n",t,D-count);	//print output
	}
	
    return 0;
}
