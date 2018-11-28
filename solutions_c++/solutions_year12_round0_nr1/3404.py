#include <iostream>
#include <fstream>
#include <strstream>
using namespace std;
int main()
{
    ifstream inp;
    inp.open("A-small-attempt1.in");
    ofstream testfile;
    testfile.open ("example.txt");
    
    string t;
    getline(inp,t);
    int t2;
    if(t.length()==1) t2=t[0]-'0';
    else t2 = ((t[0]-'0')*10) + (t[1]-'0');
    for(int j=1;j<=t2;)
    {
                 string temp;
                 while( getline( inp, temp ) )
                 {
                        for(int i=0;i<temp.length();i++)
                        {
                                switch(temp[i])
                                {
                                               case 'a': temp[i]='y'; break;
                                               case 'b': temp[i]='h'; break;
                                               case 'c': temp[i]='e'; break;
                                               case 'd': temp[i]='s'; break;
                                               case 'e': temp[i]='o'; break;
                                               case 'f': temp[i]='c'; break;
                                               case 'g': temp[i]='v'; break;
                                               case 'h': temp[i]='x'; break;
                                               case 'i': temp[i]='d'; break;
                                               case 'j': temp[i]='u'; break;
                                               case 'k': temp[i]='i'; break;
                                               case 'l': temp[i]='g'; break;
                                               case 'm': temp[i]='l'; break;
                                               case 'n': temp[i]='b'; break;
                                               case 'o': temp[i]='k'; break;
                                               case 'p': temp[i]='r'; break;
                                               case 'q': temp[i]='z'; break;
                                               case 'r': temp[i]='t'; break;
                                               case 's': temp[i]='n'; break;
                                               case 't': temp[i]='w'; break;
                                               case 'u': temp[i]='j'; break;
                                               case 'v': temp[i]='p'; break;
                                               case 'w': temp[i]='f'; break;
                                               case 'x': temp[i]='m'; break;
                                               case 'y': temp[i]='a'; break;
                                               case 'z': temp[i]='q'; break;
                                }
                        }
                 testfile << "Case #"<<j++<<": "<<temp<<endl;
                 }
    }
    testfile.close();
   // system("pause");
	return 0;
}
