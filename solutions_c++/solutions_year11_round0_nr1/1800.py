/*
 *  Bot-Trust.cpp
 *  
 *
 *  Created by Shobhit Srivastava on 07/05/11.
 *  Copyright 2011 IIT Rajisthan. All rights reserved.
 *
 */


#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main() 
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for(int test=1;test<=t;test++) 
	{
		int button;
		char bot;
		int currentO=1,currentB=1;
		int pressO=1000,pressB=1000;
		int butorder[100];
		char botorder[100];
		int time=0;
		int movetimeO,movetimeB;
		int n;
		int i,k;
		scanf("%d ",&n);
		for (i=0; i<n;i++)
		{
			scanf(" %c %d ",&bot,&button);
			
			butorder[i]=button;
			botorder[i]=bot;
		}

		for (i=0; i<n ; i++)
		{
			if(botorder[i]=='O')
			{
				if ( i!=pressO)
				{
					
					if(currentO < butorder[i])
						movetimeO=butorder[i]-currentO+1;
					else
						movetimeO=currentO-butorder[i]+1;
								
					time=time+movetimeO;
					currentO=butorder[i];
					pressO=i;
					
					for (k=i+1;k<n;k++)
						if (botorder[k]=='B')
							break;
					
					movetimeB=1000;
					if(k!=n)
					{
					if(currentB < butorder[k])
						movetimeB=butorder[k]-currentB;
					else
						movetimeB=currentB-butorder[k];
					}
					
					if(movetimeO >= movetimeB)
					{
						currentB=butorder[k];
					}	
					else
					{
						if(currentB < butorder[k])
							currentB=currentB+movetimeO;
						else
							currentB=currentB-movetimeO;
					}
				}
			}
				else
					if ( i!=pressB)
					{
						
						if(currentB < butorder[i])
							movetimeB=butorder[i]-currentB+1;
						else
							movetimeB=currentB-butorder[i]+1;
					
						time=time+movetimeB;
						currentB=butorder[i];
						pressB=i;
						
						for (k=i+1;k<n;k++)
							if (botorder[k]=='O')
								break;
						
						movetimeO=1000;
						if(k!=n)
						{
						if(currentO < butorder[k])
							movetimeO=butorder[k]-currentO;
						else
							movetimeO=currentO-butorder[k];
						}
						
						if(movetimeB >= movetimeO)
						{
							currentO=butorder[k];
						}	
						else
						{
							if(currentO < butorder[k])
								currentO=currentO+movetimeB;
							else
								currentO=currentO-movetimeB;
						}
					}
		}
		cout << "Case #"<<test<<": "<<time<<endl;
	}
	return 0;
}




