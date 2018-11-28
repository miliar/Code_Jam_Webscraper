#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;                   

int main()
{
    int cases, inputb, number, surprise, min, normaltotal, surprisetotal, j,yo;
    char inputa, output;
    ifstream inputfile;
    ofstream outputfile;
    inputfile.open("B-large.in");
    outputfile.open("B-large.out");
    inputfile >> cases;
   // cout<<cases<<"\n";
    inputa=inputfile.get();
    for(int i=0; i<cases; i++)
    {
            yo=0;
            outputfile<<"Case #"<<i+1<<": ";
     //       cout<<"Case #"<<i+1<<": \n";
            inputfile>>number;
            inputa=inputfile.get();
       //     cout<<number<<" ";
            inputfile>>surprise;
         //   cout<<surprise<<" ";
            inputa=inputfile.get();
            inputfile>>min;
           // cout<<minimum<<" ";
            inputa=inputfile.get();
            if(min>=1)
            normaltotal=min+(2*(min-1));
            else
            normaltotal=min;
            if(min>=2)
            surprisetotal=min+(2*(min-2));
            else
            surprisetotal=min;
         //   cout<<"\nNormal Total:"<<normaltotal<<"\nSurprise Total:"<<surprisetotal<<"\n";
            for(j=0; j<number; j++)
            {
                     inputfile>>inputb;
                     inputa=inputfile.get();
           //          cout<<inputb<<" ";
                     if(inputb>=normaltotal)
                     yo++;
                     else if(inputb>=surprisetotal && surprise>0)
                     {
                     yo++;
                     surprise--;
                     }
            }
            outputfile<<yo<<"\n";
          //  cout<<"\n"<<yo<<"\n";
    }
    inputfile.close();
    outputfile.close();
    getch();
    return 0;
}
