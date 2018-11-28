#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 100
using namespace std;
int main()
{
	int i,j,m=1, count=0;
	char a[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};
	char b[27]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
	char var[3000];
	int n;	
	freopen("A-small-attempt4.in","r",stdin);
	freopen("output","w",stdout);
	scanf("%d\n", &n);
	printf("Case #%d: ", m);					
		scanf("%[a-z \n]s", var);					
		for(i=0; i<3000;i++)
		{			
			if(count>=n)
			break;			
			if(var[i]=='\n')
			{			
			printf("\n");
			count++;
			if(count<n)				
			printf("Case #%d: ", ++m);			
			}			
			else
			for(j=0; j<27; j++)			
			if(var[i]==b[j])
			printf("%c", a[j]);
		}

}
			
