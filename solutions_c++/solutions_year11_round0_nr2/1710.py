#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH	5000
#define MAX_LETRAS	50

typedef struct{
	char hnas[MAX_LETRAS];
	int num_hnas;
	char fusion[MAX_LETRAS];
	char destr[MAX_LETRAS];
	int num_destr;
}letter;

void initialize_letters(letter *letra);
void get_input(FILE* fid, letter *letra, char *in);
void imprimir_letras(letter *letra);
int destruc(char *prev_word, char new_elem, letter *letras);
int is_inside(const char element, const char *list, const int size_list);
void print_output(FILE* fid, char* result);
int max(int numa,int numb);
void kill_str(char *str);

main()
{
	char first_line[MAX_LINE_LENGTH];
	int num_cases;
	int ptr;
	char str_out[MAX_LINE_LENGTH];
	int i,j;
	int index;
	char letra_anterior;
	char letra_invocada;
	letter letras[MAX_LETRAS];
	char invokes[MAX_LINE_LENGTH];
	FILE *fid_input;
	FILE *fid_output;

	fid_input=fopen("info.txt","r");
	fid_output=fopen("res.txt","a");

	fgets(first_line,MAX_LINE_LENGTH,fid_input);

	sscanf(first_line,"%d",&num_cases);

	for(i=0;i<num_cases;i++)
	{
		initialize_letters(letras);
		get_input(fid_input,letras,invokes);
		printf("\n\n\n\nCaso %d:",i+1);
		imprimir_letras(letras);
		//printf("Invokes: %s\n",invokes);
		str_out[0]=invokes[0];
		ptr=1;
		for(j=1;j<strlen(invokes);j++)
		{
			if(ptr!=0)
				letra_anterior=str_out[ptr-1];

			letra_invocada=invokes[j]-'A';
			if(ptr!=0 && (index=is_inside(letra_anterior,letras[letra_invocada].hnas,letras[letra_invocada].num_hnas))!=-1)
			{
				str_out[ptr-1]=letras[letra_invocada].fusion[index];
				printf("Fusion\n");
			}
			else if(ptr!=0 && destruc(str_out,letra_invocada+'A',letras))
			{
				printf("Destruccion\n");
				ptr=0;
			}
			else
			{
				printf("Adicion\n");
				str_out[ptr++]=invokes[j];
			}

			printf("%s\n",str_out);
		}
		str_out[ptr]='\0';
		print_output(fid_output, str_out);
		printf("%s\n",str_out);
		kill_str(str_out);
	}
		
	fclose(fid_output);
	fclose(fid_input);
}

int destruc(char *prev_word, char new_elem, letter *letras)
{
	int i,j;
	int lon=strlen(prev_word);
	for(i=0;i<lon;i++)
	{
		if(is_inside(new_elem,letras[prev_word[i]-'A'].destr,letras[prev_word[i]-'A'].num_destr)!=-1)
		{
			for(j=0;j<lon;j++)
				prev_word[j]='\0';
			return 1;
		}
	}
	return 0;
}

void kill_str(char *str)
{
	int i;
	int lon;
	lon=strlen(str);

	for(i=0;i<lon;i++)
		str[i]='\0';
}

int is_inside(const char element, const char *list, const int size_list)
{
	int i;
	for(i=0;i<size_list;i++)
	{
		if(list[i]==element)
			return i;
	}
	return -1;
}

void initialize_letters(letter *letra)
{
	int i;
	for(i=0;i<MAX_LETRAS;i++)
	{
		letra[i].num_hnas=0;
		letra[i].num_destr=0;
	}
}

void imprimir_letras(letter *letra)
{
	int i,j;
	for(i=0;i<MAX_LETRAS;i++)
	{
		if(letra[i].num_hnas>0 || letra[i].num_destr>0)
		{
			printf("\n\nLETRA %c\n",'A'+i);
			if(letra[i].num_hnas>0)
			{
				printf("Letras hermanas:\n");
				for(j=0;j<letra[i].num_hnas;j++)
				{
					printf("%c, ",letra[i].hnas[j]);
				}

				printf("\nLetras fusion:\n");
				for(j=0;j<letra[i].num_hnas;j++)
				{
					printf("%c, ",letra[i].fusion[j]);
				}
			}
			if(letra[i].num_destr>0)
			{			
				printf("\nLetras destruccion:\n");
				for(j=0;j<letra[i].num_destr;j++)
				{
					printf("%c, ",letra[i].destr[j]);
				}
			}
		}
	}
	printf("\n\n");
}

void get_input(FILE* fid, letter *letra, char *in)
{	
	char line[MAX_LINE_LENGTH];
	char text;
	char *ptr;
	int i;
	int num;

	fgets(line,MAX_LINE_LENGTH,fid);
	sscanf(line,"%d",&num);

	ptr=line;
	for(i=0;i<num;i++)
	{
		ptr=strstr(ptr," ")+1;
		letra[ptr[0]-'A'].fusion[letra[ptr[0]-'A'].num_hnas]=ptr[2];
		letra[ptr[0]-'A'].hnas[letra[ptr[0]-'A'].num_hnas++]=ptr[1];

		letra[ptr[1]-'A'].fusion[letra[ptr[1]-'A'].num_hnas]=ptr[2];
		letra[ptr[1]-'A'].hnas[letra[ptr[1]-'A'].num_hnas++]=ptr[0];
	}

	ptr=strstr(ptr," ")+1;
	sscanf(ptr,"%d",&num);

	for(i=0;i<num;i++)
	{
		ptr=strstr(ptr," ")+1;
		letra[ptr[0]-'A'].destr[letra[ptr[0]-'A'].num_destr++]=ptr[1];
		letra[ptr[1]-'A'].destr[letra[ptr[1]-'A'].num_destr++]=ptr[0];
	}
	ptr=strstr(ptr," ")+1;
	ptr=strstr(ptr," ")+1;
	strcpy(in,ptr);
}

void print_output(FILE* fid, char* result)
{
	static int n=1;
	int i;
	int ptr=0;
	char real_result[MAX_LINE_LENGTH];

	for(i=0;i<max(3*strlen(result)-5,0);i++)
	{
		if((i%3)==0)
			real_result[i]=result[i/3];
		else if((i%3)==1)
			real_result[i]=',';
		else
			real_result[i]=' ';
	}
	real_result[i]='\0';
	
	fprintf(fid,"Case #%d: [%s]\n",n++,real_result);
}

int max(int numa,int numb)
{
	if(numa<numb)
		return numb;
	else
		return numa;
}
