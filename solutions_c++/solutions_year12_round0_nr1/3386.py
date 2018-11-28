#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;
int main()
{
    char G[] = {'y','h','e','s', 'o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w',
        'j','p','f','m','a','q','q'};
    string line;
    int c;
    ifstream myfile("input.txt");
    ofstream myOfile("output.txt");
    if(myfile.is_open()&&myOfile.is_open()){
         getline(myfile,line);
         stringstream convert(line);
         if(!(convert>>c))
                          c=0;
         for(int i=0;i<c;i++){
                             getline(myfile,line);
                             int l = line.length();
                             for(int j=0;j<l;j++)
                                     line[j]=G[line[j]-'a'];
                             myOfile<<"Case #"<<i+1<<": "<<line<<endl;
         }
         myfile.close();
    }else{
               cout << "Uneable to find file";
          }
    system("PAUSE");
    return 0;
}
