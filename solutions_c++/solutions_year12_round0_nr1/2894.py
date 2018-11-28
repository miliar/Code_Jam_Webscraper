#include<stdio.h>
#include<iostream>
using namespace std;

main()
{
    FILE * fi=fopen("input.txt","r");
    FILE * fo=fopen("output.txt","w");
    int T;
    char read_line[110];
    fscanf(fi,"%d\n",&T);
    for(int line=0;line<T;line++)
    {
        fprintf(fo,"Case #%d: ",line+1);
       fgets(read_line,110,fi);
       int j=0;
       while(read_line[j]!='\n')
       {

           switch(read_line[j])
           {
                case 'a':
                        fprintf(fo,"%c",'y');
                        break;
                case 'b':
                        fprintf(fo,"%c",'h');
                        break;
                case 'c':
                        fprintf(fo,"%c",'e');
                        break;
                case 'd':
                        fprintf(fo,"%c",'s');
                        break;
                case 'e':
                        fprintf(fo,"%c",'o');
                        break;
                case 'f':
                        fprintf(fo,"%c",'c');
                        break;
                case 'g':
                        fprintf(fo,"%c",'v');
                        break;
                case 'h':
                        fprintf(fo,"%c",'x');
                        break;
                case 'i':
                        fprintf(fo,"%c",'d');
                        break;
                case 'j':
                        fprintf(fo,"%c",'u');
                        break;
                case 'k':
                        fprintf(fo,"%c",'i');
                        break;
                case 'l':
                        fprintf(fo,"%c",'g');
                        break;
                case 'm':
                        fprintf(fo,"%c",'l');
                        break;
                case 'n':
                        fprintf(fo,"%c",'b');
                        break;
                case 'o':
                        fprintf(fo,"%c",'k');
                        break;
                case 'p':
                        fprintf(fo,"%c",'r');
                        break;
                 case 'q':
                        fprintf(fo,"%c",'z');
                        break;
                case 'r':
                        fprintf(fo,"%c",'t');
                        break;
                case 's':
                        fprintf(fo,"%c",'n');
                        break;
                case 't':
                        fprintf(fo,"%c",'w');
                        break;
                 case 'u':
                        fprintf(fo,"%c",'j');
                        break;
                case 'v':
                        fprintf(fo,"%c",'p');
                        break;
                case 'w':
                        fprintf(fo,"%c",'f');
                        break;
                case 'x':
                        fprintf(fo,"%c",'m');
                        break;
                 case 'y':
                        fprintf(fo,"%c",'a');
                        break;
                case 'z':
                        fprintf(fo,"%c",'q');
                        break;
                case ' ':
                        fprintf(fo,"%c",' ');
                        break;

           }
           j++;
       }
       fprintf(fo,"\n");
    }
    fclose(fo);
    fclose(fi);
}
