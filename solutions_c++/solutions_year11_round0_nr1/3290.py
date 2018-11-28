#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main () {
  ifstream inFile;
  inFile.open ("example.in");
 
  int test_cases, buttons_pressed, button, prev_button_b, prev_button_o;
  int total_time, travel_time, iter_time_o=0, iter_time_b=0;
  char robot, prev_robot;
  int a=0, b=0;
if (inFile.is_open()) {
  inFile >> test_cases;
  for (int i=1; i <= test_cases;++i) {
   inFile >> buttons_pressed;
   total_time=0;
   prev_button_o=1;
   prev_button_b=1;
   iter_time_o = 0, iter_time_b=0;
   for(int j=1; j<= buttons_pressed;++j){
     inFile >> robot >> button;

     if(j==1){
       prev_robot=robot;
     } 
     if(prev_robot != robot){
       if(robot == 'O'){
	 //cout << "iter b: " << iter_time_b << endl;
	 travel_time = abs(button-prev_button_o) - iter_time_b;
	 //cout << "travel:" << travel_time << endl;
	 if (travel_time < 0){
	   iter_time_o++;
	   //total_time++;
	 }
	 else{
	   iter_time_o = travel_time + 1;
	   total_time += travel_time; 
	 }
	 
	 prev_button_o=button;
	 iter_time_b=0;
       }
       else{
	 //cout << "iter o: " << iter_time_o << endl;	 
	 travel_time = abs(button-prev_button_b) - iter_time_o;
	 //cout << "travel:" << travel_time << endl;
	 if (travel_time < 0){
	   iter_time_b++;
	   //total_time++;
	 }
	 else{
	   iter_time_b = travel_time +1;
	   total_time += travel_time; 
	 }
	 prev_button_b=button;
	 iter_time_o=0;
       }
     }
     else{
       if(robot == 'O'){
	 iter_time_o += abs(button-prev_button_o)+1;
	 total_time+= abs(button-prev_button_o);
	 prev_button_o=button;
	 
       }
       else{
	 iter_time_b += abs(button-prev_button_b)+1; 
	 total_time += abs(button-prev_button_b); 
	 prev_button_b=button;
       }
     }
     prev_robot = robot;     
     total_time++;
     //cout << total_time << ", ";
  }
   //cout << endl << endl << endl;
   cout << "Case #"<<i<<": "<< total_time << endl;
 }
}



 inFile.close();

  return 0;
}
