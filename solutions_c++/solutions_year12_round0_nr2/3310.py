#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char *argv[])
{
    
    ifstream file;
    ofstream write;
    write.open("output.txt");
    file.open("B-large.in");
    
    string numInput;
    getline(file,numInput);
    int num=1;
    while(!file.eof())
    {
         int n,s,p;
         int result=0;
         file>>n>>s>>p;
         for (int i=0;i<n;i++)
         {
             int t;
             file>>t;
             if (t<3)
             {
                 if (t==2)
                 {
                     if ( p<=1)
                        result++;
                     else if ((p==2) && (s!=0))
                     {
                          result++;
                          s--;
                     }
                 }
                 else if (t>=p)
                      result++;
             }
             else
             {
             if (t%3==0)
             {
                if(t/3>=p)
                   result=result+1;
                else if ((p-t/3 ==1) && (s!=0))
                {
                     result=result+1;
                     s--;
                }
             }
             else if ((t+1)%3==0)
             { 
                if((t+1)/3>=p)
                   result=result+1;
                else if ((p - (t+1)/3 == 1) && (s!=0))
                {    
                     result=result+1;
                     s--;
                }
             }
             else 
             {
                if ((t+2)/3>=p)
                   result=result+1;
             }
             }
         }
         write<<"Case #"<<num<<": "<<result<<endl;
         num++;
    }
    file.close();
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
