
#include <stdio.h>
#include <string.h>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>

#define MAX_LEN 62

void GCJ_2009Round1C_A(const char*input, const char*output)
{
    FILE* fin = freopen(input, "rb", stdin);
    FILE* fout = freopen(output, "wb", stdout);

    int N, ncase = 0;
    scanf("%d", &N);
    while (ncase ++ < N)
    {
        //run one test case
        char data[MAX_LEN];
        std::set<char>elements;

        scanf("%s", data);

        int len = strlen(data);
        for (int i = 0; i < len; i ++)
        {
            elements.insert(data[i]);
        }

        int base = elements.size();
        if (base < 2)
        {
            base = 2;
        }

        std::map<char, int>digts;
        int numbers[MAX_LEN];
        int d = 0;

        digts[data[0]] = 1;
        numbers[0] = 1;
        for (int i = 1; i < len; i ++)
        {
            if (digts.find(data[i]) == digts.end())
            {
                digts[data[i]] = d;
                numbers[i] = d;

                d ++;
                if (d == 1)
                {
                    d = 2;
                }
            }
            else
            {
                numbers[i] = digts[data[i]];
            }
        }

        long long ret = 0;

        for (int i = 0; i < len; i ++)
        {
            ret = ret * base + numbers[i];
        }

        printf("Case #%d: %lld\n", ncase, ret);
    }

    fclose(fin);
    fclose(fout);
}

int main(int argc, char** argv)
{
    char*in_file = "gcj.in";
    char*out_file = "gcj.out";

    GCJ_2009Round1C_A(in_file, out_file);


    return 0;
}