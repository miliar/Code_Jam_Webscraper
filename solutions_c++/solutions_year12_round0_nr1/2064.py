#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
    int t,p,length,i,j;
    char ele;
    string str;
    fstream fp;
    fp.open("input.txt");
    fp >> t;
    p=t;
    for(j=0;j<t;j++)
    {
        if(j==0)
        {
            getline(fp,str);
        }
        getline(fp,str);
        //break;
        //cout<<str<<endl;
        //insert(str[i]);
        i=0;
        while(str[i]!='\0')
        {
            if(str[i]==' ')
            {
                str[i]=' ';
            }
            else
            {
            switch(str[i])
            {
                case 'a':ele='y';
                            break;
                case 'b':ele='h';
                            break;

                case 'c':ele='e';
                            break;
                case 'd':ele='s';
                            break;

                case 'e':ele='o';
                            break;
                case 'f':ele='c';
                            break;

                case 'g':ele='v';
                            break;
                case 'h':ele='x';
                            break;

                case 'i':ele='d';
                            break;
                case 'j':ele='u';
                            break;

                case 'k':ele='i';
                            break;
                case 'l':ele='g';
                            break;

                case 'm':ele='l';
                            break;
                case 'n':ele='b';
                            break;

                case 'o':ele='k';
                            break;
                case 'p':ele='r';
                            break;

                case 'q':ele='z';
                            break;
                case 'r':ele='t';
                            break;

                case 's':ele='n';
                            break;
                case 't':ele='w';
                            break;

                case 'u':ele='j';
                            break;
                case 'v':ele='p';
                            break;

                case 'w':ele='f';
                            break;
                case 'x':ele='m';
                            break;

                case 'y':ele='a';
                            break;
                case 'z':ele='q';
                            break;
            }
            str[i]=ele;
            }
            i++;
        }
        cout<<"Case #"<<j+1<<": "<<str<<endl;
    }
    //cout<<str;
    fp.close();
}
