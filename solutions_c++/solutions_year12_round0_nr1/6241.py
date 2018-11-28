#include<iostream>
#include<cstdio>
#include<fstream>
#define N 1000
using namespace std;

int main()
{
    //int a,b;
    int alpha[26] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
    ifstream fin("A-small-attempt2.in");
    ofstream fout("A-small-attempt2.out");
    char str[N];//result[N];
    int t=30;
    char as[10];
    //fin>>t;
    fin.getline(as,10);
    int k=1;
    for(int q=0;q<t;q++)
    {
            
            for(int i=0;i<N;i++)
                    str[i] = '\0';
            fin.getline(str,1000);
            //int x = 0;
            fout<<"Case #"<<k<<": ";
            for(int i=0;str[i]!='\0';i++)
            {
                    if(str[i] == ' ')
                    {   fout<<" ";continue;}
                    //x = str[i]%97;
                    fout<<(char)(alpha[str[i]%97] + 97);
            }
            k++;
            fout<<endl;
    }
    //system("pause");
    return 0;
}
