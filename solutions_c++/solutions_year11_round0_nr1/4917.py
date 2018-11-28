#include "StdAfx.h"



	void robot::NewCommand (int newTarget, bool newPriority )
	{
		this->target = newTarget;
		this->priority = newPriority;
		buttonPushed = false;
	}

	void robot::NewCommand (int newTarget )
	{
		this->target = newTarget;
		buttonPushed = false;
	}

	robot::robot(char color)
	{
		this->buttonPushed = false;
		this->color = color;
		this->position = 1;
		this->target = 1;
		this->priority = false;
		this->CurrentStep=-1;
	}

	void robot::refresh()
	{
		this->buttonPushed = false;
		this->position = 1;
		this->target = 1;
		this->priority = false;
		this->MySteps.clear();
		this->CurrentStep=-1;
	}

	robot::robot(char color, int position, int target, bool priority, bool buttonPushed)
	{
		this->buttonPushed = buttonPushed;
		this->color = color;
		this->position = position;
		this->target = target;
		this->priority = priority;
	}

	bool robot::Done()
	{

		if(MySteps.size() == 0)
		{
			//cout<<"I'm Done";
			return true;
		}

		
		if(CurrentStep >= lastStep && MySteps[lastStep].satisfied(*this, *this))
		{
			//cout<<"I'm Done";
			return true;
		}
		else
			return false;
	}

	bool robot::Move()
	{
		if(MySteps.size()==0)
			return true;

		if(CurrentStep==-1)
		{
			do{
				CurrentStep++;

				if(MySteps.find(CurrentStep)!=MySteps.end())
				{
					this->NewCommand(MySteps[CurrentStep].position);
					break;
				}

				
			}while(true);
		}

		if(MySteps[CurrentStep].satisfied(*this, *this) && !this->Done())
		{
			do{
				CurrentStep++;
				if(MySteps.find(CurrentStep)!=MySteps.end())
				{
					this->NewCommand(MySteps[CurrentStep].position);
					break;
				}
			}while(true);
		}

		if(target > position)
		{
//			cout<<"moves FWD +1";
			position ++;
		}
		else if(target < position) 
		{
//			cout<<"moves BWD -1";
			position --;
		}
		else if(target == position && priority)
		{
//			cout<<"press the button";
			buttonPushed = true;
/*
			// find next command
			do{
				CurrentStep++;
				if(MySteps.find(CurrentStep)!=MySteps.end())
				{
					this->NewCommand(MySteps[CurrentStep].position);
					break;
				}
				else if(this->Done())
					break;
					
			}while(true);
			*/
		}

		if(buttonPushed)
			return true;
	}
