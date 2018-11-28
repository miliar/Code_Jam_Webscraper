#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<conio.h>
using namespace std;

typedef long long int64;
ifstream freader("C-small.in");
ofstream fwriter("C-small.out");

void eval(string to_match,string given, int match_index, int given_index, int64& counter)
{
     if (match_index == to_match.length())
     {
       counter++;
       //cout << counter << endl;
       return;
     }
     for (int i = given_index; i < given.length(); i++)
     {
         if (to_match[match_index] == given[i])
         {
            eval(to_match,given,match_index+1,i+1,counter);                          
         }
     }
}

vector<int>* windex = new vector<int>[19];

void fill_vector(string text)
{
     string temp = "welcome to code jam";
     for (int i = 0; i < 19; i++)
     {
         for (int j = 0; j < text.length(); j++)
         {
             if (temp[i] ==  text[j]) windex[i].push_back(j);  
         }
     }
}

int main()
{
    int N;
    freader >> N;
    string line;
    int64 counter;
    getline(freader,line);
    for(int i = 0; i < N; i++)
    {
            for (int j = 0; j < 19; j++) windex[j].clear();
            getline(freader,line);
            //cout << line << endl;
            counter = 0;
//            fill_vector(line);
//            for (int j = 0; j < 19; j++)
//            {
//                for (int k = 0; k < windex[j].size(); k++)
//                {
//                    cout << windex[j][k] << " ";    
//                }
//                cout << endl << endl;    
//            }
            eval("welcome to code jam",line,0,0,counter);
            fwriter << "Case #" << i + 1 << ": ";
            int num = counter % 10000;
            if (num < 10) fwriter << "0";
            if (num < 100) fwriter << "0";
            if (num < 1000) fwriter << "0";
            fwriter << num <<endl;
    }
    //getch();
    freader.close();
    fwriter.close();
    return 0;   
}
