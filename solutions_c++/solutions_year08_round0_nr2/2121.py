# include <stdio.h>
# include <conio.h>
# include <stdlib.h>

#define MAX_T		60
#define MAX_N       100
#define MAX_NAB		100

char CharToHex (char a, char b)
{
	#define LMASK	0x0F
	
	char c, d, e;
	
	d = a - 0x30;
	
	e = b - 0x30;
	
	c = (d * 10) + (e);
	
	// printf ("%d %d %d\n", d, e, c);
	
	return (c);
}

void Sort (char a [] [4], char N)
{
	int i;
	int j;
	char temp = 0;
	
	//  Sort the array in Ascending order
	
	for (i = 0; i < N; i ++)
	for (j = i + 1; j < N; j ++)
	{
		if (a [j] [0] < a [i] [0])
		{
			temp = a [i] [0];
			a [i] [0] = a [j] [0];
			a [j] [0] = temp;
			
			temp = a [i] [1];
			a [i] [1] = a [j] [1];
			a [j] [1] = temp;
			
			temp = a [i] [2];
			a [i] [2] = a [j] [2];
			a [j] [2] = temp;
			
			temp = a [i] [3];
			a [i] [3] = a [j] [3];
			a [j] [3] = temp;
		}
		else if (a [j] [0] == a [i] [0])
		{
            if (a [j] [1] < a [i] [1])
            {
    			temp = a [i] [0];
    			a [i] [0] = a [j] [0];
    			a [j] [0] = temp;
    			
    			temp = a [i] [1];
    			a [i] [1] = a [j] [1];
    			a [j] [1] = temp;
    			
    			temp = a [i] [2];
    			a [i] [2] = a [j] [2];
    			a [j] [2] = temp;
    			
    			temp = a [i] [3];
    			a [i] [3] = a [j] [3];
    			a [j] [3] = temp;
            }
		}
	}
	
	printf ("\n\n\n");
	
	for (i = 0; i < N; i ++)
	{
        printf ("%d %d %d %d\n", a [i] [0], a [i] [1], a [i] [2], a [i] [3]);
    }
    getch ();
}

void TrainReuse (char ATimeTbl [] [4], char BTimeTbl [] [4], char TrainNOs [], char NA, char NB)
{
	int i;
	int j;
	
	// Compare A arrival with B departure
    for (i = 0; i < NA; i ++)
	for (j = 0; j < NB; j ++)
	{
        if (0 == TrainNOs [NA + j])
        {
            continue;
        }
		if (ATimeTbl [i] [2] == BTimeTbl [j] [0])
		{
			if (ATimeTbl [i] [3] <= BTimeTbl [j] [1])
			{
				// Match
				// TrainNOs [NA + j] = TrainNOs [i];
				TrainNOs [NA + j] = 0;
				break;
			}
			continue;
		}
		
		if (ATimeTbl [i] [2] < BTimeTbl [j] [0])
		{
			// Match
			// TrainNOs [NA + j] = TrainNOs [i];
			TrainNOs [NA + j] = 0;
			break;
		}
	}
	
	
	// Compare B arrival with A departure
	for (i = 0; i < NB; i ++)
	for (j = 0; j < NA; j ++)
	{
        if (0 == TrainNOs [j])
        {
            continue;
        }
        
		if (BTimeTbl [i] [2] == ATimeTbl [j] [0])
		{
			if (BTimeTbl [i] [3] <= ATimeTbl [j] [1])
			{
				// Match
				// TrainNOs [j] = TrainNOs [NA + i];
				TrainNOs [j] = 0;
				break;
			}
			continue;
		}
		
		if (BTimeTbl [i] [2] < ATimeTbl [j] [0])
		{
			// Match
			// TrainNOs [j] = TrainNOs [NA + i];
			TrainNOs [j] = 0;
			break;
		}
	}
}



