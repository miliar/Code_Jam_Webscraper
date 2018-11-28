#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>



int a,b;
//int dup[6];
int d=0;
void check(char ch[],int n);
//bool check1(int c);

int main()
 {
	int j;
    FILE *fip=fopen("C-large.in","r");
	FILE *fop=fopen("C-large.out","w");
	
	fscanf(fip,"%d",&j);
	for(int ite=0;ite<j;ite++){
        d=0;
		fscanf(fip,"%d %d",&a,&b);
		for (int i=a;i<b;i++)
		{
			char ch[8];
			int n=i;
			itoa(n,ch,10);
			check(ch,n);
		}
		
		fprintf(fop,"Case #%d: %d\n",ite+1,d);
	}
  return 0;
 }

void check(char ch[], int n)
{
	
	int dup[6]={0,0,0,0,0,0};
	int k=strlen(ch);
	
	int i=0;
	while(i<k-1)
	{
		char s[8];
		for(int j=0;j<k;j++)
		{
			s[j]=ch[(j+1+i)%k];
		}
		
		int c=atoi(s);

		if( c > n && c<=b &&
			c != dup[0] &&
			c != dup[1] &&
			c != dup[2] &&
			c != dup[3] &&
			c != dup[4] &&
			c != dup[5] )
		{
			     dup[i]=c;
			     d=d+1;
		   
		}
		i++;
	}
 
}

