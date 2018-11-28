
#include <stdio.h>
#include <string.h>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>

void GCJ_2009Qulification3(const char*input, const char*output)
{
    FILE* fin = freopen(input, "rb", stdin);
    FILE* fout = freopen(output, "wb", stdout);

#define MAX_TEXT_LEN 501
#define GCJ_LEN 19
#define GCJ_MOD(v) ((v)%10000)

    int N, ncase = 0;
    scanf("%d\n", &N);
    while (ncase ++ < N)
    {
        //run one test case
        char* gcj = "welcome to code jam";
        char s[MAX_TEXT_LEN+1] = {0};
        int cnt[GCJ_LEN+1][MAX_TEXT_LEN+1] = {0};

        gets(s);
        //scanf("%s", s);

        //DP
        int len = strlen(s);

        //initialize
        cnt[0][0] = (gcj[0] == s[0]) ? 1 : 0;
        for (int j = 1; j < len; j ++)
        {
            if (gcj[0] == s[j])
            {
                cnt[0][j] = cnt[0][j-1] + 1;
            }
            else 
            {
                cnt[0][j] = cnt[0][j-1];
            }            
        }

        for (int i = 1; i < GCJ_LEN; i ++)
        {
            for (int j = i; j < len; j ++)
            {
                cnt[i][j] = cnt[i][j-1];
                
                if (gcj[i] == s[j])
                {
                    cnt[i][j] = GCJ_MOD(cnt[i][j] + cnt[i-1][j-1]);
                }
            }
        }

        //output
        if (cnt[GCJ_LEN-1][len-1] < 10)
        {
            printf("Case #%d: 000%d\n", ncase, cnt[GCJ_LEN-1][len-1]);
        }
        else if (cnt[GCJ_LEN-1][len-1] < 100)
        {
            printf("Case #%d: 00%d\n", ncase, cnt[GCJ_LEN-1][len-1]);
        }
        else if (cnt[GCJ_LEN-1][len-1] < 1000)
        {
            printf("Case #%d: 0%d\n", ncase, cnt[GCJ_LEN-1][len-1]);
        }
        else
        {
            printf("Case #%d: %d\n", ncase, cnt[GCJ_LEN-1][len-1]);
        }
    }

    fclose(fin);
    fclose(fout);
}

int main(int argc, char** argv)
{
    char*in_file = "gcj.in";
    char*out_file = "gcj.out";

    GCJ_2009Qulification3(in_file, out_file);


    return 0;
}