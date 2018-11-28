#include<iostream>
#include<cstdio>

char map(char x)
{
     char y;
     switch(x)
     {
              case 'a':y='y';break;
              case 'b':y='h';break;
              case 'c':y='e';break;
              case 'd':y='s';break;
              case 'e':y='o';break;
              case 'f':y='c';break;
              case 'g':y='v';break;
              case 'h':y='x';break;
              case 'i':y='d';break;
              case 'j':y='u';break;
              case 'k':y='i';break;
              case 'l':y='g';break;
              case 'm':y='l';break;
              case 'n':y='b';break;
              case 'o':y='k';break;
              case 'p':y='r';break;
              case 'q':y='z';break;
              case 'r':y='t';break;
              case 's':y='n';break;
              case 't':y='w';break;
              case 'u':y='j';break;
              case 'v':y='p';break;
              case 'w':y='f';break;
              case 'x':y='m';break;
              case 'y':y='a';break;
              case 'z':y='q';break;
              case ' ':y=' ';break;
              case '\n':y='\n';break;
              }
     return y;
 }
 
 
int main()
{
    int T,t,i,j,k;
    char a[150];
    FILE *in,*out;
    in=fopen("C:/inputa.in","r");
    out=fopen("C:/outputa.txt","w");
    t=0;
    
    fscanf(in,"%d\n",&T);
    while(t++<T)
    {
                fgets(a,110,in);
                fprintf(out,"Case #%d: ",t);
                //printf("%s\n",a);
                for(i=0;a[i];i++)
                {fprintf(out,"%c",map(a[i]));}
                }
                
    fclose(in);
    fclose(out);
    //system("pause");
    return 0;
    
}
