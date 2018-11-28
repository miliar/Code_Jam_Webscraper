// GjamCpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <string>
#include <iostream>
#include "ButtonEventList.h"



int main()
{
	int i,j,k;
	//printf("Hello world!\n");

	int Number_of_TestCases=0;
	int Number_of_Buttons_to_be_pressed=0;
	scanf("%d",&Number_of_TestCases);
	int l=1;
	i=1;
	

	while(l<=Number_of_TestCases)
	{
		i=1;
		scanf("%d",&Number_of_Buttons_to_be_pressed);
		int number_of_moves =0;
		ButtonEventList *CurentTestCaseEventstemp;
		ButtonEventList *CurentTestCaseEvents;
		ButtonEventList *GlobalTestCaseEvents;
		while(i<=Number_of_Buttons_to_be_pressed)
		{
			char rc[2];
			int p;

			scanf("%s %d",&rc,&p);

			//printf("%s %d",rc,p);
			
				CurentTestCaseEvents = new ButtonEventList();
				CurentTestCaseEvents->eventNUmber = i;
				CurentTestCaseEvents->eventPos = p;
				CurentTestCaseEvents->roboColor[0] = rc[0];
				CurentTestCaseEvents->roboColor[1] = '\0';
				CurentTestCaseEvents->nextEvent = NULL;
				

			if(i==1)
			{
				CurentTestCaseEventstemp = CurentTestCaseEvents;
				GlobalTestCaseEvents = CurentTestCaseEventstemp;
			}
			else
			{
				CurentTestCaseEventstemp ->nextEvent = CurentTestCaseEvents;
				CurentTestCaseEventstemp = CurentTestCaseEvents;
			}

			fflush(stdout);
			i++;
		}// Linked List Construction End;

		int cur_event = 0;
		int O_cur_pos = 1;
		int O_next_pos = 0;
		int B_cur_pos = 1;
		int B_next_pos = 0;
		int num_of_seconds = 0;
		
		bool Os_nextpos_found = false;
		bool Bs_nextpos_found = false;

		/* Find Os / Bs Next Position */
			
		CurentTestCaseEventstemp = GlobalTestCaseEvents;
		while(CurentTestCaseEventstemp != NULL)
		{
			if(CurentTestCaseEventstemp->roboColor[0] == 'O' && CurentTestCaseEventstemp->eventNUmber > cur_event && Os_nextpos_found == false)
			{
				O_next_pos = CurentTestCaseEventstemp->eventPos;
				Os_nextpos_found = true;
			}
			else if (CurentTestCaseEventstemp->roboColor[0] == 'B' && CurentTestCaseEventstemp->eventNUmber > cur_event && Bs_nextpos_found == false)
			{
				B_next_pos = CurentTestCaseEventstemp->eventPos;
				Bs_nextpos_found = true;
			}
			else
				CurentTestCaseEventstemp = CurentTestCaseEventstemp->nextEvent;
			if(Os_nextpos_found == true && Bs_nextpos_found == true)	break;
		}

		while(cur_event <= Number_of_Buttons_to_be_pressed)
		{
			
			if(cur_event == 0)
			{
				CurentTestCaseEventstemp = GlobalTestCaseEvents;
				cur_event++;
			}

			bool isEventComplete = false;
			
			while(isEventComplete == false)
			{
				bool IsOMoved = false;
				bool IsBMoved = false;
				if(O_cur_pos < O_next_pos){	O_cur_pos++; IsOMoved= true;}
				else if(O_cur_pos > O_next_pos) { O_cur_pos--; IsOMoved = true;}
					
				if(B_cur_pos < B_next_pos) {B_cur_pos++; IsBMoved = true;}
				else if(B_cur_pos > B_next_pos)	{B_cur_pos--; IsBMoved = true;}

				switch(CurentTestCaseEventstemp->roboColor[0])
				{
					case 'O' : 
						if(IsOMoved == true) {break;}
						if(O_cur_pos == O_next_pos)	
						{
								isEventComplete = true;
								ButtonEventList *CurentTestCaseEvents;
								CurentTestCaseEvents = CurentTestCaseEventstemp->nextEvent;
								Os_nextpos_found = false;
								while(CurentTestCaseEvents != NULL)
								{
									if(CurentTestCaseEvents->roboColor[0] == 'O' && CurentTestCaseEvents->eventNUmber > cur_event)
									{
										O_next_pos = CurentTestCaseEvents->eventPos;
										Os_nextpos_found = true;
										break;
									}
									CurentTestCaseEvents = CurentTestCaseEvents->nextEvent;
								}
						}
						break;
					case 'B' :
						if(IsBMoved == true) {break;}
						if(B_cur_pos == B_next_pos)	
						{
								isEventComplete = true;
								ButtonEventList *CurentTestCaseEvents;
								CurentTestCaseEvents = CurentTestCaseEventstemp->nextEvent;
								Bs_nextpos_found = false;
								while(CurentTestCaseEvents != NULL)
								{
									if(CurentTestCaseEvents->roboColor[0] == 'B' && CurentTestCaseEvents->eventNUmber > cur_event)
									{
										B_next_pos = CurentTestCaseEvents->eventPos;
										Bs_nextpos_found = true;
										break;
									}
									CurentTestCaseEvents = CurentTestCaseEvents->nextEvent;
								}

						}

						break;
				}
				num_of_seconds++;
			}
			CurentTestCaseEventstemp = CurentTestCaseEventstemp->nextEvent;
			cur_event ++;
		}

		printf("Case #%d: %d\n",l,num_of_seconds);
		l++;

		//free space for Linked List

		ButtonEventList *iTestCase;
		ButtonEventList *pTestCase;

		while(GlobalTestCaseEvents->nextEvent != NULL)
		{
			iTestCase = GlobalTestCaseEvents;
			pTestCase = iTestCase;
			while(iTestCase->nextEvent != NULL)
			{
				pTestCase = iTestCase;
				iTestCase = iTestCase->nextEvent;
			}
			delete iTestCase;
			if(pTestCase != NULL) pTestCase ->nextEvent= NULL;
			//pTestCase = NULL;
		}
		delete GlobalTestCaseEvents;
	}

	return 0;
}

