#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int i,j,T,length;
    FILE *in=fopen("C:\\Users\\yl\\Desktop\\A-small-attempt1.in","r");
    FILE *out=fopen("C:\\Users\\yl\\Desktop\\A-small-attempt1.out","w");
    char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char* str=new char[200];
    fscanf(in,"%d\n",&T);
    for(i=0;i<T;i++)
    {
       fgets(str,105,in);               
       length=strlen(str);
       for(j=0;j<length-1;j++)
       {
           if(str[j]!=32)
              str[j]=map[str[j]-97];
       }
       fprintf(out,"Case #%d: %s",i+1,str);
    }
    system("pause");
    return 0; 
}