int main (void)
{
	int N = 0;
	int T [100];
	int NA [100], NB [100];
	char ATimeTbl [100] [4], BTimeTbl [100] [4];
	char TrainNOs [200];
	char TrainFrmA [100];
	char TrainFrmB [100];
	
	FILE * fpI, * fpO;
	char chT1, chT2;
	int i;
	int k = 0;
	
	fpI = fopen ("Input.txt", "r");
	fpO = fopen ("Output.txt", "w");
	
	fscanf (fpI, "%d", &N);
	if (N > MAX_N)
	{
        printf ("Invalid no of Cases");
        exit (0);
    }
	
	while (k < N)
	{
        i = 0;
    	fscanf (fpI, "%d", &T [k]);
    	
    	if (T [k] > MAX_T)
    	{
            printf ("Invalid Turnaround time");
            exit (0);
        }
        
    	fscanf (fpI, "%d %d\n", &NA [k], &NB [k]);
    	
    	if ((NA [k] > MAX_NAB) || (NB [k] > MAX_NAB))
    	{
            printf ("Invalid no of trips");
            exit (0);
        }
    	
    	while (i < (NA [k]))
    	{
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		ATimeTbl [i] [0] = CharToHex (chT1, chT2);
    		
    		// Skip the :
    		fscanf (fpI, "%c", &chT1);
    		
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		ATimeTbl [i] [1] = CharToHex (chT1, chT2);
    		
    		// Skip the space
    		fscanf (fpI, "%c", &chT1);
    		
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		ATimeTbl [i] [2] = CharToHex (chT1, chT2);
    		
    		// Skip the :
    		fscanf (fpI, "%c", &chT1);
    		
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		ATimeTbl [i] [3] = CharToHex (chT1, chT2);
    		ATimeTbl [i] [3] += T [k];
    		
    		if (ATimeTbl [i] [3] >= 60)
    		{
                ATimeTbl [i] [2] += 1;
                ATimeTbl [i] [3] -= 60;
            }
    		
    		// Skip the new line
    		fscanf (fpI, "%c", &chT1);
    		
    		i ++;
    	}
    	i = 0;
    	
    	while (i < NB [k])
    	{
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		BTimeTbl [i] [0] = CharToHex (chT1, chT2);
    		
    		// Skip the :
    		fscanf (fpI, "%c", &chT1);
    		
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		BTimeTbl [i] [1] = CharToHex (chT1, chT2);
    		
    		// Skip the space
    		fscanf (fpI, "%c", &chT1);
    		
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		BTimeTbl [i] [2] = CharToHex (chT1, chT2);
    		
    		// Skip the :
    		fscanf (fpI, "%c", &chT1);
    		
    		fscanf (fpI, "%c%c", &chT1, &chT2);
    		BTimeTbl [i] [3] = CharToHex (chT1, chT2);
    		BTimeTbl [i] [3] += T [k];
    		
    		if (BTimeTbl [i] [3] >= 60)
    		{
                BTimeTbl [i] [2] += 1;
                BTimeTbl [i] [3] -= 60;
            }
    		
    		// Skip the new line
    		fscanf (fpI, "%c", &chT1);
    		
    		i ++;
    	} 
    	
    	for (i = 0; i < (NA [k] + NB [k]); i ++)
    	{
    		TrainNOs [i] = i + 1;
    	}
    	
        // Sort NA
    	Sort (ATimeTbl, NA [k]);
    	
    	// Sort NB
    	Sort (BTimeTbl, NB [k]);
    	
    	// Find Reusable Trains
    	TrainReuse (ATimeTbl, BTimeTbl, TrainNOs, NA [k], NB [k]);
    	
    	TrainFrmA [k] = 0;
    	TrainFrmB [k] = 0;
    	
    	// Find the no of trains from Station A and Station B
        for (i = 0; i < (NA [k] + NB [k]); i ++)
    	{
            if (0 == TrainNOs [i])
            {
                continue;
            }
            if (TrainNOs [i] <= NA [k])
            {
                TrainFrmA [k] ++;
            }
            else
            {
                TrainFrmB [k] ++;
            }
        }
        
        k ++;
    }
    
    printf ("\n\n");
    
    for (k = 0; k < N; k ++)
    {
        fprintf (fpO, "Case #%d: %d %d\n", (k + 1), TrainFrmA [k], TrainFrmB [k]);
    }
	
	return 0;
}
