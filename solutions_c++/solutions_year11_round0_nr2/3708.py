#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

//ifstream fin("input.txt");

ofstream fout("output.txt");

char opp[29][2], comb[37][3], str[101];

int main()
{
    freopen("input.txt", "r", stdin);
    int C, D, N, i, f, j, k, i2, T, CASE;
    char c;


scanf("%d", &T);
for (CASE=1; CASE <= T; CASE++)
{

    scanf("%d", &C);
    for (i=1; i<=C; i++)
    {
        do{
        scanf("%c", &c);
        }while (c==' ');
        comb[i][0]=c;
        do{
        scanf("%c", &c);
        }while (c==' ');
        comb[i][1]=c;
        do{
        scanf("%c", &c);
        }while (c==' ');
        comb[i][2]=c;
        //cout << comb[i][0] << comb[i][1] << comb[i][2] << endl;
    }
    scanf("%d", &D);
    for (i=1; i<=D; i++)
    {
        do{
        scanf("%c", &c);
        }while (c==' ');
        opp[i][0]=c;
        do{
        scanf("%c", &c);
        }while (c==' ');
        opp[i][1]=c;
        //cout << opp[i][0] << opp[i][1] << endl;
    }

    scanf("%d", &N);
    getchar();
    f=0; i=0;
    for (i2=1; i2<=N; i2++)
    {
        f=0;
        i++;
        scanf("%c", &c);
        str[i]=c;
        for (j=1; j<=C; j++)
            if (comb[j][0]==c)
                if (comb[j][1]==str[i-1])
                {
                    str[i-1]=comb[j][2];
                    f=1;
                    str[i]=0;
                    i--;
                }

        if (f==0)
        for (j=1; j<=C; j++)
            if (comb[j][1]==c)
                if (comb[j][0]==str[i-1])
                {
                    str[i-1]=comb[j][2];
                    f=1;
                    str[i]=0;
                    i--;
                }

        if (f==0)
        for (j=1; j<=D; j++)
            if (opp[j][0]==c)
            {
                for (k=1; k<=i-1; k++)
                    if (str[k]==opp[j][1])
                        i=0;
            }
            else if (opp[j][1]==c)
            {
                for (k=1; k<=i-1; k++)
                    if (str[k]==opp[j][0])
                        i=0;
            }
        str[i+1]=0;
    }


    fout << "Case #" << CASE << ": ";
    fout << "[";
    if (str[1]!=0)
    {
        fout << str[1];
        i=2;
        while (str[i]!=0)
        {
            fout << ", " << str[i];
            i++;
        }
    }
    fout << "]" << endl;
}
    return 0;
}
