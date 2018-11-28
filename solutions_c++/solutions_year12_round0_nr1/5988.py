#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    ifstream in("tongues.in");
    ofstream out("out-tongues.txt");
    int t;
    in>>t;
    char str[102];
    in.getline(str, 101);
    for(int cas =1; cas<=t; cas++)
    {
        out<<"Case #"<<cas<<": ";
        in.getline(str,101);
        for(int i =0; str[i]!='\0';i++)
        {
            if( str[i] == ' ')
             out<<" ";
            else
             out<<map[str[i]-'a'];
        }
        out<<endl;
    }
   // system("pause");
}
