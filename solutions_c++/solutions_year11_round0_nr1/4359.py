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
	int T = atoi(buffer);	//초기 몇줄인지 받아옴

	char * s = (char*)malloc (sizeof(char)) ;
	int count=0;
	int data_length=0;
	int result=0;
	data_stream *eachline = (data_stream *)malloc(sizeof(data_stream));
	data_stream *stream = (data_stream*) malloc(sizeof(data_stream));


	while(T-->0)	//줄 수 만큼 반복
	{
		count++;
		fgets(buffer, sizeof(buffer), input);

		data_length = atoi(strtok(buffer," ")); //각 줄의 첫항 즉, 행동 명령 수 받아옴 

		eachline->color= strtok(NULL," ");
		eachline->locate_num= atoi(strtok(NULL," "));
		stream= eachline;								//이로 써 각 행은 eachline이 됨



		while(--data_length>0)
		{
			data_stream *temp = (data_stream*)malloc(sizeof(data_stream));
			temp->color= strtok(NULL," ");
			temp->locate_num=  atoi(strtok(NULL, " "));


			stream->next=temp;
			stream=stream->next;

		}
		stream->next=NULL;

		//data_length는 항의 갯수 eachline이 ( 색+버튼번호 )의 line이 됨.
		//각 행별 OUTPUT 처리
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
	int end_B=0;	//O와 B의 탐색이 종료되었는가 확인

	int cur_O=1;
	int cur_B=1;	//시작 점

	int dist_O=0;	
	int dist_B=0;	//이동해야할 거리

	int loc_O =0;
	int loc_B =0;	//data stream의 위치

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
		//거리측정 후 비교하여 distance가 먼 것 선정

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
		return b-a;	//만일 리턴값이 +이면 더 나아가야 할 것이고 -라면 back 을 수행할 것.
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