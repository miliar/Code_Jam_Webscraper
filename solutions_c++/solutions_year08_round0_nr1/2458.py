// CodeJam.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
   int i,nrocases, nrosearch, nroquery,aux,z;
   int menor;
   int encontrados;
   vector <string> SearchEngines;
   vector <string> Queries;
   vector <int> qtdQuerySearch;
   vector <bool> Encontrou;
   string line;
   int casenumber;
   ifstream myfile ("C:\\Nilson\\Google\\A-large.in");
   ofstream myfile2 ("C:\\Nilson\\Google\\A-large.out");
   getline(myfile,line);
   nrocases = atoi(line.c_str());
   casenumber = 0;
   while(casenumber<nrocases)
   {
	   SearchEngines.clear();
	   Queries.clear();
	   qtdQuerySearch.clear();
	   casenumber++;
	   getline(myfile,line);
	   nrosearch = atoi(line.c_str());
	   for(i=0;i<nrosearch;i++)
	   {
		  getline(myfile,line);
		  SearchEngines.push_back(line);
	   }
	   getline(myfile,line);
	   nroquery = atoi(line.c_str());
	   for(i=0;i<nroquery;i++)
	   {
		  getline(myfile,line);
		  if(Queries.size()>1)
		  {
		     if(Queries[Queries.size()-1] != line)
		        Queries.push_back(line);
		  }
		  else
		  {
             Queries.push_back(line);
		  }
	   }
	   for(i=0;i<SearchEngines.size();i++)
	   {
		  aux=0;
		  for(z=0;z<Queries.size();z++)
		  {
			 if(Queries[z] == SearchEngines[i])
				aux++;
		  }
		  qtdQuerySearch.push_back(aux);
	   }
	   menor = 0;
	   
       Encontrou.clear();
	   for(i=0;i<SearchEngines.size();i++)
		   Encontrou.push_back(false);
	   encontrados=0;
	   for(i=0;i<Queries.size();i++)
	   {
          for(z=0;z<SearchEngines.size();z++)
		  {
			  if(Queries[i]==SearchEngines[z])
			  {
				  if(Encontrou[z] == false)
				  {
					  Encontrou[z] = true;
					  encontrados++;
					  if(encontrados == SearchEngines.size())
					  {
						  menor++;
						  for(int m=0;m<SearchEngines.size();m++)
							  Encontrou[m]=false;
						  encontrados=1;
						  Encontrou[z] = true;
					  }
				  }
			  }
		  }
	   }
	   myfile2 << "Case #" << casenumber << ": " << menor << "\n";
   }
   myfile2.close();
   myfile.close();
   return 0;
}