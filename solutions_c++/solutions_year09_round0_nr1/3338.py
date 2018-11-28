#include <iostream>
#include <stdio.h>

using namespace std;


bool match (const char* pattern, const char* word)
{
    int mode =0;

    int plen =strlen(pattern);
    int wlen = strlen(word);
    int wi =0;
    int pi =0;
    while(1)
    {
        if(pi==plen-1)
           break;
        if(mode==0)
        {
            if(pattern[pi]=='(')
            {
                mode =1;
                pi++;
            }
            else if (pattern[pi]>'z'||pattern[pi]<'a')
            {
                return false;
            }
            else
            {
                if(pattern[pi]!=word[wi])
                   return false;
                else
                {
                    pi++;
                    wi++;


                }

            }
        }
        else
        {
            if(pattern[pi]==')')
            {
                mode =0;
                pi++;
            }
            else if (pattern[pi]>'z'||pattern[pi]<'a')
            {
                return false;
            }
            else
            {
                if(pattern[pi]==word[wi])
                {
                    wi++;
                    while (pattern[pi]!=')')
                       pi++;
                    pi++;
                    mode =0;

                }
                else
                   pi++;

            }
        }
    }

    if (0!=mode)
       return false;
    if (wi==wlen)
        return true;
    else
        return false;

}
void getInt(FILE *fp, int * a)
{
    *a =0;

    while(1)
    {
        char ch=fgetc(fp);
        if (ch!=' '&& ch!='\n')
        {
            if((ch>'9')||(ch<'0'))
                break;
            *a = *a*10+(ch-'0');
        }
        else
        {
            break;
        }
    }
}
int main()
{

    int D,L,N;
    int* caseResult;
    char ** word ;
    FILE *fp;
    if((fp=fopen("c:\\a.in","r"))==NULL)  /*以只写方式打开文件*/
    {
        printf("cannot open file!\n");
        exit(0);
    }
    getInt(fp,&L);
    getInt(fp,&D);
    getInt(fp,&N);
    word = new char* [D];
    caseResult =new int[N];
    for(int i=0;i<D;i++)
    {
        word[i]=new char[L+1];
        memset(word[i],0x0,L+1);
        fgets(word[i],L+1,fp);
        char ch=fgetc(fp);
        if(ch!='\n')
           cout<<"wrong word"<<"i="<<i<<endl;
    }
    for(int i=0;i<D;i++)
    {
        char pattern[256];
        memset(pattern,0x0,256);
        fgets(pattern,257,fp);
        int success=0;
        for(int j=0;j<D;j++)
        {
            if (match(pattern,word[j]))
               success++;
        }
        caseResult[i]=success;
    }
    fclose(fp);
    if((fp=fopen("c:\\output","w"))==NULL)  /*以只写方式打开文件*/
    {
        printf("cannot open file!\n");
        exit(0);
    }
    for(int i=0;i<N;i++)
    {
        fprintf(fp,"Case #%d: %d\n",i+1,caseResult[i]);
    }
    fclose(fp);

    return 0;
}
