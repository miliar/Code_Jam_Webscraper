#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <fstream.h>

#include <string.h>

using namespace std;



/*int getDigit(int num)
{
	int j=0,d,r;
	while(num > 9)
	{
		r = num%10;
		num = num/10;
		dig[j] = r;
		j++;
	}
	dig[j] = num;
	return j;
}*/

int myPow(int x, int po) 
{
  if (po == 0) return 1;
  if (po == 1) return x;
  return x * myPow(x, po-1);
}

int main()
{
		
	FILE *in,*out;
 	in=fopen("C-small-attempt0.in","r");
    out=fopen("C-small.out","w");	

	int t1, tt;
	
	fscanf(in,"%d\n", &tt );
	for( t1 = 1; t1 <= tt; ++ t1 )
	{
		fprintf(out,"Case #%d: ", t1 );
        
		int A,B;
		
		
		fscanf(in,"%d %d",&A,&B);
		
		int result = 0, count1=0;
		for(int i = A; i<= B; i++)
		{
		
			if(i>10)
			{
				int dig[1000];
				int j=0, r, num=i;
				while(num > 9)
				{
					r = num%10;
					num = num/10;
					dig[j] = r;
					j++;
				}
				dig[j] = num;
								
			
				int len = j+1; //getDigit(i);
				int p = len;
				int c =0;
				j=0;
				
				for(int k = 0; k< len-1; k++)
				{
					//fprintf(out,"%d", dig[k] );
					if(dig[k] != 0)
					{
						//fprintf(out,"%d", dig[k] );
						int term2 = p;
						for(int l = k; l>=0 ; l--)
						{
							if(term2)
							{
								term2--;
								if(dig[l] != 0)
								c += dig[l]* myPow(10,term2);
								//fprintf(out," !%d %d! ", c, dig[l] );
							}
						}
						int tem1 = term2;
						
						for(int m = len-1; m> k; m--)
						{
							
							if(tem1)
							{
								//fprintf(out," *%d ",tem1);
								tem1--;
								if(dig[m] != 0)
								c += dig[m]* myPow(10,tem1);
							}
						}
					}
					//fprintf(out,"%d %d\n", c, i );
					//count1++;
					if(((c >= A)&&(c <= B)) && (c> i))
						result++;
					c=0;	
				}
				//fprintf(out,"%d",count1);
				//fprintf(out,"!%d %d!\n ", c, i );
				//if((c <= B) && (c> i))
					//result++;
			}
		}
		//fprintf(out,"\n");		
		fprintf(out,"%d\n", result );	 
	}
	//input.close();outfile.close();
	fclose(in);fclose(out);
	
	
	return 0;
}

