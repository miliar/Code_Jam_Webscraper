#include<algorithm>
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int main()
{
    int i , k ,c = 0 , fl = 0;
    char x[20];
    fscanf(in,"%d\n",&k);
    string t , tt;
    while(k)
    {
        k--;
        c++;
        fscanf(in,"%s",x);
        t = x;
        fl = 0;
        for(i=0;i<t.size();i++)
            for(int a=i+1;a<t.size();a++)
                if(t[a] > t[i]){ fl = 1; break;}
        fprintf(out,"Case #%d: ",c);
        if(fl)
        {
            next_permutation(t.begin(),t.end());
            for(i=0;i<t.size();i++)
                fprintf(out,"%c",t[i]);
            fprintf(out,"\n");
        }
        else
        {
            t = x;
            t += '0';
            sort(t.begin(),t.end());
            do
            {
                if(t[0] != '0') break;
            }while(next_permutation(t.begin(),t.end()));
            for(i=0;i < t.size();i++)
                fprintf(out,"%c",t[i]);
            fprintf(out,"\n");
        }
        printf("%d\n",c);
    }
    return 0;
}
