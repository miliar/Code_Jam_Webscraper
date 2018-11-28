//*** Problem A 
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T,N;
char M[100][100];     
double WP[100], OWP[100], OOWP[100], NP[100];


int main()
{

string line;     
ifstream fin ("input.txt");
ofstream fout ("output.txt");

fin>>line; //No. of test cases
cout<<line;
T = atoi(line.c_str());
for (int i=0;i<T;i++)
{
  fin>>line; //No. of buttons to press
  N = atoi(line.c_str());
  
  
  for(int j=0; j<N ; j++) //row index
  { 
   for(int l=0; l<N ; l++) //column index
   {
     fin>>M[j][l];
     //cout<<" "<<M[j][l];//TODELETE      
   }       
  }     
  //WP CALC
  for(int j=0; j<N ; j++) //row index
  { 
   WP[j]=0; NP[j]=0;
   for(int l=0; l<N ; l++) //column index
   {         
     NP[j]+=M[j][l]=='.'?0:1;
     WP[j]+=M[j][l]=='1'?1:0;    
   }          
  }  
  
  //OWP CALC
  for(int j=0; j<N ; j++) //row index
  { 
   OWP[j]=0;       
   for(int l=0; l<N ; l++) //column index
   {
     OWP[j]+=M[j][l]!='.'?(M[j][l]=='1'?WP[l]/(NP[l]-1):(WP[l]-1)/(NP[l]-1)):0;           
   }
  }  
  
  //OOWP CALC
  for(int j=0; j<N ; j++) //row index
  { 
   OOWP[j]=0;       
   for(int l=0; l<N ; l++) //column index
   {
     OOWP[j]+=M[j][l]!='.'?OWP[l]/NP[l]:0;           
   }
  }
  
  
   fout<<"Case #"<<i+1<<":"<<endl;
   for(int j=0;j<N;j++)
   {      
   fout<<(0.25*WP[j]+0.5*OWP[j]+0.25*OOWP[j])/NP[j]<<endl;
   }
   //cout<<"SOLUTION: "<<s<<endl;
}

fin.close();
fout.close();

system("pause");

 }
