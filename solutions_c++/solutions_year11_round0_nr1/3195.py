#include <iostream>
using namespace std;

int abs(int a) {
    if (a>0) return a;
    return -1*a;
}

int main() {
 int t;
 cin >> t;
 for (int i=0; i<t; i++) {
     int n;
     cin >> n;
     int orange = 1;
     int blue = 1;
     int suma,acumulat_orange,acumulat_blue;
     acumulat_blue = acumulat_orange = 0;
     
     char ra;
     int ca;
     cin >> ra >> ca;
     n--;
     if (ra == 'O') {
        suma = ca-orange + 1;        
        acumulat_orange = ca-orange + 1;
        orange = ca;     
     }
     else {
         suma = ca-blue + 1;         
         acumulat_blue = ca-blue + 1;
         blue = ca;
     }
     //cout << suma << endl;
     while (n--) {
           char r;
           int c;
           cin >> r >> c;
           if (r == 'O') {
              if (r == ra) {
                 suma+=abs(c-orange) + 1;
                 acumulat_orange+=abs(c-orange) + 1;
                 orange = c;
                 //cout << suma << endl;
              }
              else {
                   //cout << "acub: " << acumulat_blue << endl;               
                   suma += max(abs(c-orange)-acumulat_blue+1,1);
                   acumulat_orange+=max(abs(c-orange)-acumulat_blue+1,1);
                   orange = c;
                   acumulat_blue = 0;
                   //cout << suma << endl;
              }
              ra = 'O';     
           }
           else {
                if (r == ra) {
                    suma+=abs(c-blue) + 1;
                    acumulat_blue+=abs(c-blue) + 1;
                    blue = c;   
                    //cout << suma << endl;
                }
                else {
                     //cout << "acuo: " << acumulat_orange << endl; 
                     suma += max(abs(c-blue)-acumulat_orange+1,1);
                     acumulat_blue+=max(abs(c-blue)-acumulat_orange+1,1);
                     blue = c;                     
                     acumulat_orange = 0;
                     //cout << suma << endl;
                }
                ra = 'B';
           }      
     }
     cout << "Case #" << i+1 << ": " << suma << endl;    
 }  
}
