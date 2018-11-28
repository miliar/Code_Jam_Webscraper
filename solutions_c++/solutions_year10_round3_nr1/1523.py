#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
#include <fstream>


using namespace std;

class Point{  
  public:
    Point(int, int);
    int x;
    int y;
};

Point::Point(int x_, int y_){
  x = x_;
  y = y_;
};

bool intersection(Point* left[], Point* right[]) {
  Point p1 = *left[0];
  Point p2 = *left[1];
  Point p3 = *right[0];
  Point p4 = *right[1];
  
  float d = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x);
  
  if (d == 0) return false;
   
  float 
    pre = (p1.x*p2.y - p1.y*p2.x), 
    post = (p3.x*p4.y - p3.y*p4.x);
    
  float x = ( pre * (p3.x - p4.x) - (p1.x - p2.x) * post ) / d;
  float y = ( pre * (p3.y - p4.y) - (p1.y - p2.y) * post ) / d;
   
  if ( x < min(p1.x, p2.x) || x > max(p1.x, p2.x) || x < min(p3.x, p4.x) || x > max(p3.x, p4.x) ) 
    return false;
    
  if ( y < min(p1.y, p2.y) || y > max(p1.y, p2.y) || y < min(p3.y, p4.y) || y > max(p3.y, p4.y) )
    return false;
   
  return true;
} 

int count, switches;

int main() {
  string input_line;
  
  getline(cin, input_line);
  int cases=atoi(input_line.c_str());
  
  int c=0;
  while(c++ < cases) {
	  getline(cin, input_line);
    
    int intersections=0;
    
    int input_wires = atoi(input_line.c_str());
    int w=-1;
    
    Point* wires[input_wires][2];
    
    while(w++ < input_wires-1){
    
      getline(cin, input_line);
      
      string buf;
      stringstream ss(input_line);
	    
	    ss >> buf;
	    wires[w][0] = new Point(-1, atoi(buf.c_str()));
	    
	    ss >> buf;
	    wires[w][1] = new Point(1, atoi(buf.c_str()));
    }
	
    for(int i=0; i<input_wires; i++){
      for(int j=i; j<input_wires; j++){
        if(intersection(wires[i], wires[j])){
          intersections++;
        }
      }
    }
    
    printf("Case #%i: %i\n", c, intersections);
  }
}
