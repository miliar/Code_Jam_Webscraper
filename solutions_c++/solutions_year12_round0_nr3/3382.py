#include<stdio.h>
# include <string.h>
# include <stdlib.h>
#include<math.h>
using namespace std;

int areRotations(char *str1, char *str2)
{
  int size1   = strlen(str1);
  int size2   = strlen(str2);
  char *temp;
  void *ptr;
 
  /* Check if sizes of two strings are same */
  if(size1 != size2)
     return 0;
 
  /* Create a temp string with value str1.str1 */
  temp   = (char *)malloc(sizeof(char)*size1*2 + 1);
  temp[0] = '\0';
  strcat(temp, str1);
  strcat(temp, str1);
 
  /* Now check if str2 is a substring of temp */
  ptr = strstr(temp, str2);
 
  /* strstr returns NULL if the second string is NOT a
    substring of first string */
  if(ptr != NULL)
    return 1;
  else
    return 0;
}

int rotate(int num,int dig)
{
	int d = num%10;
	num = num/10;
	int ans = num+(pow(10,dig-1)*d);
	return ans;
}

int isrotate(int a,int b,int num)
{
	int i;
	int temp=num;
	while(num--)
	{
	if(a==b)
	return 1; 
	a=rotate(a,temp);
	}
	return 0;
}
		
	


int main()
{
    freopen ("C-small-attempt0.in","r",stdin);
    freopen ("out.txt","w",stdout);
	int no,a,b,num,i,j;
	scanf("%d",&no);
int c=1;
	while(no--)
	{
 
		scanf("%d %d",&a,&b);
		if(a<10)
		num=1;
		if(a>=10 && a<=99)
		num=2;
		if(a>=100 && a<=999)
		num=3;
		int temp = num;
		int ans=0;
		for(i=a;i<=b;i++)
		{
			for(j=a;j<=b;j++)
			{
			char aa[10],bb[10];
			//itoa(i, aa, 10);
			//itoa(j, bb, 10);8
			if(i==j)
			continue;
			sprintf(aa,"%d",i);
			sprintf(bb,"%d",j);

				if(areRotations(aa,bb))
				{
				ans++;
				//printf("%s %s\n",aa,bb);
				}
			}
		}
		
		printf("Case #%d: %d\n",c++,ans/2);
		
	}
}		
		
		
		
