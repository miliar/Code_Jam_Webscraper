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
	int button;
	int step;
	node *next;
	node(int Button, int Step)
	{
		button=Button;
		step=Step;
		next=0;
	}
};

class list
{
public:
	node *head;
	node *tail;
	int count;
	void addNode(node *);
	void freeNodes();
	list()
	{
		head=0;
		count=0;
		tail=0;
	}
};
int calcSeconds(list, list);
void bot();

int main()
{
	bot();
	return 0;
}

void bot()
{
	int numCases=0;
	int numNum=0;
	int r=0;
	int k=0;
	int n=0;
	int button;
	int seconds=0;
	int step=0;
	char color;
	scanf("%d",&numCases);
	list blue;
	list orange;
	for (int i=0;i<numCases;i++)
	{
		scanf("%d",&n);
		for (int j=0;j<n;j++)
		{
			scanf(" %c %d", &color,&button);
			if (color=='B')
			{
				blue.addNode(new node(button, j+1));
			}
			else if (color=='O')
			{
				orange.addNode(new node(button, j+1));
			}
		}
		seconds=calcSeconds(blue, orange);
		printf("Case #%d: %d\n", i+1,seconds);
		blue.freeNodes();
		orange.freeNodes();
	}
	return;
}

void list::addNode(node *Node)
{
	if (head==0)
	{
		head=Node;
		tail=Node;
		head->next=0;
	}
	else
	{
		tail->next=Node;
		tail=Node;
	}
	count++;
}

void list::freeNodes()
{
	node *ptr=head;
	node *ptr2;
	for (int i=0;i<count;i++)
	{
		ptr2=ptr->next;
		delete ptr;
		ptr=ptr2;
	}
	count=0;
	head=0;
	return;
}

int calcSeconds(list blue, list orange)
{
	int seconds=0;
	int flag=0;
	node *bPtr;
	node *oPtr;
	bPtr=blue.head;
	oPtr=orange.head;
	int step=1;
	int oCurrentButton=1;
	int bCurrentButton=1;
	int bMoved=0;
	int oMoved=0;
	while(oPtr!=0 || bPtr!=0)
	{
		flag=0;
		bMoved=0;
		oMoved=0;
		if (bPtr!=0)
		{
			if (step==bPtr->step && bCurrentButton==bPtr->button)
			{
				step++;
				bPtr=bPtr->next;
				flag=1;
				bMoved=1;
			}
		}
		if (oPtr!=0)
		{
			if (step==oPtr->step && oCurrentButton==oPtr->button && flag==0)
			{
				step++;
				oPtr=oPtr->next;
				oMoved=1;
			}
		}
		if (bMoved==0 && bPtr!=0)
		{
			if (bCurrentButton < bPtr->button)
			{
				bCurrentButton++;
			}
			else if (bCurrentButton > bPtr->button)
			{
				bCurrentButton--;
			}
		}
		if (oMoved==0 && oPtr!=0)
		{
			if (oCurrentButton < oPtr->button)
			{
				oCurrentButton++;
			}
			else if (oCurrentButton > oPtr->button)
			{
				oCurrentButton--;
			}
		}
		seconds++;
	}
	return seconds;
}