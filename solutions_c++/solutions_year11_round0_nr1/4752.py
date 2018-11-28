#include "stdio.h"
#include "string.h"
char read_next_character();
int main()
{
	long int T,N,num_of_buttons,num_of_sec,posO,posB,count=0,countn=0;
	int i,j,k,l;
	int o[100];
	int b[100]; 
	char ch;
	static char seq[100];
	scanf("%d\n",&T);
	while(count<T)
	{	i=0,j=0,k=0;
		num_of_buttons=0;
		num_of_sec=0;
		posO=1;
		l=0;
		posB=1;
		i=0;
		countn=0;
		memset(o,0,100*sizeof(int));
		memset(b,0,100*sizeof(int));
		memset(seq,0,100);
		scanf("%d\n",&num_of_buttons);
		
 		while(countn<num_of_buttons)
		{
		 		  ch= read_next_character();
				  if(ch=='O')
				  {		
						scanf("%d",&o[i]);
						seq[k]='O';
				   		k++;
                  		i++;
				  }	
				  else if(ch=='B')
				  {
						scanf("%d",&b[j]);				
	                    seq[k]='B';
				   		k++;
                  		j++;						
	              }		
			countn++;
		} 
		k=0;
		j=0;
		i=0;
		while(num_of_buttons)
		{
			  num_of_sec++;
			  if(seq[k]=='O')
			  {
			  	if(posO>o[i])
			  	{
			  		posO--;
				}
			  	else if(posO<o[i])
			  	{
				  posO++;
				}
				else
				{
				  k++;
				  i++;
				  num_of_buttons--;
				}
				if(posB>b[j])
			  	{
			  		posB--;
				}
			  	else if(posB<b[j])
			  	{
				  posB++;
				}
			  }
			  else
			  {
			
				if(posB>b[j])
			  	{
			  		posB--;
				}
			  	else if(posB<b[j])
			  	{
				  posB++;
				}	
				else
				{
				  k++;
				  j++;
				  num_of_buttons--;
				}			
				if(posO>o[i])
			  	{
			  		posO--;
				}
			  	else if(posO<o[i])
			  	{
				  posO++;
				}
					
			  }
			  							   
		
		}
		printf("Case #%d: %d\n",count+1,num_of_sec);
		count++;         
	}
	return 0;
}


char read_next_character()
{
	char ch;
	do
	{
		scanf("%c",&ch);
	}while(ch==' '||ch=='\n'||ch=='\t');
	return ch;
}