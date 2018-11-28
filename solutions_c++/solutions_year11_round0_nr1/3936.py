#include <cstdio>
#include <utility>
using namespace std;

typedef pair<int, int> node;

node instruct[200];
int oranges[200];
int blues[200];

int main()
{
    FILE* filein = fopen("A-large.in", "r");
	FILE* fileout = fopen("output.txt", "w");

	int numtests;
	fscanf(filein, "%d", &numtests);

	for(int currtest=0; currtest<numtests; currtest++)
	{
	    int numcom;
	    int orangeup=0;
	    int blueup=0;
	    fscanf(filein, "%d", &numcom);
	    for(int i=0; i<numcom; i++)
	    {
			char temp;
			fscanf(filein, "%c", &temp);
			while(!(temp == 'O' || temp == 'B'))
			{
				fscanf(filein, "%c", &temp);
			}
				
			int number;
			fscanf(filein, "%d", &number);

			if(temp=='O')
			{
				instruct[i].first=0;
				instruct[i].second=number;
				oranges[orangeup++]=number;
			}
			if(temp=='B')
			{
				instruct[i].first=1;
				instruct[i].second=number;
				blues[blueup++]=number;
			}
	    }

		

	    // simulate

	

	    int stepupto = 0;
	    int numsteps = 0;
	    int orangepos = 1;
	    int bluepos = 1;
	    int orangeupto = 0;
	    int blueupto = 0;
	    int orangemax = orangeup;
	    int bluemax = blueup;
	    bool orangedone = false;
	    bool bluedone = false;
	    bool hitbutton = false;
	    
	    while(true)
	    {
			//printf("****** starting a turn ********\n");
			// move orange

			//printf("o: %d || b: %d\n", orangepos, bluepos);
			
			//printf("current instruction (%d): move %d to %d\n", stepupto, instruct[stepupto].first, instruct[stepupto].second);
			
			
			if(orangepos == oranges[orangeupto] && orangedone)
			{
				// we have just hit a button in our last turn
				////printf("orange moving to next instruction\n");
				orangedone = false;
				orangeupto++;

				// move and stuff. or maybe hit the button again, who knows?
				if(orangeupto >= orangemax)
				{
					// we're done
				}
				else
				{
					// we still have instructions left
					if(orangepos == oranges[orangeupto] && instruct[stepupto].first==0 && instruct[stepupto].second==orangepos)
					{
						// hit a button
						orangedone = true;
						//printf("orange hitting a button case b\n");
						hitbutton = true;
					}

					if(orangepos > oranges[orangeupto])
					{
						orangepos--;
						// move backwards
						//printf("orange moving backwards\n");
					}
					if(orangepos < oranges[orangeupto])
					{
						orangepos++;
						//move forwards
						//printf("orange moving forwards\n");
					}
				}
			}
			else if(orangepos == oranges[orangeupto] && !orangedone)
			{
				// we have just moved here and now we need to hit a button
		   
				// but can we hit a button yet?
				if(instruct[stepupto].first==0 && instruct[stepupto].second==orangepos)
				{
				// we are meant to be hitting this button now.
				// so hit that button.
					orangedone = true;
					//printf("orange hitting a button\n");
					hitbutton = true;
					//orangeupto++;

				}
				else
				{
					//printf("orange waiting to hit a button\n");
				}
				
				// don't move
			}
			else
			{
				// no buttons; we're either done or in the process of getting to one
				if(orangeupto >= orangemax)
				{
					// we're done
				}
				else
				{
					if(orangepos > oranges[orangeupto])
					{
						orangepos--;
						//printf("orange moving backwards\n");

					}
					if(orangepos < oranges[orangeupto])
					{
						orangepos++;						
						//printf("orange moving forwards\n");

					}
				}
			}

			// move blue

			if(bluepos == blues[blueupto] && bluedone)
			{
				// we have just hit a button in our last turn
				bluedone = false;
				blueupto++;

				// move and stuff
				if(blueupto >= bluemax)
				{
					// we're done
				}
				else
				{
					// we still have instructions left
					
					if(bluepos == blues[blueupto] && instruct[stepupto].first==1 && instruct[stepupto].second==bluepos)
					{
						// hit a button again
						bluedone = true;
						//printf("blue hitting button case b\n");
						hitbutton = true;
					}
					
					if(bluepos > blues[blueupto])
					{
						bluepos--;
						// move backwards
						//printf("blue moving back\n");
					}
					if(bluepos < blues[blueupto])
					{
						bluepos++;
						//move forwards
						//printf("blue moving fowards\n");
					}
				}
			}
			else if(bluepos == blues[blueupto] && !bluedone)
			{
				// we have just moved here and now we need to hit a button
		   
				// but can we hit a button yet?
				if(instruct[stepupto].first==1 && instruct[stepupto].second==bluepos)
				{
				// we are meant to be hitting this button now.
				// so hit that button.
					bluedone = true;
					//printf("blue hitting button\n");
					hitbutton = true;
					//blueupto++;
				}
				else
				{
					//printf("blue waiting to hit button\n");
				}
				
				// don't move
			}
			else
			{
				// no buttons; we're either done or in the process of getting to one
				if(blueupto >= bluemax)
				{
					// we're done
				}
				else
				{
					if(bluepos > blues[blueupto])
					{
						bluepos--;
						//printf("blue moving back\n");
					}
					if(bluepos < blues[blueupto])
					{
						bluepos++;
						//printf("blue moving foward\n");
					}
				}
			}
			if(orangeupto >= orangemax && blueupto >= bluemax)
			{
				break;
			}
			
			if(hitbutton)
			{
				stepupto++;
				hitbutton = false;
			}
			
			
			numsteps++;
			
			

		}
		//printf("%d steps\n", numsteps);
		fprintf(fileout, "Case #%d: %d\n", currtest+1, numsteps);
		
		stepupto = 0;
	    numsteps = 0;
	    orangepos = 1;
	    bluepos = 1;
	    orangeupto = 0;
	    blueupto = 0;
	    orangemax = orangeup;
	    bluemax = blueup;
	    orangedone = false;
	    bluedone = false;
	    hitbutton = false;
		
	}
	
	
	
	
}

		    



