#include <iostream>
#include <queue>
using namespace std;

struct Node
{
	int data;
	Node *next;
	Node()
	{
		data = 0;
		next = NULL;
	}
};


void main()
{	


	unsigned int R = 0;
	unsigned int K = 0;
	unsigned int N = 0;
	unsigned int T = 0;
	freopen("C-small-attempt1.in","r",stdin);
	cin >> T;
	for(unsigned int it =0; it< T; it++)
	{
		Node *current= NULL;
		Node *Last= NULL;
		Node *kValueNode = NULL;
		Node *kValueNodeCurrent = NULL;
		cin >> R;
		cin >> K;
		cin >> N;		
		queue<unsigned int> Nqueue;
		queue<unsigned int> NqueueSample;
		for(unsigned int in = 0; in < N ; in++ )
		{
			unsigned int temp;
			cin >> temp;
			Node *tNode = (Node *)malloc(sizeof(Node));
			tNode->data = temp;
			tNode->next = NULL;
			if(in == 0)
			{				
				current =  tNode;
				Last = tNode;
			}
			else
			{				
				Last ->next = tNode;
				Last = tNode;
				Last ->next = NULL;
			}
		}

		int euro = 0;
		for(unsigned int ir = 0; ir < R ; ir++ )
		{					
			unsigned int kValue = 0;
			bool bExit = false;
			unsigned int top = 0;
			
			do
			{				
				top = current->data;				
				kValue += top;
				

				if(kValue <= K )
				{
					if(kValueNode == NULL)
					{
						kValueNodeCurrent = kValueNode =  current;
						current = current->next;
						kValueNode ->next = NULL;

					}
					else
					{
						kValueNodeCurrent->next =  current;						
						current = current->next;	
						kValueNodeCurrent = kValueNodeCurrent->next;
						kValueNodeCurrent->next = NULL;
					}
					euro += top;
				}
				else
				{					
					bExit = true;
				}
				if(current == NULL)
				{					
					break;
				}
			}
			while( !bExit ) ;	
			if(current != NULL)
			{
				Last->next = kValueNode;			
				Last = kValueNodeCurrent;			
				kValueNode = NULL;
			}
			else
			{
				current = kValueNode;
				Last = kValueNodeCurrent;			
				kValueNode = NULL;
			}			
		}
		cout<<"Case #"<<it+1<<": "<<euro<<endl;
		while(current)
		{
			kValueNode = current ;
			current = current->next ;
			delete  kValueNode;
		}
	}
}