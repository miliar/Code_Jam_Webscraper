#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A.in");
char code[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
ofstream fout("Aout.txt");
int main()
{
    int N;
    char temp[200];
    fin >> N;
    //cout << N;
    //cout << code[0] << endl;
    fin.getline(temp,200);
    for(int i=1;i<=N;i++)
    {
        fin.getline(temp,200);
        //cout << temp << endl;
        int index = 0;
        while(temp[index]!='\0')
        {
            if(temp[index]==' ');
            else temp[index]=code[temp[index]-'a'];
            index++;
        }
        fout << "Case #" << i << ": " << temp << endl;
    }
}
