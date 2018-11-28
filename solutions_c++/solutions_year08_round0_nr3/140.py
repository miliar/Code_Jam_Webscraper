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
#include <math.h>

using namespace std;


struct Case
{
	double probability;
	double f;//fly's radius
	double R;//raquet's radius
	double t;//raquet's thickness
	double r;//string radius
	double g;//gap between string
	
};

struct Rectangle
{
	Rectangle()
	{  }
	
	Rectangle(double x1, double y1, double x2, double y2)
	{
		this->x1=x1;
		this->x2=x2;
		this->y1=y1;
		this->y2=y2;
	}
		
	
	double x1;
	double  x2;
	double  y1;
	double y2;
};


double PI=3.14159;

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

void writeSolution(const char* file, vector<Case*>* vCases)
{
	ofstream out;
    
	out.open(file);
	if(out.bad()) return;

	for(int i=0; i<(*vCases).size(); i++)      
	{
		char sx[24];          
		sprintf(sx,"%f", (*vCases)[i]->probability);
		out<<"Case #"<<i+1<<": "<<sx<<"\n";
	}
    
	out.flush();
	out.close();
}

vector<Case*>* readFile(const char* file)
{
	ifstream in;
	
	//variables to read
	int numCases=0;
		
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
					
		in.getline(curLine, 1024, '\n');//here its 2 numbers
				
		vector<char*>* vPalabras=new vector<char*>();
		split(curLine, vPalabras);
		
		c->f=atof( (*vPalabras)[0] );
		c->R=atof( (*vPalabras)[1] );
		c->t=atof( (*vPalabras)[2] );
		c->r=atof( (*vPalabras)[3] );
		c->g=atof( (*vPalabras)[4] );
				
		for(int i=0; i<vPalabras->size(); i++)
			delete (*vPalabras)[i];		
		delete vPalabras;
				
		vCases->push_back(c);		
		i++; 
	}
    
	in.close();   
	return vCases;
}


double getDistance(double x1, double y1, double x2, double y2)
{
	return  sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) );
}



double getAreaArco(double x1, double y1, double x2, double y2, double radius)
{
	double distance=getDistance(x1, y1, x2, y2);	
	
	//pitagoras
	double h=sqrt(radius*radius - (distance*distance)/4.0);
	
	double angle=acos( (radius*radius+radius*radius-distance*distance) /(2*radius*radius));
	
	double sector=(PI*radius*radius*angle)/(2*PI);
	
	return 	sector- h*distance/2;
	
}


bool isDentro(double radius, double x, double y)
{
	double res=x*x+y*y-radius*radius;
	if(res>0)
		return false;
	return true;
}

double getX(double radius, double y)
{
	return sqrt(radius*radius - y*y);	
}

double getY(double radius, double x)
{
	return sqrt(radius*radius - x*x);		
}

double getAreaTriangulo(double x1, double y1, double x2, double y2, double x3, double y3)
{			
	double a=getDistance(x1, y1, x2, y2);
	double b=getDistance(x1, y1, x3, y3);
	double c=getDistance(x3, y3, x2, y2);
	double p=(a+b+c)/2.0;
	
	return sqrt(p*(p-a)*(p-b)*(p-c));
}

double areaPuntosFuera(Rectangle rect, double radius)
{
	double x1c;
	double x2c;
	double y1c;
	double y2c;
	
	if(isDentro(radius, rect.x1, rect.y2))
	{
		x1c=getX(radius, rect.y2);
		y1c=rect.y2;	
	}
	else
	{
		x1c=rect.x1;
		y1c=getY(radius, rect.x1);	
	}
	
	if(isDentro(radius, rect.x2, rect.y1))
	{
		x2c=rect.x2;
		y2c=getY(radius, rect.x2);	
	}
	else
	{
		x2c=getX(radius, rect.y1);
		y2c=rect.y1;
	}
	
	double area=0;
	area=area+getAreaArco(x1c, y1c, x2c, y2c, radius);
	area=area+getAreaTriangulo(rect.x1, rect.y1, x1c, y1c, x2c, y2c);
	area=area+getAreaTriangulo(rect.x1, rect.y1, x1c, y1c, rect.x1, rect.y2);
	area=area+getAreaTriangulo(rect.x1, rect.y1, x2c, y2c, rect.x2, rect.y1);
	return area;
}


double getAreaRect(Rectangle rect)
{
	return (rect.x2-rect.x1)*(rect.y2-rect.y1);
}



//solo devuelve los rectangulos del primer cuadrante -> ^
vector<Rectangle>* getRectangles(Case* c)
{	
	double maxY=c->R-c->t-c->f;
	
	vector<double> vHorizontal;

	double grosor=c->r;
	double espacio=c->g;
	
	//horizontals
	double desde=grosor+c->f; double hasta=maxY;
	while(desde<hasta)
	{
		vHorizontal.push_back(desde);
		if(espacio> 2*c->f)			
			desde=desde+espacio-2*c->f;
		
		if(desde>hasta)
			vHorizontal.push_back(hasta);
		else
			vHorizontal.push_back(desde);	
		desde=desde+grosor*2+2*c->f;		
	}
	
	//ahora que ya tenemos las horizontales y verticales, sacamos los triangulos
	vector<Rectangle>* rect=new vector<Rectangle>();
	
	for(int i=0; i<vHorizontal.size(); i=i+2)
	{
		for(int j=0; j<vHorizontal.size(); j=j+2)
		{
			Rectangle r=Rectangle(vHorizontal[i], vHorizontal[j], vHorizontal[i+1], vHorizontal[j+1]);
			if(getAreaRect(r)!=0)
				rect->push_back(r);
		}
	}
		
	cout<<"Nro de rect="<<rect->size()<<"\n";
	return rect;
}

int hayPuntoFuera(Rectangle rect, double radius)
{
	bool b1=isDentro(radius, rect.x1, rect.y2);
	 bool b2=isDentro(radius, rect.x2, rect.y2);
	bool b3=isDentro(radius, rect.x2, rect.y1);
	bool b4=isDentro(radius, rect.x1, rect.y1);
	
	if(b1 && b2 && b3 && b4 )
		return 0;//dentro
	if(!b1 && !b2 && !b3 && !b4 )
		return 2;//fuera
	return 1; //algun punto fuera pero no todos	
}


void getResult(Case* c)
{		
	double totalArea	=(c->R)*(c->R)*PI;
	double availableArea=0;
	
	vector<Rectangle>* vRect=getRectangles(c);
	
	double radius=c->R-c->t-c->f;
	
	for(int i=0; i<vRect->size(); i++)
	{
		int val=hayPuntoFuera( (*vRect)[i] , radius);
		if(val==0)
			availableArea+=getAreaRect((*vRect)[i]);			
		else if(val==1)			
			availableArea+=areaPuntosFuera((*vRect)[i], radius);			
	}
	
	availableArea=availableArea*4;	
	
	c->probability=1-availableArea/totalArea;		
}


int main(int argc, char *argv[])
{
	cout<<"Reading file...\n";
	vector<Case*>* cases=readFile("/opt/temp/google/C-large.in");
	
	cout<<"Processing...\n";
	for(int i=0; i<cases->size(); i++)
		getResult((*cases)[i]);
	
	cout<<"Writing solution...\n";
	writeSolution("/opt/temp/google/final2.txt", cases);
	
	cout<<"Done...\n";
	
	
	cout<<getAreaTriangulo(1, 2, 2, 3, 2, 8);
	return EXIT_SUCCESS;
}
