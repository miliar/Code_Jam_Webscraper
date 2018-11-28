/*
Dinesh Reddy
National Institute of Technology,Warangal.
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	int index[]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
	if(t==0)
		return 0;
	printf("Case #1: ");
	int i=1;
	char c;
	c=getchar();
	while(1)
	{
		c=getchar();
		if(c=='\n')
		{
			t--;
			i++;
			printf("\n");
			if(t==0)
				break;
			printf("Case #%d: ",i);
		}
		else if(c==' ')
			printf(" ");
		else
		{
			printf("%c",(char)('a'+index[c-'a']));
		}
	}
	return 0;
}
