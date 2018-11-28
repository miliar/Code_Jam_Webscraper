//============================================================================
// Name        : BotTrust.cpp
// Author      : Govs
// Version     :
// Copyright   : GPL
// Description : Hello World in C++, Ansi-style
//============================================================================

//#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int n_test,n_button,position,time,counto,countb,poso,posb;
	char color;
	ifstream file;
	ofstream results;
	file.open("A-large.in",ios::in);
	results.open("A-large.out",ios::out);
	file>>n_test;
	for(int i=0;i<n_test;i++)
	{
		file>>n_button;
		counto=0;
		countb=0;
		poso=1;
		posb=1;
		for(int j=0;j<n_button;j++)
		{
			file>>color;
			file>>position;
			if(j==0)
			{
				if(position>1)
			     time=position;
				else
					time=1;

				if(color=='O')
				{
					poso=position;
					counto=time;
				}

				if(color=='B')
				{
					posb=position;
					countb=time;
				}
			}
			else
			{
				if(color=='O')
				{
                    if(poso>position)
                    	if((time-counto)>(poso-position))
                    		time++;
                    	else
                    		time=(poso-position)+counto+1;

                    if(poso<position)
                    	if((time-counto)>(position-poso))
                    		time++;
                    	else
                    		time=(position-poso)+counto+1;
                    if(poso==position)
                    	time++;

					poso=position;
					counto=time;

				}
				if(color=='B')
				{
                    if(posb>position)
                    	if((time-countb)>(posb-position))
                    		time++;
                    	else
                    		time=(posb-position)+countb+1;
                    if(posb<position)
                    	if((time-countb)>(position-posb))
                    		time++;
                    	else
                    		time=(position-posb)+countb+1;

                    if(posb==position)
                    	time++;

					posb=position;
					countb=time;
				}
			  }
		}
		results<<"Case"<<" #"<<i+1<<": "<<time<<endl;
	}
	return 0;
}
