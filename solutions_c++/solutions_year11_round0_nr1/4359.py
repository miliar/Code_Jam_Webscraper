#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct data_stream
{
	int locate_num;
	char *color;
	struct data_stream* next;
}data_stream;

data_stream* find_next(char c, data_stream *s, int* loc, int* dist, int * cur);
int BotTrust(int n, data_stream *d);
int compare(int a, int b);

void main()
{

	FILE *input;
	fopen_s(&input,"A-large.in","r");
	FILE *output;
	fopen_s(&output,"output.txt","w");

	char buffer[10000];
	fgets(buffer, sizeof(buffer), input);
	int T = atoi(buffer);	//�ʱ� �������� �޾ƿ�

	char * s = (char*)malloc (sizeof(char)) ;
	int count=0;
	int data_length=0;
	int result=0;
	data_stream *eachline = (data_stream *)malloc(sizeof(data_stream));
	data_stream *stream = (data_stream*) malloc(sizeof(data_stream));


	while(T-->0)	//�� �� ��ŭ �ݺ�
	{
		count++;
		fgets(buffer, sizeof(buffer), input);

		data_length = atoi(strtok(buffer," ")); //�� ���� ù�� ��, �ൿ ��� �� �޾ƿ� 

		eachline->color= strtok(NULL," ");
		eachline->locate_num= atoi(strtok(NULL," "));
		stream= eachline;								//�̷� �� �� ���� eachline�� ��



		while(--data_length>0)
		{
			data_stream *temp = (data_stream*)malloc(sizeof(data_stream));
			temp->color= strtok(NULL," ");
			temp->locate_num=  atoi(strtok(NULL, " "));


			stream->next=temp;
			stream=stream->next;

		}
		stream->next=NULL;

		//data_length�� ���� ���� eachline�� ( ��+��ư��ȣ )�� line�� ��.
		//�� �ະ OUTPUT ó��
		fputs("Case #",output);
		_itoa(count,s,10);
		fputs(s,output);
		fputs(": ",output);

		result=BotTrust(data_length, eachline);

		_itoa(result,s,10);
		fputs(s,output);
		fputs("\n",output);
	}

}

int BotTrust(int n, data_stream *d)
{

	int end_O=0;
	int end_B=0;	//O�� B�� Ž���� ����Ǿ��°� Ȯ��

	int cur_O=1;
	int cur_B=1;	//���� ��

	int dist_O=0;	
	int dist_B=0;	//�̵��ؾ��� �Ÿ�

	int loc_O =0;
	int loc_B =0;	//data stream�� ��ġ

	int time=0;

	data_stream *O = (data_stream*) malloc(sizeof(data_stream));
	data_stream *B = (data_stream*) malloc(sizeof(data_stream));
	O=d;
	B=d;

	if((O=	find_next('O', O, &loc_O,&dist_O, &cur_O))==NULL)
		end_O=1;
	if((B=	find_next('B',B, &loc_B, &dist_B, &cur_B))==NULL)
		end_B=1;
	while(!(end_O==1 &&end_B==1))
	{
		//�Ÿ����� �� ���Ͽ� distance�� �� �� ����

		if(loc_O<loc_B && end_O !=1)
		{
			if(dist_O<dist_B)
			{
				dist_B -= dist_O +1;
			}
			else
				dist_B=0;
			time += dist_O +1;
			if((O=find_next('O', O->next, &loc_O,&dist_O, &cur_O))==NULL)
				end_O=1;
		}
		else if(end_B !=1)
		{
			if(dist_B<dist_O)
				dist_O -=dist_B+1;
			else 
				dist_O=0;
			time += dist_B+1;
			if((B=find_next('B',B->next, &loc_B, &dist_B, &cur_B))==NULL)
				end_B=1;

		}
	
	}
	return time;

}
int compare(int a, int b)
{
	if(b-a>0)
		return b-a;	//���� ���ϰ��� +�̸� �� ���ư��� �� ���̰� -��� back �� ������ ��.
	else
		return a-b;
}

data_stream* find_next(char c, data_stream *s, int *loc, int* dist, int * cur)
{
	
	if(s==NULL)
	{
		*dist=0;
		return NULL;
	}
	(*loc)++;
	while(1)
	{
		if(s==NULL)
		{
			*dist=0;
			return NULL;
		}
		if(*s->color==c)
			break;
		else
		{
			s=s->next;
			(*loc)++;
		}
		
	}
	*dist=compare(*cur, s->locate_num);
	*cur=s->locate_num;

	return s;

}