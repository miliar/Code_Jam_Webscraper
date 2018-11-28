/***************************************************************************
 *   Copyright (C) 2008 by Pedro Alfredo Linares Kcomt   *
 *   palk1987@hotmail.com   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/


#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <cstdlib>
#include <map>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

struct Case
{
	map<string, int> searchEngines;
	int numEngines;
	vector<string> vQueries;
	int numSwitches;
};



void fillEnginesToMinus1(map<string, int>* mapEngines)
{
	map<string,int>::iterator iter;
	for( iter= mapEngines->begin(); iter != mapEngines->end(); iter++ ) {
			iter->second=-1;
	}
	
}

vector<string>* eraseNoEngines(map<string, int>* mapEngines, int numEngines, vector<string>* vQueries)
{
	vector<string>* vOnlyEngines=new vector<string>();
	
	for(int i=0; i<vQueries->size(); i++)
	{
		map<string,int>::iterator iter = mapEngines->find( (*vQueries)[i] );
		if(iter!= mapEngines->end())//the key exists
		{
			vOnlyEngines->push_back((*vQueries)[i]);			
		}
	}
	return vOnlyEngines;		
}


void writeSolution(const char* file, vector<Case*>* vCases)
{
	ofstream out;
    
	out.open(file);
	if(out.bad()) return;

	for(int i=0; i<(*vCases).size(); i++)      
	{
		out<<"Case #"<<i+1<<": "<<(*vCases)[i]->numSwitches<<"\n";
	}
    
	out.flush();
	out.close();
}

vector<Case*>* readFile(const char* file)
{   
	ifstream in;
	
	//variables to read
	int numCases=0;
	int numSearchEngines=0;
	int numQueries=0;	
	
	in.open(file);
	if (in.bad()) return NULL;  
	
	char curLine[1024];	 
	in.getline(curLine, 1024, '\n');    
	numCases=atoi(curLine);
	
	vector<Case*>* vCases=new vector<Case*>();
	
	int i=0; char* car;
	while(!in.eof() && i<numCases)
	{ 
		Case* c=new Case();
		
		//in>>curLine;      
		in.getline(curLine, 1024, '\n');
		//for(car=curLine; isspace(*car); car++); //eliminamos espacios tabs retornos de carro      		
		numSearchEngines=atoi(curLine);
		
		
		int j=0;
		while(!in.eof() && j<numSearchEngines)
		{
			in.getline(curLine, 1024, '\n');
			string s(curLine);
			c->searchEngines[s]=-1;
			j++;
		}
		
		//in>>curLine;      
		in.getline(curLine, 1024, '\n');
		//for(car=curLine; isspace(*car); car++);			
		numQueries=atoi(curLine);
		
		
		int k=0;
		while(!in.eof() && k<numQueries)
		{			
			in.getline(curLine, 1024, '\n');
			string s(curLine);
			c->vQueries.push_back(s);
			k++;
		}
		      
		c->numEngines=numSearchEngines;
		c->numSwitches=0;
		vCases->push_back(c);
		
		i++; 
	}
    
	in.close();   
	return vCases;
}


/**
* Get the solution for one case
*/
int getNumSwitches(Case* c)
{
	//Obtenemos la data necesaria
	vector<string>* queries=eraseNoEngines(&(c->searchEngines), c->numEngines, &(c->vQueries));
	int num=0;
	int index=0; int count=0;
	int size=queries->size();
	int numSE=c->numEngines;
	
	bool fin=false;
	
	while(!fin)
	{
		fillEnginesToMinus1(&(c->searchEngines));		
		count=0;
		
		while(count!=numSE && index<size)
		{
			if(c->searchEngines[ (*queries)[index] ]==-1)//not analysed yet
			{
				c->searchEngines[ (*queries)[index] ]=index;				
				count++;				
			}
			index++;
		}	
		
		if(count==numSE)
		{
			num++;
			index--;
		}
		
		if(index==size)
		{
			fin=true;
		}//finish			
	}
	
	c->numSwitches=num;
	return num;
}


int main(int argc, char *argv[])
{
	cout<<"Reading file...\n";
	vector<Case*>* cases=readFile("/opt/temp/google/A-large.in");
	
	cout<<"Processing...\n";
	for(int i=0; i<cases->size(); i++)
		getNumSwitches((*cases)[i]);
	
	cout<<"Writing solution...\n";
	writeSolution("/opt/temp/google/file2.txt", cases);
	
	cout<<"Done...\n";
  	return EXIT_SUCCESS;
}
