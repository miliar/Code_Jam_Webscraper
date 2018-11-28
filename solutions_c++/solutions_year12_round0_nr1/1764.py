#include <iostream>
#include <fstream> 
#include <iomanip>
#include <string>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

void translate(string str) {
    char english[]="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char google[]="ynficwlbkuomxsevzpdrjgthaq YNFICWLBKUOMXSEVZPDRJGTHAQ";
    int len= str.length();
    int k=0;
    int j=0;
    while(k<len){
        j=0;
        while(j<53){
        if(str[k]==google[j]){cout << english[j];break;}

//        if(str[k]==english[j]){cout << google[j];break;}
        j++;
        }
        k++;
    }
    

}

int main()
{
  vector<string> text_file;
  int i=0;
  ifstream ifs( "input.txt" );
  string temp;

  while( getline( ifs, temp ) ){
        if(i>0){
            cout << "Case #" << i <<": ";
            translate(temp);
            cout << "\n";
        }
        i++;
        }
     text_file.push_back( temp );
    
  
}