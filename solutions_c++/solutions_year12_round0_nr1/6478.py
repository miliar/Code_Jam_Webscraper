#include <iostream>
#include <fstream>

using namespace std;


int main(){
   int ncasos, i, cas=1;
   string cad;
   ifstream flujo;
   flujo.open("A-small.txt");
   flujo>> ncasos;
   
if(flujo.good()){ 
                
ofstream flujoGuardar;
flujoGuardar.open("output.txt");
   flujo.ignore();
   while(ncasos!=0)
   {      
      getline(flujo,cad);     
  
       for(i=0;i<cad.size(); i++)
    {
      if(cad[i]== 'a')      
       cad[i]= 'y'; 
     else{
      if(cad[i]== 'b')      
       cad[i]= 'h';  
      else{
     if(cad[i]== 'c')      
       cad[i]= 'e'; 
       else{
      if(cad[i]== 'd')      
       cad[i]= 's';  
       else{
       if(cad[i]== 'e')      
       cad[i]= 'o'; 
       else{
       if(cad[i]== 'f')      
       cad[i]= 'c'; 
       else{
       if(cad[i]== 'g')      
       cad[i]= 'v'; 
        else{
       if(cad[i]== 'h')      
       cad[i]= 'x'; 
        else{
       if(cad[i]== 'i')      
       cad[i]= 'd'; 
        else{
       if(cad[i]== 'j')      
       cad[i]= 'u'; 
        else{
       if(cad[i]== 'k')      
       cad[i]= 'i'; 
        else{
       if(cad[i]== 'l')      
       cad[i]= 'g'; 
        else{
       if(cad[i]== 'm')      
       cad[i]= 'l'; 
        else{
       if(cad[i]== 'n')      
       cad[i]= 'b'; 
       else{ 
       if(cad[i]== 'o')      
       cad[i]= 'k'; 
       else{ 
       if(cad[i]== 'p')      
       cad[i]= 'r'; 
       else{ 
       if(cad[i]== 'q')      
       cad[i]= 'z'; 
       else{ 
       if(cad[i]== 'r')      
       cad[i]= 't'; 
       else{ 
       if(cad[i]== 's')      
       cad[i]= 'n'; 
       else{
       
      if(cad[i]== 't')      
       cad[i]= 'w'; 
       else{ 
       if(cad[i]== 'u')      
       cad[i]= 'j'; 
        else{
       if(cad[i]== 'v')      
       cad[i]= 'p'; 
       else{ 
       if(cad[i]== 'w')      
       cad[i]= 'f'; 
        else{
       if(cad[i]== 'x')      
       cad[i]= 'm'; 
        else{
       if(cad[i]== 'y')      
       cad[i]= 'a'; 
        else{
       if(cad[i]== 'z')      
       cad[i]= 'q'; 
       } } } } } } } }  } } } } } } } } } } } } } } } } }
    } 
      
     if(flujoGuardar.good())
     flujoGuardar<<"Case #"<<cas<<": "<<cad<< endl; 
     
     cas++;             
     ncasos--;   
   }    
}
return 0;
}
