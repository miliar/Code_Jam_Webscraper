#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector <char> v;
int com[30][30];
bool opp[30][30];

int main ()
{
    FILE *in = fopen ("B.in","r");
    FILE *out = fopen ("B.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int id=1; id<=t; id++)
    {
        int n,c,d;

        v.clear();
        memset (com,-1,sizeof(com));
        memset (opp,0,sizeof(opp));

        fscanf (in,"%d",&c);
        for (int i=0; i<c; i++)
        {
            char c1,c2,c3;
            fscanf (in," %c%c%c",&c1,&c2,&c3);
            com[c1-'A'][c2-'A'] = c3 - 'A';
            com[c2-'A'][c1-'A'] = c3 - 'A';
        }

        fscanf (in," %d",&d);
        for (int i=0; i<d; i++)
        {
            char c1,c2;
            fscanf (in," %c%c",&c1,&c2);
            opp[c1-'A'][c2-'A'] = 1;
            opp[c2-'A'][c1-'A'] = 1;
        }

        fscanf (in," %d ",&n);
        for (int i=0; i<n; i++)
        {
            char c1,tmp;
            fscanf (in,"%c",&c1);
            if (v.size() == 0)
            {
                v.push_back(c1);
                continue;
            }
            else
            {
                tmp = v.back();
                int val = com[tmp-'A'][c1-'A'];
                if (val != -1)
                {
                    v.pop_back();
                    v.push_back((char)val+'A');
                    continue;
                }
                else
                {
                    for (int j=0; j<v.size(); j++)
                    {
                        char use = v[j];
                        if (opp[use-'A'][c1-'A'] == 1)
                        {
                            v.clear();
                            break;
                        }
                    }
                    if (v.size() != 0)
                        v.push_back(c1);
                }
            }
        }

        fprintf (out,"Case #%d: [",id);
        for (int i=0; i<v.size(); i++)
        {
            fprintf (out,"%c",v[i]);
            if (i != v.size()-1) fprintf (out,", ");
        }
        fprintf (out,"]\n");
    }
}
