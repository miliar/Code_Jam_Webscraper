#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
struct button
{
	char b;
	int p;

};
int main()
{
	int t,total;//testcases
	int n;//no of buttons
	int o,b;//positions of orange and blue robot
	int k,timer,j,i;


	FILE * fp,*fp1;
	fp=fopen("A-large.in","r");
	fp1=fopen("OUTPUT A-large.txt","w");
	fscanf(fp,"%d",&t);
	
	total=t;
	while(t--)
	{
		char c;
		k=j=timer=0;
		o=b=1;
		fscanf(fp,"%d",&n);
		int *br =new int[n+1];
		int *or =new int[n+1];
		for(i=0;i<n+1;i++)
		{
			br[i]=0;
			or[j]=0;
		}
		struct button * a=new struct button[n];
		cout<<n<<endl;

		for(i=0;i<n;i++)
		{
			fscanf(fp,"%c",&c);
			fscanf(fp,"%c",&a[i].b);
			
			fscanf(fp,"%d",&a[i].p);
			if(a[i].b=='O')
			{
				or[k++]=a[i].p;
			}

			else
			{
				br[j++]=a[i].p;
			}

		}

	
	for(i=0;i<n;i++)
	{
		cout<<a[i].b<<a[i].p<<endl;
	
	}

		
			
		i=k=j=0;
		while(i<n)
		{
			if(a[i].b=='O')
			{
				
				if(b!=br[k])
					{
						
							if(abs(a[i].p-o)+1>=abs(br[k]-b))
								b=br[k];
							else
								if(b>br[k])

								b=b-(abs(a[i].p-o)+1);
								else
								b=b+abs(a[i].p-o)+1;


					

					}
				
				
				if(a[i].p!=o)
				{
					
						timer+=abs(a[i].p-o)+1;
					
						
					o=a[i].p;
					j++;
				}
				else
				{
				timer++;
				j++;
					
				}

					

					

					}//if


			if(a[i].b=='B')
			{
				if(o!=or[j])
					{
						
							if(abs(a[i].p-b)+1>=abs(or[j]-o))
								o=or[j];
							else
							
								if(o>or[j])
								o=o-(abs(a[i].p-b)+1);
								else
									o=o+abs(a[i].p-b)+1;


					}
				
				
				if(a[i].p!=b)
				{
					
						timer+=abs(a[i].p-b)+1;
					
					
						
					b=a[i].p;
					k++;
				}
				else
				{
					timer++;
					k++;
				/*	if(o!=or[j])
						if(o<or[j])
							o++;
						else
							o--;*/

					
				}

					

					

					}//if

				
			

		








			i++;

		}

			
		fprintf(fp1,"Case  #%d: %d\n",total-t,timer);
		


	}//while


		fclose(fp);
		fclose(fp1);

return 0;
	

	
}