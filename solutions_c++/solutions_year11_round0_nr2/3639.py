// GjamCpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <string>
#include <iostream>
#include "ButtonEventList.h"

class CombinerList
{
public:
	char Combiner[4];
	CombinerList *nextCombiner;

	CombinerList()
	{
	}
};

class DestroyerList
{
public:
	char Destroyer[3];
	DestroyerList *nextDestroyer;

	DestroyerList()
	{
	}
};

class FinalElementsList
{
public:
	char Element[2];
	FinalElementsList *nextElement;

	FinalElementsList()
	{
	}
};

int main()
{
	int i,j,k;
	//printf("Hello world!\n");

	int Number_of_TestCases=0;
	int Number_of_Combiners=0;
	int Number_of_Destroyers=0;
	scanf("%d",&Number_of_TestCases);
	int l=1;
	i=1;
	
	CombinerList *globalCombinerList;
	DestroyerList *globalDestroyerList;
	FinalElementsList *globalFinalElementsList;
	char *current_element;
	char *last_element;
	char *testElementString;

	globalDestroyerList = NULL;
	globalCombinerList = NULL;

	while(l<=Number_of_TestCases)
	{
		i=1;
		scanf("%d",&Number_of_Combiners);
		CombinerList *pCombinerList;
		CombinerList *iCombinerList;

		while(i<=Number_of_Combiners)
		{
			char combiner_string[4];

			scanf("%s",combiner_string);

			iCombinerList = new CombinerList();
			iCombinerList->Combiner[0] = combiner_string[0];
			iCombinerList->Combiner[1] = combiner_string[1];
			iCombinerList->Combiner[2] = combiner_string[2];
			iCombinerList->Combiner[3] = '\0';
			iCombinerList->nextCombiner = NULL;

			if(i == 1)
			{
				globalCombinerList = iCombinerList;

				pCombinerList = iCombinerList;
				i++;
				continue;
			}
			pCombinerList->nextCombiner = iCombinerList;
			pCombinerList = iCombinerList;
			i++;
		}
		
		i=1;
		scanf("%d",&Number_of_Destroyers);
		DestroyerList *pDestroyerList;
		DestroyerList *iDestroyerList;

		while(i<=Number_of_Destroyers)
		{
			char Destroyer_string[3];

			scanf("%s",Destroyer_string);

			iDestroyerList = new DestroyerList();
			iDestroyerList->Destroyer[0] = Destroyer_string[0];
			iDestroyerList->Destroyer[1] = Destroyer_string[1];
			iDestroyerList->Destroyer[2] = '\0';
			iDestroyerList->nextDestroyer = NULL;

			if(i == 1)
			{
				globalDestroyerList = iDestroyerList;

				pDestroyerList = iDestroyerList;
				i++;
				continue;
			}
			pDestroyerList->nextDestroyer = iDestroyerList;
			pDestroyerList = iDestroyerList;
			i++;
		}

		int number_of_test_Elements = 0;

		scanf("%d", &number_of_test_Elements);

		testElementString = new char[number_of_test_Elements+1];

		scanf("%s", testElementString);

		globalFinalElementsList = new FinalElementsList();
		globalFinalElementsList->Element[0] = testElementString[0];
		globalFinalElementsList->Element[1] = '\0';
		globalFinalElementsList->nextElement = NULL;

		last_element = new char[2];
		last_element[0] = testElementString[0];
		last_element[1] = '\0';

		int j = 1;
		
		current_element = new char[2];

		while(j < number_of_test_Elements)
		{
			
			current_element[0] = testElementString[j];
			current_element[1] = '\0';

			iCombinerList = globalCombinerList;
			bool IsCombined = false;
			while(iCombinerList != NULL && globalFinalElementsList != NULL)
			{
				
				if( (iCombinerList->Combiner[0] == current_element[0] && iCombinerList->Combiner[1] == last_element[0])||
					(iCombinerList->Combiner[1] == current_element[0] && iCombinerList->Combiner[0] == last_element[0]))
				{
					FinalElementsList *iFinalElementsList;
					iFinalElementsList = globalFinalElementsList;

					while(iFinalElementsList ->nextElement != NULL)	iFinalElementsList= iFinalElementsList->nextElement;
					
					iFinalElementsList->Element[0] = iCombinerList->Combiner[2];
					IsCombined = true;
					
					last_element[0] = iCombinerList->Combiner[2];
					
					break;
					
					
				}
				iCombinerList = iCombinerList->nextCombiner;

			}
			if(IsCombined == true)
			{
				j++; continue;
			}

			bool IsDestroyed = false;
			iDestroyerList = globalDestroyerList;

			while(iDestroyerList != NULL && globalFinalElementsList != NULL)
			{
				FinalElementsList *iFinalElementsList;
				iFinalElementsList = globalFinalElementsList;

				while(iFinalElementsList != NULL)
				{
					if((iDestroyerList->Destroyer[0] == current_element[0] && iDestroyerList->Destroyer[1] == iFinalElementsList->Element[0]) ||
						(iDestroyerList->Destroyer[1] == current_element[0] && iDestroyerList->Destroyer[0] == iFinalElementsList->Element[0]))
					{
						FinalElementsList *jFinalElementsList;
						FinalElementsList *pFinalElementsList;
						jFinalElementsList = globalFinalElementsList;
						pFinalElementsList = jFinalElementsList;

						while(globalFinalElementsList->nextElement != NULL)
						{
							jFinalElementsList = globalFinalElementsList;
							pFinalElementsList = jFinalElementsList;
							while(jFinalElementsList->nextElement != NULL)
							{
								pFinalElementsList = jFinalElementsList;
								jFinalElementsList = jFinalElementsList->nextElement;
							}
							delete jFinalElementsList;
							if(pFinalElementsList != NULL) pFinalElementsList->nextElement = NULL;
						}
						delete globalFinalElementsList;
						globalFinalElementsList = NULL;
						IsDestroyed = true;
						break;
					}
					iFinalElementsList = iFinalElementsList->nextElement;
				}
				iDestroyerList = iDestroyerList->nextDestroyer;
			}
			
			if(IsDestroyed == true)
			{
				j++;
				continue;
			}

			if(globalFinalElementsList == NULL)
			{
				globalFinalElementsList = new FinalElementsList();
				globalFinalElementsList->Element[0] = testElementString[j];
				globalFinalElementsList->Element[1] = '\0';
				globalFinalElementsList->nextElement = NULL;

				last_element[0] = testElementString[j];
			}
			else
			{
				FinalElementsList *iglobalFinalElementsList;
				iglobalFinalElementsList = globalFinalElementsList;

				while(iglobalFinalElementsList->nextElement != NULL)	iglobalFinalElementsList = iglobalFinalElementsList->nextElement;

				iglobalFinalElementsList->nextElement = new FinalElementsList();
				iglobalFinalElementsList->nextElement->Element[0] = testElementString[j];
				iglobalFinalElementsList->nextElement->Element[1] = '\0';
				iglobalFinalElementsList->nextElement->nextElement = NULL;

				last_element[0] = testElementString[j];
			}

			j++;
		}

		printf("Case #%d: [",l);

		FinalElementsList *iglobalFinalElementsList;
		iglobalFinalElementsList = globalFinalElementsList;

		if(iglobalFinalElementsList != NULL)
		{	
			printf("%s",iglobalFinalElementsList->Element);
		
			iglobalFinalElementsList=iglobalFinalElementsList->nextElement;
		}

		while(iglobalFinalElementsList != NULL)
		{
			printf(", %s",iglobalFinalElementsList->Element);
			iglobalFinalElementsList=iglobalFinalElementsList->nextElement;
		}

		printf("]\n");
		l++;

		//free space for Linked List

		if(globalCombinerList != NULL)
		{
			while(globalCombinerList->nextCombiner != NULL)
			{
				iCombinerList = globalCombinerList;
				pCombinerList = iCombinerList;
				while(iCombinerList->nextCombiner != NULL)
				{
					pCombinerList = iCombinerList;
					iCombinerList = iCombinerList->nextCombiner;
				}
				delete iCombinerList;
				if(pCombinerList != NULL) pCombinerList->nextCombiner = NULL;
			}
			delete globalCombinerList;
		}
		globalCombinerList = NULL;

		if(globalDestroyerList != NULL)
		{
			while(globalDestroyerList->nextDestroyer != NULL)
			{
				iDestroyerList = globalDestroyerList;
				pDestroyerList = iDestroyerList;
				while(iDestroyerList->nextDestroyer != NULL)
				{
					pDestroyerList = iDestroyerList;
					iDestroyerList = iDestroyerList->nextDestroyer;
				}
				delete iDestroyerList;
				if(pDestroyerList != NULL) pDestroyerList->nextDestroyer = NULL;
			}
			delete globalDestroyerList;
		}
		globalDestroyerList = NULL;

		FinalElementsList *pglobalFinalElementsList;
		if(globalFinalElementsList != NULL)
		{
			while(globalFinalElementsList->nextElement != NULL)
			{
				iglobalFinalElementsList = globalFinalElementsList;
				pglobalFinalElementsList = iglobalFinalElementsList;
				while(iglobalFinalElementsList->nextElement != NULL)
				{
					pglobalFinalElementsList = iglobalFinalElementsList;
					iglobalFinalElementsList = iglobalFinalElementsList->nextElement;
				}
				delete iglobalFinalElementsList;
				if(pglobalFinalElementsList != NULL) pglobalFinalElementsList->nextElement = NULL;
			}

			delete globalFinalElementsList;
		}
		globalFinalElementsList = NULL;

		delete testElementString;
		delete last_element;
		delete current_element;
	}

	return 0;
}

