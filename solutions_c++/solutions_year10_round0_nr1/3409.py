#include <iostream>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <string>
#include "math.h"

using namespace std;

int main(){
    /*all we care about is having the same outputs for the same inputs so say we have 4 snappers 0000 , 1000, 0100, 1100, 0010, 1010, 0110, 1110, 0001, 1001, 0101, 1101, 0011, 1011, 0111, 1111 ON!  ... 
    so we have binary counting where all the bits need to be on to give power to the light. We have n bits to match n snappers and a pattern will repeat on the cycle every 2^n snaps.
    */
    
    int k = 0; int n = 0;int c = 0;
    string line = "";
    size_t p;
    string t = "";
    ifstream test ("A-large.in");
    ofstream output ("output.txt");
    cout << "Input" << setw(10) << "Output" << endl;
    if(test.is_open() && output.is_open()){
                       while(!test.eof() && c <= 10000){
                                         getline(test, line);
                                         p = line.find(" ");
                                         t = line.substr(0, p);
                                         istringstream buff(t);
                                         buff >> n;
                                         t = line.substr(p+1);
                                         istringstream buff2(t);
                                         buff2 >> k;
                                         if(c>0){
                                         int temp = pow(2,n);
                                         if ((k % temp) == temp-1){cout << n << " " << k << " " << "Case #" << c << ": ON" << endl; output << "Case #" << c << ": ON" << endl;}
                                         else {cout << n << " " << k << " " << "Case #" << c << ": OFF" << endl;  output << "Case #" << c << ": OFF" << endl;}
                                         }
                                         c++;
                                         }
                       output.close();
                       test.close();
    }
    else { cout << "stupid input file";}
    cin.get();
}
