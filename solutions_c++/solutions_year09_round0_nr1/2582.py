#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int ret_match(char*,char*);
int main()
{
	FILE *fp;
	int L,D,N;
	char entry_line[20];
	char input_line[275];	
	char *ch;

	char *word_list[5005];
	char *possible_word[550];

	int len;
	int cnt[550];


	fp=fopen("cur2.in","r");

	if(fp!=NULL)
		fgets(entry_line,20,fp);
	sscanf(entry_line,"%d %d %d",&L,&D,&N);
	//printf("L = %d, D = %d, N = %d\n",L,D,N);//3 5 4
	
	for(int i=0;i<D;i++)
	{
		fgets(entry_line,20,fp);
		
		len = strlen(entry_line);			
		entry_line[len-1] = '\0';
		len = strlen(entry_line);			
		//printf("str = %s len = %d",entry_line,len);
		ch = (char*)malloc(20*sizeof(char));
		strcpy(ch,entry_line);
		//printf("%s\n",ch);	
		word_list[i] = ch;
		//printf(":%s: %d\n",word_list[i],strlen(word_list[i]));
		
					
	}
	
	for(int i=0;i<N;i++)
	{
		fgets(input_line,275,fp);
		
		len = strlen(input_line);			
		input_line[len-1] = '\0';
		len = strlen(input_line);			
		//printf("str = %s len = %d",input_line,len);
		ch = (char*)malloc(275*sizeof(char));
		strcpy(ch,input_line);
		//printf("%s\n",ch);	
		possible_word[i] = ch;
		//printf(":%s: %d\n",possible_word[i],strlen(possible_word[i]));
	}	

	// now we have word_list[i] has the i-th word from dictionary
	// and possible_word[j] has the j-th input possible word with (,)

	//N =1;

	for(int i=0;i<N;i++)// for each input possible word
	{
		
		for(int j=0;j<D;j++)// search for each word in the dictionary
		{
			if(ret_match(possible_word[i],word_list[j])==1)
				cnt[i] += 1;

		}
		
	}


	for(int i=0;i<N;i++)
		printf("Case #%d: %d\n",(i+1),cnt[i]);
	
					
	return 0;
}

int ret_match(char* s1,char *s2)
{
	char regEx[275];char str[20];
	char ch;
	strcpy(regEx,s1);strcpy(str,s2);	
	int L=strlen(regEx);int M=strlen(str);
	int flag=0;
	int k =0;

	//printf("%s: %s\n",regEx,str);
	for(int i=0;i<M;i++)// each dictionary word
	{
		ch = str[i];
		//printf("1# %c\n",ch);
		for(int j=k;j<L;j++) // each reg expr
		{
			if(regEx[j]=='(')
			{
				k = j;
				
				//printf("2# %c\n",regEx[k]);
				
				flag = 0;		
				while(regEx[k++] != ')')
				{
					//printf("3# %c\n",regEx[k]);
					if(regEx[k] == ch)
					{
						flag=1;	
						//break;	
				}	}
				if(flag==1)
					break;
				else
					return 0;

			}
			else
			{
				if(regEx[j]==ch)
			 	{
					//printf("4# %c %c\n",regEx[j],ch);	
					k = j+1;
					break;
				}	
				else
					return 0;	

			}



		}
	}




	//printf("%c %c\n",regEx[0],str[0]);

	return 1;
}
