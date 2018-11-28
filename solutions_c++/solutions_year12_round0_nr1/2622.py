#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <fstream>

using namespace std;


int main(int argc, char *argv[])
{
   const char SPACE[2] = " ";
   int N; //number of cases 
   char c;
   char c1;
   char output[120];
   int ii, jj, i1, j1; //iterators
   
   ifstream i_file1 ("inputs/A-small-attempt0.in");
  //ifstream i_file2 ("inputs/english.in");
   ofstream o_file ("outputs/english.out");
   
   i_file1 >> N; //reading number of cases
   c = i_file1.get();
   for(ii = 1; ii <= N; ii++) {
	 /*case input code*/
	 c  = 'x';
	 jj = 0;
	 output[0] = '\0';
	 while(true) {
       jj++;
	   c  = i_file1.get();
	   /*switch was obtained by diffing sample and reasoning for 'z'*/
	   switch(c) {
		case ' ':
		 strcat(output," ");
   		 break;
		case 'a':
		 strcat(output,"y");
   		 break;
		case 'b':
		 strcat(output,"h");
   		 break;
   	    case 'c':
		 strcat(output,"e");
   		 break;
   	    case 'd':
		 strcat(output,"s");
   		 break;
   	    case 'e':
		 strcat(output,"o");
   		 break;
   	    case 'f':
		 strcat(output,"c");
   		 break;
   	    case 'g':
		 strcat(output,"v");
   		 break;
   	    case 'h':
		 strcat(output,"x");
   		 break;
   	    case 'i':
		 strcat(output,"d");
   		 break;
   	    case 'j':
		 strcat(output,"u");
   		 break;
   	    case 'k':
		 strcat(output,"i");
   		 break;
   	    case 'l':
		 strcat(output,"g");
   		 break;
   	    case 'm':
		 strcat(output,"l");
   		 break;
   	    case 'n':
		 strcat(output,"b");
   		 break;
   	    case 'o':
		 strcat(output,"k");
   		 break;
   	    case 'p':
		 strcat(output,"r");
   		 break;
   	    case 'q':
		 strcat(output,"z");  
   		 break;
   	    case 'r':
		 strcat(output,"t");
   		 break;
   	    case 's':
		 strcat(output,"n");
   		 break;
   	    case 't':
		 strcat(output,"w");
   		 break;
   	    case 'u':
		 strcat(output,"j"); 
   		 break;
   	    case 'v':
		 strcat(output,"p");
   		 break;
   	    case 'w':
		 strcat(output,"f");
   		 break;
   	    case 'x':
		 strcat(output,"m");
   		 break;
   	    case 'y':
		 strcat(output,"a");
   		 break;
   	    case 'z':
		 strcat(output,"q"); 
   		 break;
	    //default:
       }
	   
	   if (c == '\n' or c == EOF){
		 break;
	   }
     }
     
	 /*case output code*/
	 //file output
	 o_file << "Case #" << ii << ": " << output << "\n";
	 //console output
	 cout << "Case #" << ii << ": " << output << "\n";
   }
   i_file1.close();
   //i_file2.close();
   o_file.close();

   cin.get();

	return 0;
}


