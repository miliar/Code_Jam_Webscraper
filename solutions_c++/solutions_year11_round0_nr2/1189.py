#include <iostream>
#include <fstream>
#include <string>
using namespace std;
inline int trans(char a)
{
    if(a=='Q')return 0;
    if(a=='W')return 1;
    if(a=='E')return 2;
    if(a=='R')return 3;
    if(a=='A')return 4;
    if(a=='S')return 5;
    if(a=='D')return 6;
    if(a=='F')return 7;
    return -1;
}
inline void clear(char a[], int n)
{
    while(n--)
        a[n] = 0;
}
inline void clear(int a[], int n)
{
    while(n--)
        a[n] = 0;
}
int main()
{
    fstream fout, fin;
    fout.open("output.txt");
    fin.open("input.txt");
    int T, C, D, N, t;
    fin>>T;
    for(t=1; t<=T; ++t)
    {
        int exiele[8]={0}, oppele[8*8+8]={0};
        char combele[8*8+8]={0};
        char output[101] = {0};
        char *end = output;
        fin>>C;
        char a, b, c;
        while(C--)
        {
            fin>>a>>b>>c;
            combele[trans(a)*8+trans(b)] = c;
            combele[trans(b)*8+trans(a)] = c;
        }
        fin>>D;
        while(D--)
        {
            fin>>a>>b;
            oppele[trans(a)*8+trans(b)] = 1;
            oppele[trans(b)*8+trans(a)] = 1;
        }
        fin>>N;
        while(N--)
        {
            fin>>a;
            int i;
            if(end != output)
            {
                if( (trans(*(end-1)) != -1) && (b = combele[trans(*(end-1))*8+trans(a)]))
                {
                    exiele[trans(*(end-1))] -= 1;
                    *(end-1) = b;
                }
                else
                {
                    for(i=0; i<8; ++i)
                    if(exiele[i])
                        if(oppele[trans(a)*8+i])
                        {
                            clear(output, end-output);
                            clear(exiele, 8);
                            end = output;
                            break;
                        }
                    if(i==8)
                        *end++ = a, exiele[trans(a)] += 1;
                }
            }
            else
                *end++ = a, exiele[trans(a)] = 1;
        }
        fout<<"Case #"<<t<<": [";
        if(end != output)
        {
            char *begin = output;
            fout<<*begin++;
            while(begin != end)
                fout<<", "<<*begin++;
        }
        fout<<"]"<<endl;
    }
    return 0;
}
