#include<cstdio>
using namespace std;

void transform(char *buff)
{
    char arr[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    for(int i=0;buff[i]!='\0';++i)
    {
        if(buff[i]!=' ')
            buff[i] = arr[buff[i]-'a'];
    }

}

int main()
{
    int T=0;
    char buff[102];

    FILE *fin,*fout;
    fin=fopen("input.in","r");
    fout=fopen("output.txt","w");

    //freopen("input.in","r",stdin);

    fscanf(fin,"%d\n",&T);
    for(int i=0;i<T;++i)
    {
        fscanf(fin,"%[^\n]%*c",buff);
        transform(buff);
        fprintf(fout,"Case #%d: %s\n",i+1,buff);
    }
    return 0;
}
