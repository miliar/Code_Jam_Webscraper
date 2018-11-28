#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <float.h>
#include <limits.h>
#include <time.h>
#include <ctype.h>
#include <iostream>
using namespace std;


class node
{
public:
	char element;
	char pair;
	int exists;
	node *next;
	node()
	{
		element='\0';
		pair='\0';
		exists=0;
		next=0;
	}
};


class base
{
public:
	node *combine;
	node *oppose;
	base()
	{
		combine=0;
		oppose=0;
	}
};
class list
{
public:
	base elements[100];
	node elementExists[100];
	int count;
	char elementList[100];
	void addNode(char element1, char element2, char nonBaseElement);
	void addNode(char element1, char element2);
	void freeNodes();
	void addElement(char);
	void printElementList();
	void clearList();
	list()
	{
		count=0;
	}
};

void magicka();

int main()
{
	magicka();
	return 0;
}
void magicka()
{
	int numCases=0;
	int numNum=0;
	int c=0;
	int d=0;
	int n=0;
	char elements[3];
	list elementList;
	scanf("%d",&numCases);
	for (int i=0;i<numCases;i++)
	{
		scanf("%d ",&c);
		for (int j=0;j<c;j++)
		{
			scanf("%c%c%c ",&elements[0],&elements[1],&elements[2]);
			elementList.addNode(elements[0], elements[1], elements[2]);
		}
		scanf("%d ", &d);
		for (int j=0;j<d;j++)
		{
			scanf("%c%c ",&elements[0],&elements[1]);
			elementList.addNode(elements[0], elements[1]);
		}
		scanf("%d ", &n);
		for (int j=0;j<n;j++)
		{
			scanf("%c",&elements[0]);
			elementList.addElement(elements[0]);
		}
		printf("Case #%d: ",i+1);
		elementList.printElementList();
		printf("\n");
		elementList.freeNodes();
	}
	return;
}

void list::addNode(char element1, char element2, char nonBaseElement)
{
	node *ptr=elements[element1].combine;
	node *ptr2=ptr;
	if (ptr!=0)
	{
		while (ptr!=0)
		{
			ptr2=ptr;
			ptr=ptr->next;
		}
		ptr2->next=new node();
		ptr2->next->element=nonBaseElement;
		ptr2->next->pair=element2;
		ptr2->next->exists=1;
	}
	else
	{
		elements[element1].combine=new node();
		elements[element1].combine->element=nonBaseElement;
		elements[element1].combine->pair=element2;
		elements[element1].combine->exists=1;
	}

	ptr=elements[element2].combine;
	ptr2=ptr;
	if (ptr!=0)
	{
		while (ptr!=0)
		{
			ptr2=ptr;
			ptr=ptr->next;
		}
		ptr2->next=new node();
		ptr2->next->element=nonBaseElement;
		ptr2->next->pair=element1;
		ptr2->next->exists=1;
	}
	else
	{
		elements[element2].combine=new node();
		elements[element2].combine->element=nonBaseElement;
		elements[element2].combine->pair=element1;
		elements[element2].combine->exists=1;
	}
}

void list::addNode(char element1, char element2)
{
	node *ptr=elements[element1].oppose;
	node *ptr2=ptr;
	if (ptr!=0)
	{
		while (ptr!=0)
		{
			ptr2=ptr;
			ptr=ptr->next;
		}
		ptr2->next=new node();
		ptr2->next->pair=element2;
		ptr2->next->exists=1;
	}
	else
	{
		elements[element1].oppose=new node();
		elements[element1].oppose->pair=element2;
		elements[element1].oppose->exists=1;
	}

	ptr=elements[element2].oppose;
	ptr2=ptr;
	if (ptr!=0)
	{
		while (ptr!=0)
		{
			ptr2=ptr;
			ptr=ptr->next;
		}
		ptr2->next=new node();
		ptr2->next->pair=element1;
		ptr2->next->exists=1;
	}
	else
	{
		elements[element2].oppose=new node();
		elements[element2].oppose->pair=element1;
		elements[element2].oppose->exists=1;
	}
}

void list::freeNodes()
{
	node *ptr;
	node *ptr2;
	for (int i=0;i<100;i++)
	{
		elementExists[i].exists=0;
		ptr=elements[i].combine;
		while(ptr!=0)
		{
			ptr2=ptr->next;
			delete ptr;
			ptr=ptr2;			
		}
		elements[i].combine=0;
		ptr=elements[i].oppose;
		while(ptr!=0)
		{
			ptr2=ptr->next;
			delete ptr;
			ptr=ptr2;			
		}
		elements[i].oppose=0;
	}
	count=0;
}

void list::addElement(char newElement)
{//printElementList(); printf("  Adding element: %c.  count=%d\n",newElement,count);
	node *ptr=elements[newElement].combine;
	while(ptr!=0)
	{
		if (elementList[count-1]==ptr->pair && count>0)
		{//printf("got here: %c \n",elementList[0]);
			elementExists[elementList[count-1]].exists--;
			elementList[count-1]=ptr->element;
			return;
		}
		ptr=ptr->next;
	}
	ptr=elements[newElement].oppose;
	while(ptr!=0)
	{
		if (elementExists[ptr->pair].exists>0)
		{
			count=0;
			clearList();
			return;
		}
		ptr=ptr->next;
	}
	elementList[count]=newElement;
	count++;
	elementExists[newElement].exists++;
}

void list::printElementList()
{

	printf("[");

	for (int i=0;i<count;i++)
	{
		printf("%c",elementList[i]);
		if (i<(count-1))
		{
			printf(", ");
		}
	}
	printf("]");
}


void list::clearList()
{
	for (int i=0;i<100;i++)
	{
		elementExists[i].exists=0;
	}
}