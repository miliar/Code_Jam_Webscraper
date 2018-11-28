#include <stdio.h>
#include <stdlib.h>
#include "string.h"
#include <malloc.h>
#define L 10	//���ȡ�û�н����������ַ���
#define D 25
#define N 10

struct WordList
{
	int id;
	char letter[L];
};
struct TestList
{
	char flag;
	struct TestList *next ;
};
struct piList
{
	//�����ĳ����������
	int id;//����һ���ֵ�ƥ��
	struct piList *next;
};
//ȫ�ֱ���
struct WordList List[D];//�ֵ������ݵ��б�

int f_countList(struct piList *p)
{
	int count = 0;
	while(p->next != NULL)
	{
		p = p->next;
		count ++;
	}
	//printf("��%d\n",count);
	return count;
}
struct piList* compare_add(char test,int index,struct piList *p)//������Ĳ�������test���ֵ��б�Ƚ�
{
	//index��0��ʼ 
	//����ƥ����Ŀ
	//������p��ɾ�����в�ƥ����
	
	//printf("\t\t�Ƚ���ĸ%c\n",test);
	//printf("\t\t��������");
	//f_countList(p);
	int count = 0;//����Ϊ����Ϊ1 
	int i;
	struct piList* re;//��������
	re = (piList *)malloc(sizeof(piList));
	re->next = NULL;
	struct piList* s;//������re������ָ��
	s = re;
	while(p != NULL && p->next != NULL)
	{
		i = p->next->id;
		//printf("%d\t\t%c",i,test);
		if(List[i].letter[index] == test)//ͷ�ڵ�û������
		{
			//����һ���ڵ�
			//printf("���\n");
			struct piList *e = (piList *)malloc(sizeof(piList));
			e->id = i;
			e->next = NULL;
			s->next = e;
			s = s->next;
			p = p->next;
		}
		else
		{
			//printf("XXX\n");
			p = p->next;
		}
	}
	/*
	if(re->next == NULL)
		printf("v\n");
	else
		printf("m\n");
	*/
	//f_countList(re);
	//printf("\t\t����������");
	f_countList(re);
	return re;//���ش�ͷ�ڵ������
}

