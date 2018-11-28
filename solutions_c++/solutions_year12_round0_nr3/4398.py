/******************************************************************************
Author: Jonathan Lam
Project Name: recycled num.cpp
Compiler: Dev C++
Due Date: 4/14/2012
******************************************************************************/
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <fstream>
#include <map>

using namespace std;

int getRec(int l, int u);

int main()
{        
    int counter = 1, lower = 0, upper = 0, max;
    ifstream file;
    ofstream ofile;
    
    file.open("C-small-attempt0.in");
    ofile.open("answer.in");    
    file>>max;
    
    while (counter <= max)
    {                  
          file>>lower>>upper;
          getRec(lower,upper);
                     
          cout<<"Case #"<<counter<<": "<<getRec(lower,upper)<<endl;            
          ofile<<"Case #"<<counter<<": "<<getRec(lower,upper)<<endl;              
          counter++;   
    }    
    file.close();
    ofile.close();
    system("pause");
    return 0;
}

int getRec(int l, int u)
{
    string s1 = "", s2 = "";
    map<int,int> tracker;
    int counter = 0, num;
    for (int x = l; x <= u; x++)
    {
        stringstream convert;
        convert << x;
        s1 = convert.str();
        tracker.clear();
        
        for (int size = 1; size < s1.size(); size++)
        {               
               s2 += s1.substr(s1.size()-size, size);
               s2 += s1.substr(0, s1.size()-size);
               
               stringstream convertBack(s2);
               convertBack >> num;
               convertBack.flush();               
               tracker[num]++;       //Keeps track of repeating numbers. ie 1212 -> 2121 twice
               
               if (num > x && num <= u && tracker[num] == 1)
                  counter++;
               s2 = "";
        }
     
         
    }
    //cout<<endl<<"count: "<<counter<<endl;
    return counter;
}







