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


#include <iostream>
#include <cstdlib>
#include <map>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

struct Time
{
	int horas;
	int minutos;
	
	Time()
	{
	}
	
	Time(int horas, int minutos)
	{
		this->horas=horas;
		this->minutos=minutos;
	}
	
	void sub(Time time)
	{
		horas=horas-time.horas;
		minutos=minutos-time.minutos;
		if(minutos<0)
		{
			minutos=minutos+60;					                                           	
			horas--;
		}
	}
	
	void add(Time time)
	{
		horas=horas+time.horas;
		minutos=minutos+time.minutos;					
		if(minutos>59)
		{
			minutos=minutos-60;
			horas++;
		}
	}
	
	int comparar(Time time)
	{
		if(horas>time.horas)
			return 1;
		if(horas<time.horas)
			return -1;
		if(minutos>time.minutos)
			return 1;
		if(minutos<time.minutos)
			return -1;
		return 0;
	}
	
	string toString()
	{
		char sx[10], sy[10];          
		sprintf(sx,"%d",horas);
		sprintf(sy,"%d",minutos);
		string cad="";
		cad=cad+sx+":"+sy;
		return cad;       
	}
	
	void copiar(Time time)
	{
		horas=time.horas;
		minutos=time.minutos;
	}
};

struct Case
{
	int numTrainsA;
	int numTrainsB;	
	int turnroundTime;
	vector<Time> timeTableADep;
	vector<Time> timeTableAArr;
	vector<Time> timeTableBDep;
	vector<Time> timeTableBArr;		
};

void split(char* cad, vector<char*>* vPalabras)
{
	int index=0, indexPal;
	int len=strlen(cad);
	while(index<len)
	{
		while(cad[index]==' ') index++;
			
		//separamos una palabra
		indexPal=0;	
		char* palabra=new char[255];
		while(index<len && cad[index]!=' ')
		{
			palabra[indexPal++]=cad[index++];	
		}
		palabra[indexPal]='\0';
		vPalabras->push_back(palabra);
		index++;		
	}		
}

void showTimeTable(vector<Time>* dep, vector<Time>* arr)
{
	for(int i=0; i<dep->size(); i++)
	{
		cout<<(*dep)[i].toString()<<" "<<(*arr)[i].toString()<<"\n";
	}		
}

void merge(vector<Time>* tDep, vector<Time>* tArr)
{
		int size=tDep->size();
		if(size<2)
			return;
	
		int mitad=size/2;
		vector<Time>* part1Dep=new vector<Time>();
		vector<Time>* part2Dep=new vector<Time>();
		
		vector<Time>* part1Arr=new vector<Time>();
		vector<Time>* part2Arr=new vector<Time>();
		
		for(int i=0; i<mitad; i++)
		{
			part1Dep->push_back( (*tDep)[i] );
			part1Arr->push_back( (*tArr)[i] );
		}
		
		for(int i=mitad; i<size; i++)
		{
			part2Dep->push_back((*tDep)[i]);
			part2Arr->push_back( (*tArr)[i] );
		}
		
		merge(part1Dep, part1Arr);
		merge(part2Dep, part2Arr);						
		
		tDep->clear(); tArr->clear();
		
		int index1=0, index2=0;
		int size1=part1Dep->size();
		int size2=part2Dep->size();
		
		while(index1<size1 && index2<size2)
		{
			int val=(*part1Dep)[index1].comparar( (*part2Dep)[index2]);
			if(val<0)
			{
				tDep->push_back( (*part1Dep)[index1]);
				tArr->push_back( (*part1Arr)[index1]);
				index1++;
			}
			else
			{
				tDep->push_back( (*part2Dep)[index2]);
				tArr->push_back( (*part2Arr)[index2]);
				index2++;
			}								
		}
		
		while(index1<size1)
		{
			tDep->push_back( (*part1Dep)[index1]);
			tArr->push_back( (*part1Arr)[index1]);
			index1++;
		}
		
		while(index2<size2)
		{
			tDep->push_back( (*part2Dep)[index2]);
			tArr->push_back( (*part2Arr)[index2]);
			index2++;
		}
				
		delete part1Dep;
		delete part2Dep;
		delete part1Arr;
		delete part2Arr;
}





void split(char* cad, vector<char*>* vPalabras, char car)
{
	int index=0, indexPal;
	int len=strlen(cad);
	while(index<len)
	{
		while(cad[index]==car) index++;
			
		//separamos una palabra
		indexPal=0;	
		char* palabra=new char[255];
		while(index<len && cad[index]!=car)
		{
			palabra[indexPal++]=cad[index++];	
		}
		palabra[indexPal]='\0';
		vPalabras->push_back(palabra);
		index++;		
	}		
}

void getTime(char* cad, Time* t)
{
	vector<char*>* vPalabras=new vector<char*>();
	split(cad, vPalabras, ':');	
		
	t->horas=atoi( (*vPalabras)[0]);
	t->minutos=atoi( (*vPalabras)[1]);
		
	for(int i=0; i<vPalabras->size(); i++)
		delete (*vPalabras)[i];		
	delete vPalabras;
}


void writeSolution(const char* file, vector<Case*>* vCases)
{
	ofstream out;
    
	out.open(file);
	if(out.bad()) return;

	for(int i=0; i<(*vCases).size(); i++)      
	{
		out<<"Case #"<<i+1<<": "<<(*vCases)[i]->numTrainsA<<" "<<(*vCases)[i]->numTrainsB<<"\n";
	}
    
	out.flush();
	out.close();
}

