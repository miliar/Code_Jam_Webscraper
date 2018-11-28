/* Enter your code here. Read input from STDIN. Print output to STDOUT */
#include <iostream> 
#include <string> 
#include <vector> 
#include <map> 
#include <stdio.h> 
#include <stdio.h>
#include <stdlib.h>
#include <limits>

using namespace std; 

// a list ds for numbers will be best for this 
typedef struct node 
	{
	int data; 
	struct node * next; 
	} NODE;

// add a new node to head list 
void add_to_head (struct node **head, struct node *newnode)
	{
	newnode->next = *head; 
	*head = newnode; 
	}

// convert integer to list 
struct node * to_list(long long i)
	{
	struct node * list = NULL; 
	while(i!=0)
		{
		int r = i % 10; 
		struct node * newnode = (struct node *) malloc (sizeof(struct node));
		newnode->data = r; 
		newnode->next = NULL; 
		add_to_head(&list, newnode); 
		i /= 10;
		}
	return list; 
	}

long long to_number(struct node * head)
	{
	struct node * current = head; 
	long long n = 0; 

	while(current != NULL)
		{
		int r = current->data; 
		n = n*10 + r; 
		current = current->next; 
		}

	return n; 
	}

struct node * concatenate(struct node * p1, struct node *p2)
	{
	if(p1 == NULL)
		{
		return p2; 	
		}

	struct node *current = p1; 
	while(current->next!=NULL)
		current = current->next; 
	current->next = p2; 
	return p1; 
	}

struct node *head(struct node *head)
	{
	struct node *current = head; 
	struct node *newnode = (struct node *) malloc (sizeof(struct node));
	if(!newnode)
		{
		cout << "memory limit" << endl; 
		return NULL; 
		}
	newnode->data = current->data; 
	newnode->next = NULL; 
	return newnode; 
	}

struct node *tail(struct node *head)
	{
	return (head->next); 
	}

vector<vector<long long> > glv; 

int digits(long long i)
	{
	int num = 0; 
	while(i!=0)
		{
		i /= 10;
		num ++; 
		}
	return num; 
	}

vector<long long> rotate(long long i)
	{
	vector<long long> v; 

	int d = digits(i); 

	struct node * xs = to_list(i); 
	do { 
		if ((to_number(xs) != i) && (d == digits(to_number(xs))))
			v.push_back(to_number(xs));
		xs = concatenate(tail(xs), head(xs));
		} while (to_number(xs) != i); 

	return v; 
	}

long long process (long long a, long long b)
	{
	long long n = 0; 
	for(long long i=a;i<=b;i++)
		{
		for (int j=0;j<glv[i].size();j++)
			{
			if( (i < glv[i][j]) && (glv[i][j]>=a) && (glv[i][j]<=b))
				{
				n++;
				}
			}
		}

	return n;
	}

int main () 
	{ 	
	int t; 
	cin >> t; 
	cin.clear(); // ignore erroneous line of input:
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
	vector<long long> temp; 
	temp.push_back(-1); 
	glv.push_back(temp); 
	for (long long i=1;i<=3000;i++)
		{
		vector<long long> rots = rotate(i);
		glv.push_back(rots); 
		}

	for(int i=0;i<t;i++)
		{
		long long a, b; 
		cin >> a; 
		cin >> b; 
		cout << "Case #" << (i+1) << ": " << process(a,b) << endl; 
		}
	return 0; 
	} 
