#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX 30	//10�� 6�¿� �ش��ϴ� 2�� �ڸ���


void itob(int v, int* bin);


void main()
{

	FILE *input;
	fopen_s(&input,"small.in","r");
	FILE *output;
	fopen_s(&output,"output.txt","w");

	char buffer[10000];
	fgets(buffer, sizeof(buffer), input);
	int T = atoi(buffer);							//test case 
	int *value;
	int *check_digit;
	int **binary;
	int candy=0;
	int i=0, j=0;
	int min;
	int max=0;
	int impossible=0;
	int count=0, result=0;
	char* s=(char*)malloc (sizeof(char));

	while(T-->0)
	{

		count++;
		fgets(buffer, sizeof(buffer), input);
		candy = atoi(strtok(buffer," "));			//ĵ���
		value = (int*)malloc(candy*sizeof(int));
		binary = (int**)malloc(candy*sizeof(int));
		check_digit = (int*)malloc(MAX*sizeof(int));
		*binary =(int*)malloc(MAX*sizeof(int));
		s=(char*)malloc (sizeof(char));

		fgets(buffer, sizeof(buffer), input);
		*value= atoi(strtok(buffer," "));

		max = *value;
		min = *value;
		
		for(i=0;i<MAX;i++)
		{
			*(*binary+i)=0;
			*(check_digit+i)=0;
		}
		itob(*(value), *(binary));
		
		for(i=1;i<candy;i++)
		{
			*(binary+i)=(int*)malloc(MAX*sizeof(int));		//���̳ʸ� ���������� �Ҵ�
			*(value+i)= atoi(strtok(NULL," "));
			for(j=1;j<MAX;j++)
			{
				*(*(binary+i)+j)=0;
			}

			if(min>*(value+i))
				min=*(value+i);	//�������� �� �ּ��� ĵ�� ���
			max += *(value+i);	//��ü ĵ���� value

			itob(*(value+i), *(binary+i));
		}

		impossible=0;
		
		for(j=0;j<MAX;j++)
		{
			for(i=0;i<candy;i++)
			{
				if(*(*(binary+i)+j)==1)
				{
					if(*(check_digit+j)==1)
						*(check_digit+j)=0;		//j�ڸ��� �ش��ϴ� 1�� ���� ¦��������
					else if(*(check_digit+j)==0)
						*(check_digit+j)=1;		//Ȧ��������
				}
			}
			if(*(check_digit+j)==1)
			{
				impossible=1;
				break;
			}
		}


		//�� �ະ OUTPUT ó��
		fputs("Case #",output);
		_itoa(count,s,10);
		fputs(s,output);
		fputs(": ",output);

		
		if(impossible==1)
			fputs("NO",output);
		else
		{
			result=max-min;
			s=(char*)malloc(sizeof(char));
			_itoa(result,s,10);
			fputs(s, output);
		}
		fputs("\n",output);
		free(value);
	}

}

void itob(int v, int* bin)
{

	int i=0;
	while(1)
	{
		if(v==0)
			break;
		*(bin+i) = v%2 ;
		i++;
		v=v/2;
	}

}