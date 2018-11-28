#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_D 5010

char s[MAX_D][1024];
vector<string> r;

int main(void)
{
    int L,D,N;

    scanf("%d %d %d",&L,&D,&N);

    for(int i = 0; i < D; i++)
        scanf("%s",s[i]);

    for(int i = 0; i < N; i++)
    {
        scanf("%s",s[D]);
        r.clear();
        int pos = 0;
        for(int j = 0; s[D][j]; j++,pos++)
        {
            if (s[D][j] == '(')
            {
                int k;
                for(k = 0; s[D][j+k+1] != ')'; k++)
                    s[D+1][k] = s[D][j+k+1];
                s[D+1][k] = 0;

                if (pos == 0)
                {
                    for(int z = 0; z < D; z++)
                        if (strchr(s[D+1],s[z][0]))
                            r.push_back(s[z]);
                }
                else
                {
                    for(int z = 0; z < (int)r.size(); z++)
                        if (pos >= L || strchr(s[D+1],r[z][pos]) == NULL)
                        {
                            r.erase(r.begin()+z);
                            z--;
                    }
                }

                j += k+1;
            }
            else
            {
                if (pos == 0)
                {
                    for(int k = 0; k < D; k++)
                        if (s[k][pos] == s[D][j])
                            r.push_back(string(s[k]));
                }
                else
                {
                    for(int k = 0; k < (int)r.size(); k++)
                        if (pos >= L || r[k][pos] != s[D][j])
                        {
                            r.erase(r.begin()+k);
                            k--;
                        }
                }
            }
        }

        printf("Case #%d: %d\n",i+1,(int)r.size());
    }

    return(0);
}

