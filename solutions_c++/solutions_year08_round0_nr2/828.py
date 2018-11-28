#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    FILE *in,*out;
    int n, t, na, nb, h, m, traina, trainb, i, j, k;   
    
    in = fopen("in.txt","r");
    out = fopen("b.txt","w");
    
    fscanf(in,"%d\n",&n);
    for (i=0; i<n; i++)
    {
        fscanf(in,"%d\n",&t);
        fscanf(in,"%d %d\n",&na, &nb);
        vector<int> froma(na), tob(na), fromb(nb), toa(nb);
        vector<char> sa(na,1), sb(nb,1);
        for (j=0; j<na; j++)
        {
            fscanf(in,"%d:%d ",&h, &m);
            froma[j] = h*60 + m;
            
            fscanf(in,"%d:%d\n",&h, &m);
            tob[j] = h*60 + m + t;
        }
        
        for (j=0; j<nb; j++)
        {
            fscanf(in,"%d:%d ",&h, &m);
            fromb[j] = h*60 + m;
            
            fscanf(in,"%d:%d\n",&h, &m);
            toa[j] = h*60 + m + t;
        }
        
        traina = na;
        trainb = nb;
        sort(froma.begin(),froma.end());
        sort(fromb.begin(),fromb.end());
        for (j=0; j<nb; j++)
        {
            for(k=0; k<na; k++)
            {
                if (sa[k] && (toa[j] <= froma[k]))
                {
                    sa[k] = 0;
                    traina--;
                    break;
                }
            }
        }
        
        for (j=0; j<na; j++)
        {
            for(k=0; k<nb; k++)
            {
                if (sb[k] && (tob[j] <= fromb[k]))
                {
                    sb[k] = 0;
                    trainb--;
                    break;
                }
            }
        }
        
        fprintf(out,"Case #%d: %d %d\n",i+1, traina, trainb);                
    }
    fclose(in);
    fclose(out);
}
