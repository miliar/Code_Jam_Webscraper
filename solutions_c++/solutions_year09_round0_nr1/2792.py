// 
// Author:	G2 (Jit Ray Chowdhury)
//jit.ray.c@gmail.com
// Created on Sept 3, 2009
//For Google Code Jam 
//Qualification Round
//AlienLanguage

#include <stdlib.h>

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cmath>

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef vector<string> VS;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
//
// 
//
int main(int argc, char** argv) {
        ifstream fin("input.txt");
	ofstream fout("output.txt");

	int CN,L,l,D,d ,cn, S,match[5001][2],x,y,z,init;
	LL a,b,R;
        //VS patt;
        char word[500],patt[5001][16];
        string tmp;
	fin >>L>>D>> CN;
        for (d = 1; d <= D; ++d) {
            fin>>patt[d];
           // cout<<d<<patt[d]<<endl;
        }
	for (cn = 1; cn <= CN; ++cn) {

		fin>>word;
                //g2's_coode start
                for (d = 1; d <= D; ++d) {
                    match[d][0]=1;
                    match[d][1]=0;
                 }
		
                x=strlen(word);
                y=0;
                z=0;
                
                for(int i=0;i<x;i++)
                {
                    init=0;
                    if(word[i]=='(')
                    {   
                        y=1;//multi on
                        init=1;
                    }
                    else if(word[i]==')')
                    {   
                        y=0;//multi off
                       
                        for (d = 1; d <= D; ++d) 
                        {
                            //if(match[d][0]==1)
                                match[d][0]=match[d][1];
                                match[d][1]=0;
                            
                        }  
                        z++;
                    }
                    else 
                    {
                        
                        for (d = 1; d <= D; ++d) 
                        {
                            if(match[d][0]==1)
                            {
                                if(y==0)
                                    if(word[i]!=patt[d][z])
                                        match[d][0]=0;
                                if(y==1)
                                    if(word[i]==patt[d][z])
                                        match[d][1]=1;
                            }
                                
                           if(match[d][0]==1)R++;
                        }
                        
                        //cout<<word[i]<<"-"<<z;
                       
                        
                        if(y==0)z++;//nxt letter in pattern
                    }
                  //  R=0;
                   // for (d = 1; d <= D; ++d) 
                   // {
                   //     if(match[d][0]==1)R++;
                   // }
                    //cout<<" R"<<R;
                    
                }
                R=0;
                for (d = 1; d <= D; ++d) 
                    {
                        if(match[d][0]==1)R++;
                    }
                //cout <<word;
		//g2's_coode end		
		//debug output
		cout << "Case #" << cn << ": " <<R<< '\n';
		//final output
		fout << "Case #" << cn << ": " << R<< '\n';
	}
	//system("pause");
    return (EXIT_SUCCESS);
}

