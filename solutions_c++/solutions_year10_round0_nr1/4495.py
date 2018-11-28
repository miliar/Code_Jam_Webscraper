#include <iostream>
#include <fstream>
using namespace std;

int main(char* args[], int n) {
    
   ifstream entrada ("small.in", ios::in);
   ofstream salida ("salida.out", ios::out);
   
   int totalCasos = 0;
   
   entrada >> totalCasos;
   
   
   for (int i = 0; i < totalCasos; i++) {
       
       if(i != 0) salida << endl;
       
       int totalSnappers = 0;
       int  totalClicks = 0;
       entrada >> totalSnappers >> totalClicks;
       
       int * snappers = new int[totalSnappers];
       
       for (int j = 0; j < totalSnappers; j++) {
       
           snappers[j] = 0;    
       }
       
       for (int k = 0; k < totalClicks; k++) {
           
           bool power = true;
          int r = 0; 
          while(power && (r < totalSnappers)) 
          {
                 if(snappers[r] == 0) {
                    power = false;
                    snappers[r] = 1;
                 }else snappers[r] = 0;
                 
                 r++;
                 
                 
                                    
          }  
       }
       
       bool luz = true;
       
       for(int p = 0; p < totalSnappers; p++) {
       
               luz = (snappers[p] == 1) && luz; 
       }
       
       if(luz) salida << "Case #" << (i+1) <<": ON";
       else salida << "Case #" << (i+1) <<": OFF";
       
       //delete [] snappers;
   }
    
}