void main()
{
	//��ȡ�ֵ���ø�ʽ����ȡ
	FILE* dictionary;

	FILE* output;
	//��ȡ�������� L D N
	//int L = 0,D = 0,N = 0;
	dictionary = fopen("DDD.in","r");//�ֵ������ļ�
	output = fopen("Out.out","w");
	if(dictionary==0)
	 {
		 printf("error_1");
	 }
	//printf("%d+%d+%d",L,D,N);//��������
	//struct WordList *List;//�ֵ������ݵ��б�

	//��������
	int i = 0;//�ֵ��������� D
	for(i = 0 ;i < D;i ++)
	{
		//ֻ��ȡ�����͵�����
		//List=(struct WordList *)malloc(sizeof(WordList));
		List[i].id = i;
		//fscanf(dictionary,"%s",&List[i].data);
		//printf("%d\n",List[i]);
		//fscanf(dictionary,"%s",&xx);
		fscanf(dictionary,"%s",&List[i].letter);
		//printf("%c",xx[1]);
		//printf("%c\n",List[i].letter[2]);
	}
	//printf("%d",List[2].data[1]);
	fclose(dictionary);
	
	//��ȡ��������
	//��ȡ�ֵ���ø�ʽ����ȡ
	FILE* testdata;

	//��ȡ�������� L D N
	//int L = 0,D = 0,N = 0;
	testdata = fopen("NNN.in","r");//�ֵ������ļ�
	struct TestList *List2[N];//�������ݵ��б�
	int n= 0;//N����������
	for(n = 0;n < N;n++)
	{
		//ֻ��ȡ�����͵�����
		//char temp[];
		struct TestList *s;
		char temp = ' ';
		s = (TestList *)malloc(sizeof(TestList));
		List2[n] = (TestList *)malloc(sizeof(TestList));
		s = List2[n];
		fscanf(testdata,"%c",&temp);
		//printf("%c",temp);
		s->flag = temp;
		s->next = NULL;
		//printf("%c\n",List2[n]->flag);
		while( temp != '#' && temp != '\n')
		{
			struct TestList *p;
			p = (TestList *)malloc(sizeof(TestList));
			fscanf(testdata,"%c",&temp);
			p->flag = temp;
			p->next = NULL;
			//printf("%c",temp);
			//����
			s->next = p;
			s = p;
			//printf("%d",feof(testdata));
			//�����˽�����\n
		}
		//printf("%d\n",n);
	}
	for(n = 0;n < 4;n++)
	{
		//printf("%d\n",n);
		struct TestList *p;
		p = List2[n];
		int x = 0;
		while(p != NULL)
		{
			//printf("%c",p->flag);
			//if(p->flag == '\n')
			//	printf("%d",x);
			x++;
			p = p->next;
		}
		printf("\n");
	}
	fclose(testdata);


	//������ȡ����

	//�����������ʼѭ���Ƚ�
	int pi[N]={1};//ÿ���������ݵ�ƥ����
	for(n = 0;n < N;n++)
	{
		//N����������
		struct TestList *p;
		struct piList *thisTest,*thisTestP;
		int index = 0;
		p = List2[n];
		//��¼����������������Щ�ֵ�ƥ��
		thisTest = (piList *)malloc(sizeof(piList));
		//��ʼ������.����ȫ��ƥ�䡣����ͷ�ڵ�
		thisTestP = thisTest;
		thisTestP->id = -1;
		for(int a = 0;a < D;a++)
		{
			struct piList *s;
			s = (piList *)malloc(sizeof(piList));
			s->id = a;
			s->next = NULL;
			thisTestP->next = s;
			thisTestP = thisTestP->next;
		}
		
		//����ͷ�ڵ�
		thisTestP = thisTest;
		printf("��%d����������\n",n+1);
		//
		while(p != NULL && p->flag != '\n' && p->flag != '#')
		{
			//�����ĳ����(��ĸ+����)��ѭ��
			printf("dd");
			int ifnone = 0;//ĳ����ĸ��ƥ����Ŀ 
			//�����������ݿ������
			//���ݿ������Ŷ�αȽ���ĸ����������
			//�˳����ݿ�󽫴˴����ɵ��������������һ�����ݿ�ıȽ�
			struct piList *thisArea;
			thisArea = (piList *)malloc(sizeof(piList));
			thisArea->next = NULL;
			printf("\t�Ƚϵ�%d���ݿ�\n",index);
			if(p->flag == '(')
			{
				//��ѭ���Ƚ�
				//printf("\t\t\t---------------------\n");
				p = p->next;
				//
				 while(p->flag != ')')
				 {
					//�����ĳ����ĸ
					
					//ifnone = compare(p->flag,index,thisTestP);//�����Ƿ�Ϊ��
					 //û���ͷ�thisTestP���ڴ档
					 //
					struct piList* s = compare_add(p->flag,index,thisTestP);//���ش�ͷ�ڵ������
					//printf("\t\t����������");
					//f_countList(s);
					//���ӵ�������ݿ��ר������
					struct piList* temp = thisArea;
					while(temp->next != NULL)//�ҵ���ǰ����Ľ�β
						temp = temp->next;
					//�������ɵ�����ӵ�֮ǰ��������
					//if(s->next == NULL)
					//	printf("v");
					temp->next = s->next;//���ص�������ͷ�ڵ�
					
					p = p->next; //��һ��ĸ�ڴ����ݿ���
					//�����ڴ����ݿ��в�����һ����ĸ
				 }

				p = p->next;//����')'
				//printf("\t\t\t===========================\n");
			}
			else//�������������ֱ�ӱȽ�
			{
				//ifnone = compare(p->flag,index,thisTestP);//�����Ƿ�Ϊ��
					 //û���ͷ�thisTestP���ڴ档
					 //
				struct piList* s = compare_add(p->flag,index,thisTestP);//���ش�ͷ�ڵ������
				//printf("\t\t����������2");
				//f_countList(s);
				thisArea = s;

				p = p->next;//��һ����ĸ/���ݿ�
			}
			//������һ�����ݿ�
			//û���ͷ��ڴ�
			thisTestP = thisArea;
			if(thisArea->next == NULL)//���û��ƥ��
				break;
			//printf("\t���������ݿ�\n");
			index++;
		}
		//�˲���ƥ�������������
		pi[n] = f_countList(thisTestP);
		//�ͷ��ڴ�
		printf("Case #%d: %d\n",n+1,pi[n]);
		fprintf(output,"Case #%d: %d\n",n+1,pi[n]);
	}


	fclose(output);
	//List2[0].flag = 's';
	//printf("%c\n",List2[0].flag );
		getchar();
}