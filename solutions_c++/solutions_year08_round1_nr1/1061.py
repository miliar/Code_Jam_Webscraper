#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>

#define BUFSZ 10000

bool decsort(int a, int b)
{
    return a > b;
}

int main(int argc, char *argv[])
{
    FILE *fp;
//    freopen(argv[1], "rt", stdin);
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T, n;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }

    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (int i=0; i<T; i++)
    {
        int j;
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        n = atoi(token);

        std::vector<int> x;
        std::vector<int> y;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        for (j=0, subtoken = strtok_r(token, " ", &sptr2);
             j<n;
             j++, subtoken = strtok_r(NULL, " ", &sptr2))
        {
            x.push_back(atoi(subtoken));
        }

        std::sort(x.begin(), x.end());

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        for (j=0, subtoken = strtok_r(token, " ", &sptr2);
             j<n;
             j++, subtoken = strtok_r(NULL, " ", &sptr2))
        {
            y.push_back(atoi(subtoken));
        }

        std::sort(y.begin(), y.end(), decsort);

        /*
        for (j=0; j < n; j++)
        {
            std::cout << x[j] << ' ';
        }
        std::cout << std::endl;

        for (j=0; j < n; j++)
        {
            std::cout << y[j] << ' ';
        }
        std::cout << std::endl;
        */


        long int sum = 0;;
        for (j=0; j < n; j++)
        {
            sum += x[j]*y[j];
        }
        std::cout << "Case #" << i+1 << ": " << sum << std::endl;




    }
    return 0;
}
