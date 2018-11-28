/***************************************************************************
 *   Copyright (C) 2008 by Boris Nikolai Konrad   *
 *   bkonrad@stud1   *
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

#include <stdio.h>
#include <stdlib.h>	
#include <math.h>
#include <iostream>
#include <string>

using namespace std;

FILE* file_s;
FILE* file_t; 


struct sample{
       int na_or_nb;     
       int train_dep;
       int train_arr;       
       int status;
} samples[200];
       

std::string sourcefile="source.txt";
std::string targetfile="target2.txt";



int intcmp(int a, int b)
{
    if (a==b) return 0;
    if (a<b) return -1;
    if (a>b) return 1;
}

int qs_struct(struct sample items[], int left, int right)
  {

    register int i, j;
    int x;
    struct sample temp;

    i = left; j = right;
    x = items[(left+right)/2].train_dep;

    do {
        
        
      while((intcmp(items[i].train_dep,x) < 0) && (i < right)) i++;
      while((intcmp(items[j].train_dep,x) > 0) && (j > left)) j--;
      
      if(i <= j) {
        temp = items[i];
        items[i] = items[j];
        items[j] = temp;
        i++; j--;
      }
    } while(i <= j);

    if(left < j) qs_struct(items, left, j);
    if(i < right) qs_struct(items, i, right);
    
    
  }

void quick_struct(struct sample items[], int count)
  {
    qs_struct(items,0,count-1);
  }








int main(int argc, char *argv[])
{
for  (int a=1;a<(argc);a++) 
  {
	// Eingabedatei
 	if ((string)argv[a-1]=="-s") {
		sourcefile=argv[a];	
		cout << "Folgende Datei wird versucht einzulesen: " << sourcefile << endl;
	}

	// Ausgabedatei
 	if ((string)argv[a-1]=="-t") {
		targetfile=argv[a];	
		cout << "Folgende Datei wird als Output benutzt: " << targetfile << endl;
	}
  }

cout << "Lese Datei." << endl;

  //Source-Datei öffnen
  if((file_s = fopen("source.txt","r")) == NULL)
  {
    fprintf(stderr,"Source-Datei konnte nicht geöffnet werden.\n");
    return 1;
  }

// Einlesen
char no_of_cases[3];
int noc;
fgets(no_of_cases,500,file_s);


string temp="";
for (int j=0;j<3;j++) temp += no_of_cases[j];	
noc = strtod(temp.c_str(),NULL);	
cout << noc << " Cases." << endl;

int t;
int na;
int nb;

int results_na[noc];                                                         
int results_nb[noc];


char intime[2];
char intrain[12];
char in_no[7];


int trains_a = 0;
int trains_b = 0;

//for (int i=0; i<100; i++) { natrain[i][0]=0; nbtrain[i][0]=0; natrain[i][1]=0; nbtrain[i][1]=0;}
int lastj=0;

for (int i=0; i<noc; i++)
{
   
	//cout << i << " i " << endl;

	fgets(intime,3,file_s);
	string temp="";
	for (int j=0;j<3;j++) temp += intime[j];	
	t = strtod(temp.c_str(),NULL);	

	fgets(intime,7,file_s);
	temp="";
	
	int k;
	for (int j=0;j<7;j++) 
	{
		if (!(intime[j] == ' '))
			{
			temp += intime[j];		
			}
		else
		{		
		k=j;
		break;
		}	
	}	

	na = strtod(temp.c_str(),NULL);


	temp="";
	for (int j=k;j<7;j++) 
	{
		if (!(intime[j] == ' '))
		temp += intime[j];
		else
		{
		k=j;
		continue;
		}	
	}
	nb = strtod(temp.c_str(),NULL);

	int tempsum = na + nb;
	lastj=0;


    for (int j=0; j<tempsum;j++) 
    {
        samples[j].train_dep=0;
        samples[j].train_arr=0;        
    }

	for (int j=0;j<tempsum;j++) 
	{
        
        
        if(j>=na) 
        {
         samples[j].na_or_nb = 1;
         }
        else samples[j].na_or_nb = 0;
        
        fgets(intrain,12,file_s);
		samples[j].train_dep += (intrain[0]-'0')*600;		
		samples[j].train_dep += (intrain[1]-'0')*60;
		samples[j].train_dep += (intrain[3]-'0')*10;
		samples[j].train_dep += (intrain[4]-'0');

		samples[j].train_arr += (intrain[6]-'0')*600;		
		samples[j].train_arr += (intrain[7]-'0')*60;
		samples[j].train_arr += (intrain[9]-'0')*10;
		samples[j].train_arr += (intrain[10]-'0');


		
	fgets(intrain,12,file_s);
	}
	
	
	cout << "na: " << na << " nb: " << nb << " t: " << t << endl;


    quick_struct(samples, tempsum);


            
  


    results_na[i]=0;   
	results_nb[i]=0;
    trains_a = 0;
    trains_b = 0;	
	
  cout << endl << endl;
  cout << "Zuege starten. i: " << i << endl;   
  	
	for (int k=0;k<tempsum;k++)
     {
             samples[k].status=0;
             samples[k].train_arr += t;
             cout <<  "Dep: " << samples[k].train_dep << "Arr: " << samples[k].train_arr << " NA/NB: " << samples[k].na_or_nb << endl;
     }
     

  
  for (int j=0;j<14400;j++) 
  {
     for (int k=0;k<tempsum;k++)
     {
         if (samples[k].train_dep==j)
         {
            if (samples[k].na_or_nb==0)
               {
               if (trains_a==0)
                  {
                    results_na[i]+=1;
                    samples[k].status=1;
                    cout << "Start Zug A, j: " << j << " k: " << k << " results_na " << results_na[i] <<endl;
                    }
                    
               if (trains_a>0)
                  {
                    trains_a-=1;
                    samples[k].status=1;
                    cout << "Zug A aus Depot, j: " << j << " k: " << k << " results_na " <<  results_na[i] << endl;
                    }     
               }      

            if (samples[k].na_or_nb==1)
               {
               if (trains_b==0)
                  {
                    results_nb[i]+=1;
                    cout << "Start Zug B, j: " << j << " k: " << k << " results_nb " <<  results_nb[i] << endl;
                    samples[k].status=1;
                    }
                    
               if (trains_b>0)
                  {
                    trains_b-=1;
                    samples[k].status=1;
                    cout << "Zug B aus Depot, j: " << j << " k: " << k << " results_nb " <<  results_nb[i] << endl;
                    }     
               }      
            }

     
         if (samples[k].train_arr==j)
         {
            if (samples[k].na_or_nb==0)
               {
                    samples[k].status=2;
                    trains_b+=1;       
                    cout << "Zug A erreicht B, j: " << j << " k: " << k << endl;                 
               }      

            if (samples[k].na_or_nb==1)
               {
                    samples[k].status=2;
                    trains_a+=1;    
                    cout << "Zug B erreicht A, j: " << j << " k: " << k << endl;
               }      
            }                         
     }
  }

    
    
}
  fclose(file_s);
  

  

//
  //File schreiben
  //

	//Datei 2 erstellen // öffnen
  	if((file_t = fopen(targetfile.c_str(),"w")) == NULL)
    {
    fprintf(stderr,"Output-Datei konnte nicht geöffnet werden.\n");
    return 1;
    }
  cout << "Schreibe Datei." << endl;
 
for (int i=0; i<noc; i++)
{
 fputs("Case #", file_t);

 char aktuell[3];
 sprintf(aktuell, "%d", i+1);
 
 fputs(aktuell,file_t);
 fputs(": ", file_t);
 
 char t_na[3];
 char t_nb[3];
sprintf(t_na, "%d", results_na[i]);
sprintf(t_nb, "%d", results_nb[i]);
 fputs(t_na,file_t);
 fputc(32, file_t);
 fputs(t_nb,file_t);
 
 fputc ( 13, file_t);
 fputc ( 10, file_t);
}

 fclose(file_t);
 
  int ttt;
  cin >> ttt;
  return EXIT_SUCCESS;
}
