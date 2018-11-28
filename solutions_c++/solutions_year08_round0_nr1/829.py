#include <stdio.h>
#include <string>
#include <map>
using namespace std;
int main()
{
    FILE *in,*out;
    int n, count, sn, qn, bsn, i, j;
    char sc[1001];    
    
    in = fopen("in.txt","r");
    out = fopen("a.txt","w");
    
    fscanf(in,"%d\n",&n);
    for (i=0; i<n; i++)
    {
        map<string, int> se;
        map<string, int>::iterator mp;
        count = 0;
        fscanf(in,"%d\n",&sn);
        for(j=0; j<sn; j++)
        {
            fgets(sc,1000,in);
            string s(sc);
            se[s] = 1;
        }
        for (mp=se.begin(); mp!=se.end() ;mp++)
            printf("%s %d\n",mp->first.c_str(),mp->second);
        getchar();
        fscanf(in,"%d\n",&qn);        
        bsn = sn;
        for(j=0; j<qn; j++)
        {
            fgets(sc,1000,in);
            string s(sc);
re:            
            if (se[s])
            {   
                bsn--;
                printf("b = %d",bsn);
                se[s] = 0;
                if (!bsn)
                {
                    count++;
                    for (mp=se.begin(); mp!=se.end() ;mp++)
                        mp->second = 1;
                    bsn = sn;
                    goto re;
                }
            }
        }
        fprintf(out,"Case #%d: %d\n",i+1,count);                
    }
    fclose(in);
    fclose(out);
}
