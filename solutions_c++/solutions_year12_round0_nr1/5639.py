#include<iostream>
#include<fstream>
using namespace std;
void func( char *s);
int main(int argc,char* argv[]){
    char s[105];
    int count=1,max=0;
    FILE *fp1,*fp2;
    fp1=fopen("A-small-attempt0 (4).in","r");
    fp2=fopen("target1.txt","w+");
    if(fp1==NULL){
                 printf("\nFile not exists\n");
    }
    while(fgets(s,104,fp1)){
        if(max==0){
           max=atoi(s);
           continue;
        }
        func(s);
        char temp[105];
        sprintf(temp,"Case #%d: %s",count,s);
        fputs(temp,fp2);
        count++;
        if(count>max)
            break;
    }
    fclose(fp1);
    fclose(fp2);
    system("pause");
    return 0;
}

    
void func( char *s)
{

     while(*s!='\0')
     {
                              switch(*s)
                              {
                                             
                                             
                                             case 'a': *s='y';
                                             break;
                                             case 'b': *s='h';
                                             break;
                                             case 'c': *s='e';
                                             break;
                                             case 'd': *s='s';
                                             break;
                                             case 'e': *s='o';
                                             break;
                                             case 'f': *s='c';
                                             break;
                                             case 'g': *s='v';
                                             break;
                                             case 'h': *s='x';
                                             break;
                                             case 'i': *s='d';
                                             break;
                                             case 'j': *s='u';
                                             break;
                                             case 'k': *s='i';
                                             break;
                                             case 'l': *s='g';
                                             break;
                                             case 'm': *s='l';
                                             break;
                                             case 'n': *s='b';
                                             break;
                                             case 'o': *s='k';
                                             break;
                                             case 'p': *s='r';
                                             break;
                                             case 'q': *s='z';
                                             break;
                                             case 'r': *s='t';
                                             break;
                                             case 's': *s='n';
                                             break;
                                             case 't': *s='w';
                                             break;
                                             case 'u': *s='j';
                                             break;
                                             case 'v': *s='p';
                                             break;
                                             case 'w': *s='f';
                                             break;
                                             case 'x': *s='m';
                                             break;
                                             case 'y': *s='a';
                                             break;
                                             case 'z': *s='q';
                                             break;
                                                   
                                             
                              }              
                              ++s;   
             }
             }
            
     
