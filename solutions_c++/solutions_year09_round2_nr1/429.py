#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// #define  INPUT_FILE_NAME "A-small-attempt1.in"
// #define OUTPUT_FILE_NAME "A-small-attempt1.out"

#define  INPUT_FILE_NAME "A-large.in"
#define OUTPUT_FILE_NAME "A-large.out"

struct node
{
	float value;
	char ani[20];
	struct node* n1;
	struct node* n2;
};

int line;

struct node* getnode(FILE* fp)
{
	struct node* node;
	char temp;
	int count;
	node = new struct node;
	fscanf(fp, "%f",&(node->value));
	while(1)
	{
		temp = fgetc(fp);
		if (temp == ')')
		{
			node->n1 = NULL;
			node->n2 = NULL;
			return node;
		}
		else if (temp >= 'a' && temp <= 'z')
		{
			count = 0;
			while(1)
			{
				node->ani[count++] = temp;
				temp = fgetc(fp);
				if (temp < 'a' || temp > 'z')
				{
					node->ani[count++] = '\0';
					break;
				}
			}
			break;
		}
	}
	
	while(fgetc(fp) != '(');
	node->n1 = getnode(fp);
	while(fgetc(fp) != '(');
	node->n2 = getnode(fp);
	while(fgetc(fp) != ')');
	return node;
}

int main()
{
	int i,j,k,l;
	int ii,jj,kk,ll;
	FILE* fp1;
	FILE* fp2;
	int test_num;
	int len;
	float ret;
	
	char data[10000] = {0,};
	char temp[100];
	char tt[100][100];
	int t[10];
	int s[100];

	struct node* root;
	struct node* node;

	// read data
	fp1 = fopen(INPUT_FILE_NAME,"r");
	fp2 = fopen(OUTPUT_FILE_NAME,"w+");
	if (fp1 == NULL || fp2 == NULL) 
	{
		printf("file open error\n");
		return -1;
	}

	fscanf(fp1,"%d",&test_num);
	

	for (i=0;i<test_num;i++)
	{
		memset(data,0,10000);
		fscanf(fp1,"%d",&ii);

		while(fgetc(fp1) != '(');

		root = getnode(fp1);

		fprintf(fp2,"Case #%d:\n",i+1);
		fscanf(fp1,"%d",&line);

		jj = 0;

		while(jj < line)
		{
			
			fscanf(fp1,"%s",temp);
			
			
			fscanf(fp1,"%d",&ii);
		
			for(k=0; k<ii;k++)
			{
				fscanf(fp1,"%s",tt[k]);
			}

			ret = 1;
			node = root;
			while(node != NULL)
			{
				ret = ret * node->value;
				for(k=0; k<ii;k++)
				{
					if (strcmp(tt[k],node->ani) == 0) break;
				}
				if (k == ii) node = node->n2;
				else node = node->n1;
			}
			fprintf(fp2,"%0.7f\n",ret);
			jj++;
		}



	}

	fclose(fp1);
	fclose(fp2);

	return 0;
}