vector<Case*>* readFile(const char* file)
{
	ifstream in;
	
	//variables to read
	int numCases=0;
	int numA=0;
	int numB=0;	
	
	in.open(file);
	if (in.bad()) return NULL;  
	
	char curLine[1024];	 
	in.getline(curLine, 1024, '\n');    
	numCases=atoi(curLine);
	
	vector<Case*>* vCases=new vector<Case*>();
	
	int i=0; 
	while(!in.eof() && i<numCases)
	{ 
		Case* c=new Case();
		
		in.getline(curLine, 1024, '\n');		
		c->turnroundTime=atoi(curLine);	
			
		in.getline(curLine, 1024, '\n');//here its 2 numbers
				
		vector<char*>* vPalabras=new vector<char*>();
		split(curLine, vPalabras);
		numA=atoi( (*vPalabras)[0] );
		numB=atoi( (*vPalabras)[1] );
		
		for(int i=0; i<vPalabras->size(); i++)
			delete (*vPalabras)[i];		
		delete vPalabras;
		
		int j=0;
		while(!in.eof() && j<numA)
		{
			in.getline(curLine, 1024, '\n'); //aca hay 2 horas
			
			vPalabras=new vector<char*>();
			split(curLine, vPalabras);
			
			Time t, t2;
			getTime( (*vPalabras)[0], &t);
			c->timeTableADep.push_back(t);
			getTime( (*vPalabras)[1], &t2);
			c->timeTableAArr.push_back(t2);
			
			for(int i=0; i<vPalabras->size(); i++)
				delete (*vPalabras)[i];		
			delete vPalabras;
			
			j++;
		}
		
		
		int k=0;
		while(!in.eof() && k<numB)
		{			
			in.getline(curLine, 1024, '\n'); //aca hay 2 horas
			
			vPalabras=new vector<char*>();
			split(curLine, vPalabras);
			
			Time t, t2;
			getTime( (*vPalabras)[0], &t);
			c->timeTableBDep.push_back(t);
			getTime( (*vPalabras)[1], &t2);
			c->timeTableBArr.push_back(t2);
			
			for(int i=0; i<vPalabras->size(); i++)
				delete (*vPalabras)[i];		
			delete vPalabras;
			k++;
		}
		
		vCases->push_back(c);		
		i++; 
	}
    
	in.close();   
	return vCases;
}

void getResult(Case* c)
{	
	int numA, numB	;
	numA=0; numB=0;
		
	int indexA=0, indexB=0;
	
	vector<Time> vLlegadaHaciaA;	
	vector<Time> vLlegadaHaciaB;
	
	merge( &(c->timeTableADep), &(c->timeTableAArr));
	merge( &(c->timeTableBDep), &(c->timeTableBArr));
	
	/*cout<<"Horarios ordenados A:\n";
	showTimeTable( &(c->timeTableADep), &(c->timeTableAArr) );
	cout<<"\nHorarios ordenados B:\n";
	showTimeTable( &(c->timeTableBDep), &(c->timeTableBArr) );
	cout<<"\n";*/
	
	bool existe;
	while(indexA<c->timeTableADep.size() || indexB<c->timeTableBDep.size())
	{
		if( (indexB==c->timeTableBDep.size() || c->timeTableADep[indexA].comparar( c->timeTableBDep[indexB] ) <0) && indexA!=c->timeTableADep.size() ) // en A se parte primero
		{
			//buscamos disnponibles en los de llegada
			existe=false;
			for(int i=0; i<vLlegadaHaciaA.size(); i++)
				if(vLlegadaHaciaA[i].comparar(c->timeTableADep[indexA])<=0){
					existe=true;
					vLlegadaHaciaA.erase(vLlegadaHaciaA.begin()+i);
					break;
				}
			if(!existe)		
				numA++;
			
			Time tarr=c->timeTableAArr[indexA];
			tarr.add(Time(0, c->turnroundTime));			
			vLlegadaHaciaB.push_back(tarr);
			indexA++;
		}
		else // en b se parte primero
		{
			//buscamos disnponibles en los de llegada
			existe=false;
			for(int i=0; i<vLlegadaHaciaB.size(); i++)
				if(vLlegadaHaciaB[i].comparar(c->timeTableBDep[indexB])<=0){
				existe=true;
				vLlegadaHaciaB.erase(vLlegadaHaciaB.begin()+i);
				break;
				}
				if(!existe)		
					numB++;
			
				Time tarr=c->timeTableBArr[indexB];
				tarr.add(Time(0, c->turnroundTime));			
				vLlegadaHaciaA.push_back(tarr);
			    indexB++;
		}
	}
	
	c->numTrainsA=numA;
	c->numTrainsB=numB;
}

int main(int argc, char *argv[])
{
	cout<<"Reading file...\n";
	vector<Case*>* cases=readFile("/opt/temp/google/B-large.in");
	
	cout<<"Processing...\n";
	for(int i=0; i<cases->size(); i++)
		getResult((*cases)[i]);
	
	cout<<"Writing solution...\n";
	writeSolution("/opt/temp/google/train2.txt", cases);
	
	cout<<"Done...\n";
	return EXIT_SUCCESS;
}
