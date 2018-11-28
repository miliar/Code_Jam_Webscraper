#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int N;
    char G[101];
    cin>>N;
    cin.getline(G,101);
    for (int i=0; i<N; i++)
    {
        cin.getline(G,101);

        for (int j=0; j<strlen(G); j++)
        {
            switch ((int)G[j])
            {
                case 97:  //a
                G[j]='y';
                break;
                case 98:  //b
                G[j]='h';
                break;
                case 99:  //c
                G[j]='e';
                break;
                case 100: //d
                G[j]='s';
                break;
                case 101: //e
                G[j]='o';
                break;
                case 102: //f
                G[j]='c';
                break;
                case 103: //g
                G[j]='v';
                break;
                case 104: //h
                G[j]='x';
                break;
                case 105: //i
                G[j]='d';
                break;
                case 106: //j
                G[j]='u';
                break;
                case 107: //k
                G[j]='i';
                break;
                case 108: //l
                G[j]='g';
                break;
                case 109: //m
                G[j]='l';
                break;
                case 110: //n
                G[j]='b';
                break;
                case 111: //o
                G[j]='k';
                break;
                case 112: //p
                G[j]='r';
                break;
                case 113: //q
                G[j]='z';
                break;
                case 114: //r
                G[j]='t';
                break;
                case 115: //s
                G[j]='n';
                break;
                case 116: //t
                G[j]='w';
                break;
                case 117: //u
                G[j]='j';
                break;
                case 118: //v
                G[j]='p';
                break;
                case 119: //w
                G[j]='f';
                break;
                case 120: //x
                G[j]='m';
                break;
                case 121: //y
                G[j]='a';
                break;
                case 122: //z
                G[j]='q';
                break;

            }
        }
        cout<<"\nCase #"<<i+1<<": "<<G<<"\n";

    }
    return 0;
}
