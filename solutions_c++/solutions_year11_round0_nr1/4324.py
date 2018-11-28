#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>

using namespace std;

struct robots
{
	char b;
	robots* next;
};
int rollout(robots *P,int current);
void update(robots *P,int *current, int steps);
void main()
{
	ifstream in ("inL1.in");
	ofstream out("outL1.in");
	//out.open("output.in");
	int N;
	int T;
	int Case=0;

	in>>N;
	while (!in.eof())
	{
		in>>T;
		char *chrO=new char[T];
		char *chrB=new char[T];
		int *num=new int[T];

		robots *B = new robots;
		robots *O = new robots;
		robots *pO=NULL;
		robots *pB=NULL;
		char *name = new char[T];
		int steps=0;
		for (int i=0;i<T;i++)
		{	
			int bt;
			in>>name[i];
			in>>bt;
			if(name[i]=='O')
			{
				if(pO==NULL)
				{
					pO=O;
					pO->b=bt;
					pO->next=NULL;
				}
				else
				{
					robots *t=new robots;
					t->b=bt;
					t->next=NULL;
					pO->next=t;
					pO=pO->next;
				}

			}
			else
			{
				if(pB==NULL)
				{
					pB=B;
					pB->b=bt;
					pB->next=NULL;
					
				}
				else
				{
					robots *t=new robots;
					t->b=bt;
					t->next=NULL;
					pB->next=t;
					pB=pB->next;
				}
			}
		}

		Case++;
		if(pO==NULL)
		{
			steps+=rollout(B,1);
			
			out<<"Case #"<<Case<<": "<<steps<<endl;
			continue;
		}
		if(pB==NULL)
		{
			steps+=rollout(O,1);
			out<<"Case #"<<Case<<": "<<steps<<endl;
			continue;
		}

		int OC=1;//current O
		int BC=1;//current B
		pB=B;
		pO=O;
		bool flagO=true;
		bool flagB=true;
		for(int i=0;i<T;i++)
		{
			if(name[i]=='O')
			{
				//if(flagO==false)
				//	steps++;
				//flagO=true;
				int next;
				int step;
				next=pO->b;
				step = abs(next-OC);
				steps+=step;
				OC=next;
				update(pB,&BC,step);
					
				steps++;//push button
				pO=pO->next;
			}
			if(name[i]=='B')
			{
				int next;
				int step;
				next = pB->b;
				
				step = abs(next-BC);
				steps+=step;//move
				BC=next;
				update(pO,&OC,step);
					
				
				steps++;
				pB=pB->next;
			}
			
			if(pO==NULL)
			{
				steps+=rollout(pB,BC);
				break;
			}

			
			if(pB==NULL)
			{
				steps+=rollout(pO,OC);
				break;
			}	
		}
		out<<"Case #"<<Case<<": "<<steps<<endl;
	}
	in.close();
	out.close();
}
int rollout(robots *P,int current)
{
	int steps = 0;
	robots *p=P;
	int next = current;
	while(p!=NULL)
	{
		next = p->b;
		steps+=abs(next-current)+1;//move + update
		current = next;
		p=p->next;
	}
	//steps++;//push button
	return steps;
}
void update(robots *P,int *current, int steps)
{
	int distance = P->b - *(current);
	
	if (distance==0)
		return;
	if (abs(distance)>steps)
	{
		*(current)= *(current) + steps*(distance/abs(distance));
		*(current)= *(current)+(distance/abs(distance));
		return;
	}
	else
	{
		*(current) = P->b;
		return;
	}
}