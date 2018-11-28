#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;


/*
Input 

4
1 9
10 40
100 500
1111 2222

Output

Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287
*/

int calc(string in, string upper)
{
    int count = 0;
    int len = in.length();
    string in2 = in + in;
    vector<string> result;
    for (int idx = 1 ; idx < len ; ++idx)
    {
        int i = 0, j = idx;

        while(i < len)
        {
            if (in2[i] < in2[j])
            {
                string r(in2.substr(idx, len));
                if (r <= upper && find(result.begin(), result.end(), r) == result.end())
                {
                    result.push_back(r);
                    ++count;
                }
                break;
            }
            else if (in2[i] > in2[j])
            {
                break;
            }

            ++i;
            ++j;
            //++idx;
        }
    }

    return count;
}

int main()
{
    FILE *ifile = freopen("C-large.in", "r", stdin);
    FILE *ofile = freopen("output_data.txt", "w", stdout);

    int num_inputs = 1;
    scanf("%d \r\n", &num_inputs);

    int start, end;
    for (int i = 0 ; i < num_inputs ; ++i)
    {
        scanf("%d %d", &start, &end);

        int count = 0;
        char buf[1024];

        itoa(end, buf, 10);
        string upper(buf);
        for (int n = start; n <= end ; ++n)
        {
            itoa(n, buf, 10);
            count += calc(buf, upper);
        }

        printf("Case #%d: %d\n", (i+1), count);
    }

    fclose(ifile);
    fclose(ofile);

    return 0;
}