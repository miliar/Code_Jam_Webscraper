#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    char google[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
    int noc;
    char str[150];
    ifstream in;
    in.open("A-small-attempt1.in");
    ofstream out;
    out.open("output.txt");
    in >> noc;
    in.ignore();
    for(int z=0; z<noc; z++)
    {
      in.getline(str,150);
      int size = strlen(str);
//      cout<<str;
      str[size] = '\0';
      char mystr[size];
      mystr[size] = '\0';
                
      for(int i=0; i<size; i++)
      {
        if (str[i] == ' ') {mystr[i] = ' '; }
        else
        {
           for(int j=0; j<26; j++)
           {
              if (str[i] == google[j]) {mystr[i] = char (97 + j);  break;}
              
           }
        }
      }
    cout<< mystr <<endl;
    out <<"Case #"<<z+1<<": "<< mystr << endl;
    }
    in.close();
    out.close();
    //system("pause");
    return 0;
}
