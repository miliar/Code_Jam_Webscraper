#include <cstdio>
#include <string>

using namespace std;

int main()
{
    string a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";
    string b="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";
    FILE* be = fopen("small.in","r");
    char c;
    int db;
    fscanf(be,"%d%c",&db,&c);
    int i=0;
    FILE* ki=fopen("ki.out","w");
    fprintf(ki,"Case #1: ");
    while(i<db)
    {
        fscanf(be,"%c",&c);
        if((c=='\n') && (i<db-1))
        {
            fprintf(ki,"\nCase #%d: ",i+2);
            i++;
        }
        else if(c=='\n')
        {
            i++;
        }
        else
        {
            fprintf(ki,"%c", b[a.find(c)]);
        }
    }
}
