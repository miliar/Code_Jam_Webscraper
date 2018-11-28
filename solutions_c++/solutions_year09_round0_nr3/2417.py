#include <cstdlib>
#include <iostream>
#include <ios>
#include <fstream>
#include <string>

using namespace std;

int find(string match,string subject)
{
    //cout<<subject<<endl;
    if (match.length() == 0) return 1;
    
    int str_pos =subject.find(match[0]);
    //cout<<"\t"<<str_pos<<endl;
    int counter = 0;
    while(str_pos<subject.length() && str_pos > -1)
        {
         counter += find(match.substr(1), subject.substr(str_pos+1));
         str_pos = subject.find(match[0],str_pos+1);
                  }
    //cout<<"\treturn with:"<<counter<<endl;
   // system("PAUSE");
    return counter;
}


int main(int argc, char *argv[])
{
    
//file
    // Datei öffnen
    ifstream in_file("C-small-attempt0.in", ios::in|ios::binary);
    if (!in_file) // Fehler beim ™ffnen der Datei
    {
     cerr << "\nFehler beim Öffnen der Datei ";
     exit(1);
    }
//PREPARATION    
    int cases_count;
    string subject;
    in_file>>cases_count;
    int i;
         getline(in_file,subject);
    for (i=0;i<cases_count;i++)
       { subject = "";
         getline(in_file,subject);
         printf  ("Case #%i: %04i\n", i+1, find("welcome to code jam",subject));
        //cout<<endl<<endl<<endl<<endl<<endl<<endl;
        }
    return EXIT_SUCCESS;
}
