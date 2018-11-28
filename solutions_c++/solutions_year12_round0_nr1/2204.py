#include <cstdlib>
#include <iostream>
#include<fstream.h>

using namespace std;

int main()
{
    char buf[110];
    int is;
    char let[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    ifstream infile("C:\\Users\\Flirt-PC\\Desktop\\test.txt");
    ofstream outf("C:\\Users\\Flirt-PC\\Desktop\\result.txt");
    //infile>>is;
   infile.getline(buf,110);
   int i=0;
    while(infile)
    {
         infile.getline(buf,110);
         int j=0;
         while(buf[j]!='\0')
         {
                            if(buf[j]==' ')
                            {}
                            else
                            {
                                buf[j]=let[int(buf[j])-97];
                            }
                            j++;
         }
           i++; 
         outf<<"Case #"<<i<<": "<<buf;
         outf<<"\n";
         
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
