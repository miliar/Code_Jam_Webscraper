#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    
    int T, Ti;
    fin >> T;

    string Nstr;
    int len;
    int Li;
    

    vector<char> digits;
    vector<char> sorteddig;
    vector<char> withoutz;
    vector<char> changechars;
    int zeroes;
    int zi;
    //vector<int> newdig;
    int dig;
    int i, index, lenc;
    string finalstr;
    char tempchar, nextchar, newfront;
    
    //string Nstr;
    for (Ti=0; Ti<T; Ti++)
    {
        digits.clear();
        sorteddig.clear();
        withoutz.clear();
        changechars.clear();
        finalstr = "";
        zeroes = 0;
        
        fin >> Nstr;
        len = Nstr.length();
        for (Li=0; Li<len; Li++)
        {
            digits.push_back(Nstr[Li]);
            sorteddig.push_back(Nstr[Li]);
            withoutz.push_back(Nstr[Li]);
        }
        
        
        sort(sorteddig.begin(), sorteddig.end());
        reverse(sorteddig.begin(), sorteddig.end());
        sort(withoutz.begin(), withoutz.end());
        reverse(withoutz.begin(), withoutz.end());
        
        while (withoutz.back()=='0')
        {
              withoutz.pop_back();
              zeroes++;
        }
        if (withoutz.size()==1)
        {
                finalstr += withoutz.back();
                for (zi = 0; zi < zeroes; zi++)
                {
                    finalstr += '0';
                }
                finalstr += '0';
        }
        else
        {
             tempchar = digits.back();
             changechars.push_back(tempchar);
             digits.pop_back();
             nextchar = digits.back();
             digits.pop_back();
             while (nextchar >= tempchar && !digits.empty())
             {
    
                   changechars.push_back(nextchar);
                   tempchar = nextchar;
                   nextchar = digits.back();
                   digits.pop_back();
    
             }
             if (nextchar >= tempchar && digits.empty())
             {
                                finalstr += withoutz.back();
                                withoutz.pop_back();
                                for (zi=0; zi<zeroes; zi++)
                                {
                                 finalstr += '0';
                                }   
                                finalstr += '0';
                                while (!withoutz.empty())
                                {
                                 finalstr += withoutz.back();
                                 withoutz.pop_back();
                                 }
             }
             else 
             {
                 changechars.push_back(nextchar);
                 sort(changechars.begin(), changechars.end());
                 lenc = changechars.size();
                 index = 0;
                 while (changechars[index] <= nextchar) index++;
                 newfront = changechars[index];
                 changechars.erase(changechars.begin()+index);
                 
                 //beginning is same
                 reverse(digits.begin(), digits.end());
                 while (!digits.empty())
                 {
                  finalstr += digits.back();
                  digits.pop_back();
                 }
                 
                 finalstr += newfront;
                 for (i=0; i<changechars.size(); i++)
                 {
                     finalstr += changechars[i];
                 }
             }
    }
        
        fout << "Case #" << (Ti+1) << ": " << finalstr << endl;
    }
    
    fin.close();
    fout.close();    
    
    return 0;
}
