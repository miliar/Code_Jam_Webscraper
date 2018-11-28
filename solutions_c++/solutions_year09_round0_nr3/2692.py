#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

#define N 100

struct TestList//˫������
{
	char flag;
	int id;
	struct TestList *next ;
	struct TestList *pre ;
};

//ȫ�ֱ���
struct TestList* f_getCharP(struct TestList* p,char x,int index)
{
	//���ص�index��x��ָ��.index ��0��ʼ
	int count = 0;
	while( p != NULL)
	{
		if(p->flag == x)
			count ++;
		if(count == index+1)
			break;
		p = p->next;
	}
	//����Ĳ�����֤�ܹ��ҵ�
	return p;
}
int f_CharAfterNum(struct TestList *p,char x)//��p��ʼ������Ƿ����x�ַ������ش��ڸ���
{
	//x����Ҫ���ҵ��ַ�
	int count = 0;
	//char a = p->flag;
	//int b = p->id;
	
	while(p != NULL)
	{
		if(p->flag == x)
			count ++;
		p = p->next;
	}

	return count;

}
int countN = 0;
int f_searchChar(int i,struct TestList *thisP,char a[])//i���ַ����
{
	//������ĸָ�빹�ɵ�����
	/*
	�����ĳһ���ַ����ж��ֿ��ܵ�λ�á�
	��������е�һ��λ�ã�������һ���ַ�����welcome����һ���ַ��������ǲ��������е�
	
	*/
	//�õ�����ַ��Ŀ���λ����t
	int t = f_CharAfterNum(thisP,a[i]);
	//�������һ��λ�õݹ�
	for(int g = 0;g < t;g++)
	{
		//�õ����λ�õ�ָ��
		struct TestList *thisNew = f_getCharP(thisP,a[i],g);//����thisPָ���i��a[i]��ָ���ַ
		//������λ�ò������һ���ַ�����ݹ�
		if(i == 18)
		{
			//printf("%c",a[preI]);
			//printf("%d",f_CharAfterNum(thisS,a[preI]));	
			countN ++;
		}
		else
		{
			//�ݹ�ʱ���õ�ǰλ���滻��ʼλ�ã������ַ�Ϊ��һ���������
			f_searchChar(i+1,thisNew,a);
		}
	}
	//printf("%d ",count);
	return countN;
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

	struct TestList *List2[N];//�������ݵ��б�
	int OutPutData[N];
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
		//printf("%c",temp);
		s->flag = '-';
		s->id = -1;
		s->next = NULL;//����ͷ�ڵ�
		s->pre = NULL;
		//printf("%c\n",List2[n]->flag);
		int id = 0;
		while( temp != '#' && temp != '\n')
		{
			struct TestList *p;
			p = (TestList *)malloc(sizeof(TestList));
			fscanf(dictionary,"%c",&temp);
			p->flag = temp;
			p->id = id;
			id++;
			p->next = NULL;
			p->pre = s;
			//printf("%c",temp);
			//����
			s->next = p;
			s = p;
			//printf("%d",feof(dictionary));
			//�����˽�����\n
		}
		//printf("%d\n",n);
	}

	fclose(dictionary);


	//������ȡ����
////////////////////////////////////////////////////////////////////////////////////////////////////////////

	for(int n = 0;n < N;n++)
	{
		//���ĳ����������
		struct TestList *thisTest;
		thisTest = List2[n];
		struct TestList *footer;
		//��ʼ��������ܿ�����
		countN = 0;
		
		//���ַ���welcome to code jam
		// w e l c o m ' ' t g d 
		struct TestList *pp;
		pp = thisTest->next;
		//
		char CharName[19] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};//�ֱ�洢������ĸ�������г��ֵĴ���
		int totalCount = 0;
		totalCount = f_searchChar(0,pp,CharName);
		OutPutData[n] = totalCount;

	}
	for(int n = 0;n<N;n++)
	{
		if(OutPutData[n] > 9999)
			OutPutData[n] = OutPutData[n] - OutPutData[n]/10000 * 10000;
		//printf("Case #%d: %04d\n",n+1,OutPutData[n]);
		fprintf(output,"Case #%d: %04d\n",n+1,OutPutData[n]);
	}
	fclose(output);
	printf("Finish");
	getchar();
}