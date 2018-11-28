#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("A-small.txt");
    out.open("out.txt");
    int t=0,temp=0;
    string In, Out;
    in>>temp;
    getline(in,In);
    while(temp){
        ++t;
        Out=In;
        getline(in,In);
        Out=In;
        for(int i=0; i<In.size();++i){
            if(In[i]=='a') Out[i]='y';
            if(In[i]=='b') Out[i]='h';
            if(In[i]=='c') Out[i]='e';
            if(In[i]=='d') Out[i]='s';
            if(In[i]=='e') Out[i]='o';
            if(In[i]=='f') Out[i]='c';
            if(In[i]=='g') Out[i]='v';
            if(In[i]=='h') Out[i]='x';
            if(In[i]=='i') Out[i]='d';
            if(In[i]=='j') Out[i]='u';
            if(In[i]=='k') Out[i]='i';
            if(In[i]=='l') Out[i]='g';
            if(In[i]=='m') Out[i]='l';
            if(In[i]=='n') Out[i]='b';
            if(In[i]=='o') Out[i]='k';
            if(In[i]=='p') Out[i]='r';
            if(In[i]=='q') Out[i]='z';
            if(In[i]=='r') Out[i]='t';
            if(In[i]=='s') Out[i]='n';
            if(In[i]=='t') Out[i]='w';
            if(In[i]=='u') Out[i]='j';
            if(In[i]=='v') Out[i]='p';
            if(In[i]=='w') Out[i]='f';
            if(In[i]=='x') Out[i]='m';
            if(In[i]=='y') Out[i]='a';
            if(In[i]=='z') Out[i]='q';
        }
        out<<"Case #"<<t<<": "<<Out<<endl;
        --temp;
    }
    in.close();
    out.close();
    return 0;
}
