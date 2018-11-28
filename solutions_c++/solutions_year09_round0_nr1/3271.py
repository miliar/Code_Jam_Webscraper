#include <stdio.h>
#include <stdlib.h>
#include "string.h"
#include <malloc.h>
#define L 10	//长度。没有结束符。非字符串
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
	//针对与某条测试数据
	int id;//与哪一条字典匹配
	struct piList *next;
};
//全局变量
struct WordList List[D];//字典条数据的列表

int f_countList(struct piList *p)
{
	int count = 0;
	while(p->next != NULL)
	{
		p = p->next;
		count ++;
	}
	//printf("长%d\n",count);
	return count;
}
struct piList* compare_add(char test,int index,struct piList *p)//将传入的测试数据test与字典列表比较
{
	//index从0开始 
	//返回匹配数目
	//从链表p中删除所有不匹配项
	
	//printf("\t\t比较字母%c\n",test);
	//printf("\t\t传入链表");
	//f_countList(p);
	int count = 0;//链表为空则为1 
	int i;
	struct piList* re;//返回链表
	re = (piList *)malloc(sizeof(piList));
	re->next = NULL;
	struct piList* s;//对链表re操作的指针
	s = re;
	while(p != NULL && p->next != NULL)
	{
		i = p->next->id;
		//printf("%d\t\t%c",i,test);
		if(List[i].letter[index] == test)//头节点没有数据
		{
			//创建一个节点
			//printf("相等\n");
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
	//printf("\t\t返回链表长度");
	f_countList(re);
	return re;//返回带头节点的链表
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

	//创建数组
	int i = 0;//字典数据条数 D
	for(i = 0 ;i < D;i ++)
	{
		//只读取数字型的数据
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
	
	//读取测试数据
	//读取字典采用格式化读取
	FILE* testdata;

	//读取基本参数 L D N
	//int L = 0,D = 0,N = 0;
	testdata = fopen("NNN.in","r");//字典数据文件
	struct TestList *List2[N];//测试数据的列表
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
			//链接
			s->next = p;
			s = p;
			//printf("%d",feof(testdata));
			//包含了结束符\n
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


	//正常读取数据

	//如果遇到（则开始循环比较
	int pi[N]={1};//每条测试数据的匹配项
	for(n = 0;n < N;n++)
	{
		//N条测试数据
		struct TestList *p;
		struct piList *thisTest,*thisTestP;
		int index = 0;
		p = List2[n];
		//记录此条测试数据与哪些字典匹配
		thisTest = (piList *)malloc(sizeof(piList));
		//初始化数据.假设全部匹配。含有头节点
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
		
		//重置头节点
		thisTestP = thisTest;
		printf("第%d条测试数据\n",n+1);
		//
		while(p != NULL && p->flag != '\n' && p->flag != '#')
		{
			//针对于某个块(字母+括号)的循环
			printf("dd");
			int ifnone = 0;//某个字母的匹配数目 
			//创建用于数据块的链表
			//数据块中随着多次比较字母，链表增长
			//退出数据块后将此次生成的最终链表带入下一个数据块的比较
			struct piList *thisArea;
			thisArea = (piList *)malloc(sizeof(piList));
			thisArea->next = NULL;
			printf("\t比较第%d数据块\n",index);
			if(p->flag == '(')
			{
				//则循环比较
				//printf("\t\t\t---------------------\n");
				p = p->next;
				//
				 while(p->flag != ')')
				 {
					//针对于某个字母
					
					//ifnone = compare(p->flag,index,thisTestP);//返回是否为空
					 //没有释放thisTestP的内存。
					 //
					struct piList* s = compare_add(p->flag,index,thisTestP);//返回带头节点的链表
					//printf("\t\t接受链表长度");
					//f_countList(s);
					//链接到这个数据块的专属链表
					struct piList* temp = thisArea;
					while(temp->next != NULL)//找到当前链表的结尾
						temp = temp->next;
					//把新生成的链表接到之前的链表上
					//if(s->next == NULL)
					//	printf("v");
					temp->next = s->next;//返回的链表有头节点
					
					p = p->next; //下一字母在次数据块中
					//继续在此数据块中查找下一个字母
				 }

				p = p->next;//跳过')'
				//printf("\t\t\t===========================\n");
			}
			else//如果不是括号则直接比较
			{
				//ifnone = compare(p->flag,index,thisTestP);//返回是否为空
					 //没有释放thisTestP的内存。
					 //
				struct piList* s = compare_add(p->flag,index,thisTestP);//返回带头节点的链表
				//printf("\t\t接受链表长度2");
				//f_countList(s);
				thisArea = s;

				p = p->next;//下一个字母/数据块
			}
			//继续下一个数据块
			//没有释放内存
			thisTestP = thisArea;
			if(thisArea->next == NULL)//如果没有匹配
				break;
			//printf("\t结束此数据块\n");
			index++;
		}
		//此测试匹配结束，输出结果
		pi[n] = f_countList(thisTestP);
		//释放内存
		printf("Case #%d: %d\n",n+1,pi[n]);
		fprintf(output,"Case #%d: %d\n",n+1,pi[n]);
	}


	fclose(output);
	//List2[0].flag = 's';
	//printf("%c\n",List2[0].flag );
		getchar();
}