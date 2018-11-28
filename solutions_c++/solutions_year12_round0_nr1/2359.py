//
//  main.cpp
//  GoogleCJ_1
//
//  Created by Michèle De Decker on 14/04/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main (int argc, const char * argv[])
{  
    //string alpha[26] = {"y","n","f","i","c","w","l","b","k","u","o","m","x","s","e","v","z","p","d","r","j","g","t","h","a","q"};
    ifstream input("input.txt");
    ofstream output("output.txt");
    int T = 0;
    input >> T;
    input.ignore();
    
    vector<string> G;
    
    for(int i = 0; i < T; i++)
    {
        G.push_back("");
        getline(input,G[i]);
        for(int j = 0; j < G[i].length(); j++)
        {
            switch (G[i][j])
            {
                    case 'y':
                    G[i].replace(j, 1, "a");
                    break;
                    
                    case 'n':
                    G[i].replace(j, 1, "b");
                    break;
                    
                    case 'f':
                    G[i].replace(j, 1, "c");
                    break;
                    
                    case 'i':
                    G[i].replace(j, 1, "d");
                    break;
                    
                    case 'c':
                    G[i].replace(j, 1, "e");
                    break;
                    
                    case 'w':
                    G[i].replace(j, 1, "f");
                    break;
                    
                    case 'l':
                    G[i].replace(j, 1, "g");
                    break;
                    
                    case 'b':
                    G[i].replace(j, 1, "h");
                    break;
                    
                    case 'k':
                    G[i].replace(j, 1, "i");   
                    break;
                    
                    case 'u':
                    G[i].replace(j, 1, "j");  
                    break;
                    
                    case 'o':
                    G[i].replace(j, 1, "k");    
                    break;
                    
                    case 'm':
                    G[i].replace(j, 1, "l");
                    break;
                    
                case 'x':
                    G[i].replace(j, 1, "m");
                    break;

                case 's':
                    G[i].replace(j, 1, "n");
                    break;

                case 'e':
                    G[i].replace(j, 1, "o");
                    break;

                case 'v':
                    G[i].replace(j, 1, "p");
                    break;

                case 'z':
                    G[i].replace(j, 1, "q");
                    break;

                case 'p':
                    G[i].replace(j, 1, "r");
                    break;

                case 'd':
                    G[i].replace(j, 1, "s");
                    break;

                case 'r':
                    G[i].replace(j, 1, "t");
                    break;

                case 'j':
                    G[i].replace(j, 1, "u");
                    break;

                case 'g':
                    G[i].replace(j, 1, "v");
                    break;

                case 't':
                    G[i].replace(j, 1, "w");
                    break;

                case 'h':
                    G[i].replace(j, 1, "x");
                    break;
                    
                case 'a':
                    G[i].replace(j, 1, "y");
                    break;

                case 'q':
                    G[i].replace(j, 1, "z");
                    break;
                    
                    default:
                    break;


            }
            
        }
        output << "Case #" << i+1 <<": " << G[i] << endl;
    }
   
    return 0;
}

