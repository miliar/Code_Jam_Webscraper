#include <cstdio>
#include <stack>
using namespace std;

// QWERASDF = 01234567

char combine[10][10];
int count[10];

bool opp[10][10];

stack<char> mys;



int lk(char c)
{
	switch(c)
	{
		case 'Q':
			return 0;
		case 'W':
			return 1;
		case 'E':
			return 2;
		case 'R':
			return 3;
		case 'A':
			return 4;
		case 'S':
			return 5;
		case 'D':
			return 6;
		case 'F':
			return 7;
		default:
			//printf("error =/");
			return 9;
	}
	return 8;
}
			

void clearit()
{
	int sizething = mys.size();
	for(int i=0; i<sizething; i++)
	{
		char temptop = mys.top();
		count[lk(temptop)]--;
		mys.pop();
	}
	if(!mys.empty())
	{
		printf("clearning failed!\n");
	}
}




int main()
{
	FILE* filein = fopen("B-large.in", "r");
	FILE* fileout = fopen("output.txt", "w");
	
	
	int numtests;
	fscanf(filein, "%d", &numtests);
	for(int currtest=0; currtest<numtests; currtest++)
	{
		int numcomb;
		fscanf(filein, "%d", &numcomb);
		for(int i=0; i<numcomb; i++)
		{
			char temp[5];
			fscanf(filein, "%s", temp);
			combine[lk(temp[0])][lk(temp[1])] = temp[2];
			combine[lk(temp[1])][lk(temp[0])] = temp[2];
		}
		
		int numopp;
		fscanf(filein, "%d", &numopp);
		for(int i=0; i<numopp; i++)
		{
			char temp[5];
			fscanf(filein, "%s", temp);
			opp[lk(temp[0])][lk(temp[1])]=true;
			opp[lk(temp[1])][lk(temp[0])]=true;
		}
		
		int numgo;
		fscanf(filein, "%d", &numgo);
		char temp[105];
		fscanf(filein, "%s", temp);
		for(int i=0; i<numgo; i++)
		{
			char curr = temp[i];
			printf("curr:%c\n", curr); // make sure it scans right
			
			// now go invoking some stuffs. curr is the item to add.
			
			if(mys.empty())
			{
				mys.push(curr);
				count[lk(curr)]++;
				printf("empty; adding\n");
			}
			else
			{
				bool combined = false;
				// something is on the stack
				
				// if we invoke this, will it combine with the top element?
				
				// first, is the top element a base element?
				
				char topelem = mys.top();
				
				if(lk(mys.top())>7)
				{
					printf("top isn't base\n");
					// nope
				}
				else
				{
					if(combine[lk(mys.top())][lk(curr)] != 0)
					{
						printf("top combines to make smth\n");
						// they make something
						combined = true;
						mys.pop();
						count[lk(topelem)]--;
						mys.push(combine[lk(topelem)][lk(curr)]);
					}

				}
				if(!combined)
				{
					// add the top element.
					// first check it doesn't asplode
					bool asplode = false;
					for(int x=0; x<8; x++)
					{
						if(count[x]>0)
						{
							// we have some of whatever x is on there
							// will curr asplode with x?
							if(opp[lk(curr)][x])
							{
								// yes, will asplode
								// clear the whole list
								printf("curr asplodes\n");
								clearit();
								asplode = true;
								for(int k=0; k<10; k++)
								{
									count[k]=0;
								}
							}
						}
					}
					if(!asplode)
					{
						printf("adding curr\n");
						// actually add it
						mys.push(curr);
						count[lk(curr)]++;
					}
				}
			}
		}
		
		//printf("%d***\n", mys.size());
		
		stack<char> rev;
		int sizething = mys.size();
		for(int i=0; i<sizething; i++)
		{
			rev.push(mys.top());
			printf("%c ", mys.top());
			mys.pop();
		}		
		
		fprintf(fileout, "Case #%d: [", currtest+1);
		for(int i=0; i<sizething; i++)
		{		
			if(rev.size()>1)
			{
				fprintf(fileout, "%c, ", rev.top());
			}
			else
			{
				fprintf(fileout, "%c", rev.top());
			}
			rev.pop();
		}
		fprintf(fileout, "]\n");
		
		for(int i=0; i<10; i++)
		{
			for(int j=0; j<10; j++)
			{
				combine[i][j]=0;
				opp[i][j]=0;
			}
			count[i]=0;
		}
	}
}
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
