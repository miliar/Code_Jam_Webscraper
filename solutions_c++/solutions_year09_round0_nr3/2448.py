
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>

using namespace std;

void run()
{
    //const char flnm_in[] = "C-small-attempt0.in";
    //const char flnm_out[] = "C-small.out";
    const char flnm_in[] = "C-large.in";
    const char flnm_out[] = "C-large.out";
    char buf[1000];
    ifstream i_file;
    i_file.open(flnm_in);
    if (!i_file.is_open())
        return;
    i_file.getline(buf, 600, '\n');
    int N = atoi(buf);
    char tc[100][601];
    for (int i=0;i<N;i++)
    {
        i_file.getline(tc[i], 600, '\n');
    }
    i_file.close();

    ofstream o_file;
    o_file.open(flnm_out);
    const char s[] = "welcome to code jam";
    int ls = strlen(s);
    for (int i=0;i<N;i++)
    {
        long long n[501][19];
        memset(n,0,sizeof(n));
        int lt=strlen(tc[i]);
        int cc=0;
        for (int j=0;j<lt;j++)
        {
            if (tc[i][j] == s[0])
                cc++;
            n[j][0] = cc;
        }
        for (int b=1;b<ls;b++)
            for (int j=1;j<lt;j++)
            {
                n[j][b] = n[j-1][b]+((tc[i][j]==s[b])?n[j-1][b-1]:0);
                n[j][b] = n[j][b] % 10000;
            }
        char num[5];
        sprintf(num, "%4d", n[lt-1][ls-1]);
        for (int k=0;k<4;k++)
        {
            if (num[k]==' ')
                num[k]='0';
        }
        char msg[100];
        sprintf(msg, "Case #%d: %s\n", i+1, num);
        o_file<<msg;
    }
    o_file.close();
};

int main(int argc, char* argv[])
{
    run();
	return 0;
}
