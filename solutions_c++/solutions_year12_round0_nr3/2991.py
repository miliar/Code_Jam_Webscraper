#include <iostream>
#include <cstring>
#include <sstream>
#include <set>
using namespace std;

int str2int(char *start, char *end)
{
    int value = 0;
    char *p = start;

    while (*p && p<=end)
    {
        value = value*10 + *p-'0';
        p++;


    }
    return value;
}


int main()
{
    int T;
    cin >> T;

    for (int testcase=1; testcase <= T; ++testcase) {


        int a, b;
        cin >> a >> b;

        set< pair<int, int> > total;

        for(int i=a; i<=b; i++)
        {
            stringstream s(stringstream::in | stringstream::out);
            char num[20], dnum[40];

            s << i;
            s >> num;
            strcpy(dnum, num);
            strcat(dnum, num);

            int len = strlen(num);


            int j,k , l;
            for(j=1; j<len; j++)
            {
                int ret = str2int(dnum+ j, dnum+j+len-1);

                if(ret!=i && ret>=a && ret<=b)
                    if(ret < i)
                        total.insert(make_pair(ret, i));
                    else
                        total.insert(make_pair(i, ret));
            }

        }
        cout << "Case #" << testcase <<": " <<total.size() << endl;


    }
    return 0;
}
