#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

#define N 100

struct TestList//双向链表
{
	char flag;
	int id;
	struct TestList *next ;
	struct TestList *pre ;
};

//全局变量
struct TestList* f_getCharP(struct TestList* p,char x,int index)
{
	//返回第index个x的指针.index 从0开始
	int count = 0;
	while( p != NULL)
	{
		if(p->flag == x)
			count ++;
		if(count == index+1)
			break;
		p = p->next;
	}
	//传入的参数保证能够找到
	return p;
}
int f_CharAfterNum(struct TestList *p,char x)//从p开始到最后是否存在x字符。返回存在个数
{
	//x是需要查找的字符
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
int f_searchChar(int i,struct TestList *thisP,char a[])//i是字符序号
{
	//所有字母指针构成的数组
	/*
	针对于某一个字符，有多种可能的位置。
	针对于其中的一个位置，搜索下一个字符。是welcome的下一个字符，而不是测试数据中的
	
	*/
	//得到这个字符的可能位置数t
	int t = f_CharAfterNum(thisP,a[i]);
	//针对于任一个位置递归
	for(int g = 0;g < t;g++)
	{
		//得到这个位置的指针
		struct TestList *thisNew = f_getCharP(thisP,a[i],g);//返回thisP指针后i个a[i]的指针地址
		//如果这个位置不是最后一个字符，则递归
		if(i == 18)
		{
			//printf("%c",a[preI]);
			//printf("%d",f_CharAfterNum(thisS,a[preI]));	
			countN ++;
		}
		else
		{
			//递归时是用当前位置替换初始位置，查找字符为下一个数组变量
			f_searchChar(i+1,thisNew,a);
		}
	}
	//printf("%d ",count);
	return countN;
}
void main()
{
	//读取字典采用格式化读取
	FILE* dictionary;

	FILE* output;
	//读取基本参数 L D N
	//int L = 0,D = 0,N = 0;
	dictionary = fopen("DDD.in","r");//字典数据文件
	output = fopen("Out.out","w");
	if(dictionary==0)
	 {
		 printf("error_1");
	 }
	//printf("%d+%d+%d",L,D,N);//测试正常
	//struct WordList *List;//字典条数据的列表

	struct TestList *List2[N];//测试数据的列表
	int OutPutData[N];
	int n= 0;//N条测试数据
	for(n = 0;n < N;n++)
	{
		//只读取数字型的数据
		//char temp[];
		struct TestList *s;
		char temp = ' ';
		s = (TestList *)malloc(sizeof(TestList));
		List2[n] = (TestList *)malloc(sizeof(TestList));
		s = List2[n];
		//printf("%c",temp);
		s->flag = '-';
		s->id = -1;
		s->next = NULL;//包含头节点
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
			//链接
			s->next = p;
			s = p;
			//printf("%d",feof(dictionary));
			//包含了结束符\n
		}
		//printf("%d\n",n);
	}

	fclose(dictionary);


	//正常读取数据
////////////////////////////////////////////////////////////////////////////////////////////////////////////

	for(int n = 0;n < N;n++)
	{
		//针对某条测试数据
		struct TestList *thisTest;
		thisTest = List2[n];
		struct TestList *footer;
		//初始化该组的总可能性
		countN = 0;
		
		//简化字符串welcome to code jam
		// w e l c o m ' ' t g d 
		struct TestList *pp;
		pp = thisTest->next;
		//
		char CharName[19] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};//分别存储各个字母在链表中出现的次数
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