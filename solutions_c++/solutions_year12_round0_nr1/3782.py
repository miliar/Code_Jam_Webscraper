#include<iostream>
#include<fstream>
#include<string>
using namespace std;

char replace[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    ifstream in("C:/Users/Ansh/Desktop/A-small-attempt1.in");
    ofstream out("C:/Users/Ansh/Desktop/output.txt");
    string input;
    int testcases;
    in>>testcases;
    getline(in, input);
    for(int i=0; i<testcases; i++)
    {
        getline(in, input);
        out<<"Case #"<<(i+1)<<": ";
        for(int j=0; j<input.length(); j++)
        {
            if(input[j]>='a' && input[j]<='z')
                out<<replace[input[j]-'a'];
            else
                out<<input[j];
        }
        out<<endl;
    }
}
