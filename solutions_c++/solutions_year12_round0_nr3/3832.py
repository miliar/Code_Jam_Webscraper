#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int count[2000001][10];

int diginInNum(int i)
{
	int count=0;
	if(i==0) return 1;
	while(i!=0)
	{
		i/=10;
		count++;
	}
	return count;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int t,i,a,b,k,c,p,m,n,len,case_no=0,new_num,index,d1,d2;
	char num[10],temp_num[10];
	

	for( i=2000000; i>=1; i-- )
	{
		n = i;
		index = 1;
		
		m = n;
		itoa(m,num,10);
		len = strlen(num);
		d1 = diginInNum(n);
		
		for(k=1;k<=len;k++)
		{
			c=0;
			for( p = len-k; p<len ;p++ )
				temp_num[c++] = num[p];
			for( p = 0; p<len-k;p++ )
				temp_num[c++] = num[p];
			temp_num[c] = 0;
			new_num = atoi(temp_num);
			if( n ==  new_num) break;
			d2 = diginInNum(new_num);
			
			if(  new_num < n && (d1 == d2) )
			{
				count[i][index++] = new_num;
			}
		}
		count[i][0] = index;

		memset(num,0,sizeof(num));
		memset(temp_num,0,sizeof(temp_num));
	}

//	printf("done\n");

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&a,&b);
		c = 0;
		for( i=a; i<=b; i++)
		{
			for( k=1; k<count[i][0]; k++)
			{
				if( count[i][k] >= a ) c++;
			}
		}
		printf("Case #%d: %d\n",++case_no,c);
	}

	return 0;
}