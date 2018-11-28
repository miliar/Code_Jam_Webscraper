#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_NUM_ORDER	20000
#define MAX_LINE_LENGTH	(2+5*MAX_NUM_ORDER)

typedef struct{
	int num;
	int boton[MAX_NUM_ORDER];
	char robot[MAX_NUM_ORDER];
}ordenes;

typedef struct{
	char color;
	int actual_order;
	int touch_time;
}robot;

void get_input(FILE* fid, ordenes &orders);
void get_next_order(robot &rob, const ordenes orders);
void initialize_robot(robot &rob,const char color);
char *min(char *numa, char *numb);
int ind_min(int numa,int numb);
int max(int numa,int numb);
void print_output(FILE* fid, int result);

main()
{
	FILE *fid_input;
	FILE *fid_output;
	ordenes orders;
	robot rob[2];
	int time=0;
	char first_line[MAX_LINE_LENGTH];
	int i;
	int num_cases;
	int waited;

	fid_input=fopen("info.txt","r");
	fid_output=fopen("res.txt","a+");

	fgets(first_line,MAX_LINE_LENGTH,fid_input);

	sscanf(first_line,"%d",&num_cases);

	for(i=0;i<num_cases;i++)
	{
		time=0;
		initialize_robot(rob[0],'O');
		initialize_robot(rob[1],'B');
	
		get_input(fid_input,orders);
	
		get_next_order(rob[0], orders);
		get_next_order(rob[1], orders);

		do
		{
			waited=ind_min(rob[0].actual_order,rob[1].actual_order);
			time=max(rob[waited].touch_time,time+1);
			rob[waited].touch_time=time;

			//printf("Robot %c cumple orden Nº%d, tocar boton %d\n",rob[waited].color,rob[waited].actual_order,orders.boton[rob[waited].actual_order],rob[waited].touch_time);
			//printf("Tiempo parcial: %d Robot: %c\n",time,rob[waited].color);

			get_next_order(rob[waited],orders);
		}while(rob[0].actual_order!=MAX_NUM_ORDER || rob[1].actual_order!=MAX_NUM_ORDER);
		//printf("Tiempo total: %d\n",time);			
		print_output(fid_output,time);
	}
		
	fclose(fid_output);
	fclose(fid_input);
}

void get_next_order(robot &rob, const ordenes orders)
{
	int i;
	for(i=(rob.actual_order+1);i<orders.num;i++)
	{
		if(orders.robot[i]==rob.color)
		{
			if(rob.actual_order==-1)
				rob.touch_time=orders.boton[i];
			else
				rob.touch_time+=(abs(orders.boton[i]-orders.boton[rob.actual_order])+1);
			rob.actual_order=i;
			//printf("Robot %c fetches orden Nº%d, tocar boton %d, se libera en %d\n",rob.color,rob.actual_order,orders.boton[rob.actual_order],rob.touch_time);
			return;
		}
	}
	rob.actual_order=MAX_NUM_ORDER;
}

void initialize_robot(robot &rob,const char color)
{
	rob.color=color;
	rob.actual_order=-1;
	rob.touch_time=0;
}

void get_input(FILE* fid, ordenes &orders)
{	
	char line[MAX_LINE_LENGTH];
	int line_length;

	char *read_o=line;
	char *read_b=line;
	
	char robot;
	int boton;
	
	fgets(line,MAX_LINE_LENGTH,fid);

	sscanf(line,"%d ", &line_length);

	read_o=strstr(read_o,"O");
	read_b=strstr(read_b,"B");

	orders.num=0;
	while(read_o!=NULL || read_b!=NULL)
	{
		sscanf(min(read_o,read_b),"%c %d",&robot,&boton);
		
		orders.robot[orders.num]=robot;
		orders.boton[orders.num++]=boton;

		if(robot=='O' && read_o!=NULL)
		{
			read_o++;
			read_o=strstr(read_o,"O");		
		}	
		else if(robot=='B' && read_b!=NULL)
		{		
			read_b++;	
			read_b=strstr(read_b,"B");		
		}
	}
}

void print_output(FILE* fid, int result)
{
	static int n=1;
	fprintf(fid,"Case #%d: %d\n",n++,result);
}

char *min(char *numa, char *numb)
{
	if((numa!=NULL && numa<numb) || numb==NULL)
		return numa;
	else
		return numb;
}


int ind_min(int numa,int numb)
{
	if(numa<numb)
		return 0;
	else
		return 1;
}

int max(int numa,int numb)
{
	if(numa<numb)
		return numb;
	else
		return numa;
}
