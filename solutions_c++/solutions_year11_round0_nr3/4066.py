#include <stdio.h>
#include <fstream>
#include <iostream>

using namespace std;

int T,N;
int Narr[15],maximum;
short Carr[15];

void initialize()
{
    for(int i=0;i<15;i++)
    {
        Carr[i] = 0;
    }
}

int checksum(int a)
{
    int sum=0;
        for(int i=0;i<N;i++)
        {
            if(a == Carr[i])
                sum = sum + Narr[i];
        }
    return sum;
}

int checkfalse()
{
    int s1=0,s2=0;

    for(int i=0;i<N;i++)
    {
        if(Carr[i] == 0)
        {
            s1 = s1^Narr[i];
        }
        else
        {
            s2 = s2^Narr[i];
        }
    }
    if(s1 == s2)
        return 1;
    else
        return 0;
}

void distribute(int i)
{
    if(i!=N)
    {
        for(int x=0;x<=1;x++)
        {
            Carr[i] = x;
            distribute(i+1);
        }
    }
    else
    {
        for(int x=0;x<=1;x++)
        {
            Carr[i] = x;
            int sen,pak;
            sen = checksum(0);
            pak = checksum(1);
                if(sen != 0 && pak != 0)
                {
                    if(checkfalse())
                    {
                        if(sen > maximum)
                            maximum = sen;
                    }
                }

        }
    }
}

main()
{
    ifstream fin;
    ofstream fout("outcandysplit.txt");
    fin.open("C-small-attempt1.in");

    fin>>T;
    for(int i=0;i<T;i++)
    {
        initialize();
        fin>>N;
        for(int j=0;j<N;j++)
        {
            fin>>Narr[j];
        }
        if((checksum(0)%2)!=0)
        {
            fout<<"Case #"<<i+1<<": NO\n";
            continue;
        }
        else
        {
            maximum = -1;
            distribute(0);
        }
        if(maximum != -1)
            fout<<"Case #"<<i+1<<": "<<maximum<<endl;
        else
            fout<<"Case #"<<i+1<<": NO\n";
    }

    fin.close();
    fout.close();
}
