#include<iostream>
#include<math.h>
#include<fstream>
#include<string>
#include <cstdlib>
using namespace std;
int main (int argc, char* argv[]) 
{
   char alpha[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k',
   'r','z','t','n','w','j','p','f','m','a','q'};
   ifstream file;
   string lineBuffer;
   int count=1;
   file.open("A-small-attempt1.in");
   getline(file,lineBuffer);
   
   while (!file.eof()) 
   {
       getline(file, lineBuffer);
       if (lineBuffer.length() == 0)
           continue; //ignore all empty lines
       else 
       {
		   const char * in = lineBuffer.c_str();
		   int len=strlen(in),i;
		   char *out=(char*)malloc(sizeof(char));
		   for(i=0;i<len;i++)
		   {    if(in[i]==' ')
		   			out[i]=' ';
		   		else
		   		{
		   	    	int temp= in[i]-'a';
			   		out[i]=alpha[temp];
			   	}	
		   }
		   
		   ofstream myfile;
		   myfile.open ("output",ios::app);
		   myfile<<"Case #"<<count<<": ";
		   count++;
		   for(i=0;i<len;i++)
			   myfile<<out[i];
		   myfile<<endl;	 		   
		   myfile.close();
		   free(out);
       }
    }
	return 0;
}
