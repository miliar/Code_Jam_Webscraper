// googlecodejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <string.h>

void main()
{
	int cont_input, cont_line;
	int cont_time = 0;
	int before_time=0;
	int comp,dist;
	int i, j =0;
	char chk_first = 'Y';
	int before_val_B = 1;
	int before_val_O = 1;
	char before_val_type;
	int total_val = 0;
	
	char *input_data;
	FILE *f;
	FILE *fw;

	char buf[1024]={0};
	char *str;
	f= fopen("A-large.in","r");
	fw= fopen("answer.txt","w");
	if(f==NULL)
	{
		printf("error");
		exit(1);
	}
	cont_input = atoi(fgets(buf,256,f));
	
	for(i=0; i<cont_input; i++)
	{
		memset(buf,0,sizeof(buf));
		fgets(buf,1024,f);
		str = strtok(buf, " ");
		cont_line = atoi(str);
		
		for(j=0; j<cont_line; j++)
		{
			str = strtok(NULL, " ");
			if(str) 
			{
				
				if(*str == 'B')
				{
					if(chk_first == 'Y')
					{
						str = strtok(NULL, " ");
						chk_first = 'N';
						before_val_B = atoi(str);
						before_time = atoi(str);
						total_val = atoi(str);
					
						
					}
					else
					{
						str = strtok(NULL, " ");
						if(before_val_type == 'B')
						{
							total_val = total_val + abs(before_val_B - atoi(str)) +1;
							before_time = before_time + abs(before_val_B - atoi(str)) +1;
							
						
							before_val_B = atoi(str);
						}
						else if(before_val_type == 'O')
						{
							comp = atoi(str);
							dist = abs(before_val_B - comp);
							if((before_time - dist) >=0)
							{
								total_val = total_val + 1;
								before_time =1;
							}
							else
							{
							
								total_val = total_val + (dist - before_time) + 1;
							
								before_time =  (dist - before_time) + 1;
							}
							before_val_B = atoi(str);
							
						}
						
					}
					before_val_type ='B';
					
				}
				else if(*str == 'O')
				{
				
					if(chk_first == 'Y')
					{
						str = strtok(NULL, " ");
						chk_first = 'N';
						before_val_O = atoi(str);
						before_time = atoi(str);
						total_val = atoi(str);
						
					}
					else
					{
						str = strtok(NULL, " ");
						if(before_val_type == 'O')
						{
							total_val = total_val + abs(before_val_O - atoi(str)) +1;
							before_time =before_time + abs(before_val_O - atoi(str)) +1;
							
							before_val_O = atoi(str);
						}
						else if(before_val_type == 'B')
						{
							comp = atoi(str);
							dist = abs(before_val_O - comp);

							if((before_time - dist) >=0)
							{
								total_val = total_val + 1;
								before_time = 1;
							}
							else
							{
								total_val = total_val + (dist - before_time) + 1;
								before_time =  (dist - before_time) + 1;
							}
							before_val_O = atoi(str);
							
						}
						
					}
					before_val_type ='O';
				}
				
			}
			
		}
		fprintf(fw, "Case #%d: %d\n", i + 1, total_val);
		total_val = 0;
		before_val_O = 1;
		before_val_B = 1;
		before_time=0;
		chk_first = 'Y';
	}
	
	fclose(f);

}

