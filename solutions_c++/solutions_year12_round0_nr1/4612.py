#include<iostream>
#include<fstream>

using namespace std;

main()
{
    int i,j;
    string msg;
    ifstream ifs;
    ifs.open("input1.txt");
    int n;
    ifs>>n;
    getline(ifs,msg);
    ofstream ofs;
    ofs.open("output1.txt");
    for(i=1;i<=n;i++)
    {
        getline(ifs,msg);
        char newMsg[msg.size()];
        cout<<msg<<endl;
        for(j=0;j<(msg.size());j++)
        {
            char ch = msg[j];
            switch(ch)
            {
                case 'a':
                newMsg[j]='y';
                break;

                case 'b':
                newMsg[j]='h';
                break;

                case 'c':
                newMsg[j]='e';
                break;

                case 'd':
                newMsg[j]='s';
                break;

                case 'e':
                newMsg[j]='o';
                break;

                case 'f':
                newMsg[j]='c';
                break;

                case 'g':
                newMsg[j]='v';
                break;

                case 'h':
                newMsg[j]='x';
                break;

                case 'i':
                newMsg[j]='d';
                break;

                case 'j':
                newMsg[j]='u';
                break;

                case 'k':
                newMsg[j]='i';
                break;

                case 'l':
                newMsg[j]='g';
                break;

                case 'm':
                newMsg[j]='l';
                break;

                case 'n':
                newMsg[j]='b';
                break;

                case 'o':
                newMsg[j]='k';
                break;

                case 'p':
                newMsg[j]='r';
                break;

                case 'q':
                newMsg[j]='z';
                break;

                case 'r':
                newMsg[j]='t';
                break;

                case 's':
                newMsg[j]='n';
                break;

                case 't':
                newMsg[j]='w';
                break;

                case 'u':
                newMsg[j]='j';
                break;

                case 'v':
                newMsg[j]='p';
                break;

                case 'w':
                newMsg[j]='f';
                break;

                case 'x':
                newMsg[j]='m';
                break;

                case 'y':
                newMsg[j]='a';
                break;

                case 'z':
                newMsg[j]='q';
                break;

                case ' ':
                newMsg[j]=' ';
                break;
            }
        }
        ofs<<"Case #"<<i<<": "<<newMsg<<endl;
    }
    ifs.close();
    ofs.close();
}
