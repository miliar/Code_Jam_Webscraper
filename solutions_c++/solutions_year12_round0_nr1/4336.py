#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;    


int main()
{
    int cases;
    char c,nw,output,x,a;
    ifstream inputfile;
    ofstream outputfile;
    inputfile.open("A-small-attempt0.in");
    outputfile.open("A-small.out");
    inputfile >> cases;
    cout<<cases<<"\n";
    c=inputfile.get();
    for(int i=0; i<cases; i++)
    {
        //    blah=0;
            outputfile<<"Case #"<<i+1<<": ";
            cout<<"Case #"<<i+1<<": \n";
            
            
            //c=inputfile.get();
            do
            {
            x=inputfile.get();
            if(x==' ')
            {outputfile<<x;}
            else
            {int i;
char arr[52]={'e','o','j','u','p','r','m','l','y','a','s','n','l','g','c','e','k','i','d','s','x','m','v','p','n','b','r','t','i','d','b','h','t','w','a','y','h','x','w','f','f','c','o','k','u','j','g','v','z','q','q','z'};
      for(i=0;i<52;i=i+2)
      {
                       if(x==arr[i])
                       outputfile<<arr[i+1];
      }   
            
            }
            }while(x!='\n' && !inputfile.eof());
            outputfile<<"\n";
          //  cout<<"\n"<<blah<<"\n";
    }
    inputfile.close();
    outputfile.close();
    getch();
    return 0;
}
