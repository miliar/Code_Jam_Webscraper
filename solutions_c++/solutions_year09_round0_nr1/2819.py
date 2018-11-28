#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    char str[5020][20];
    int strcheck[5020][20];
    char temp[800];
    ifstream fin("c:\\test.txt");
    ofstream fout("c:\\output.txt");
    int L, D, N;
    fin>>L>>D>>N;
    for(int i = 0; i < D; i++)
    {
        fin>>str[i];
    }
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < D; j++)
        {
            for(int k = 0; k < L; k++)
            {
                strcheck[j][k] = 0;
            }
        }
        fin>>temp;
        int now = 0;
        for(int j = 0; temp[j]!='\0';j++)
        {
            if(temp[j] == '(')
            {
                j++;
                while(temp[j]!= ')')
                {
                    for(int k = 0; k < D; k++)
                    {
                        if(str[k][now] == temp[j])
                        {
                            strcheck[k][now] = 1;
                        }
                    }
                    j++;
                }
                now++;
            }
            else
            {
                for(int k = 0; k < D; k++)
                {
                    if(str[k][now] == temp[j])
                    {
                        strcheck[k][now] = 1;
                    }
                }
                now++;
            }
        }
        int sum = 0;
        int check;
        for(int j = 0; j < D; j++)
        {
            check = 0;
            for(int k = 0; k < L; k++)
            {
                if(strcheck[j][k] != 1)
                {
                    check = 1;
                }
            }
            if(check == 0)
            {
                sum++;
            }
        }
        fout<<"Case #"<<i+1<<": "<<sum<<endl;
    }



    fin.close();
    fout.close();
    return 0;
}
