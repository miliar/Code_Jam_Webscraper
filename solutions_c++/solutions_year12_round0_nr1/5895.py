#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
    char ch;
    char j;
    int t=0,k=1,k2=0;

   
    FILE *fr,*fw;
    fr = fopen("A-small-attempt10.in","r");
    fw= fopen("A-small-attempt.out","w");
while(ch!=EOF)
     {   
       
          j= getc(fr);
             
           switch(j)
           {
                case 97: fputc('y',fw);
                  break;
                  case 98: fputc('h',fw);  
                           break;
                  case 99: fputc('e',fw);
                           break;
                  case 100: fputc('s',fw);
                    break;
                  case 101: fputc('o',fw);
                  break;
                  case 102: fputc('c',fw);
                  break;
                  case 103: fputc('v',fw);
                  break;
                  case 104: fputc('x',fw);
                                    break;
                  case  105: fputc('d',fw);
                  break;
                  case 106: fputc('u',fw);
                  break;
                  case 107: fputc('i',fw);
                                    break;
                  case 108: fputc('g',fw);
                  break;
                  case 109: fputc('l',fw);
                  break;
                  case 110: fputc('b',fw);
                  break;
                  case 111: fputc('k',fw);
                  break;
                  case 112: fputc('r',fw);
                  break;
                  case 113: fputc('z',fw);
                  break;
                  case 114: fputc('t',fw);
                  break;
                  case 115: fputc('n',fw);
                  break;
                  case 116: fputc('w',fw);
                  break;
                  case 117: fputc('j',fw);
                  break;
                  case 118: fputc('p',fw);
                  break;
                  case 119: fputc('f',fw);
                  break;
                  case 120: fputc('m',fw);
                  break;
                  case 121: fputc('a',fw);
                  break;
                  case 122: fputc('q',fw);
                  break;
                  case 32: fputc(' ',fw);
                         break;          
           }
          
           if(j=='\n')
           {
                       if(k==31)
           break;
           if(k>=2)
            fprintf(fw,"\nCase #%d: ",k++);
            else
           fprintf(fw,"Case #%d: ",k++);
            
           }
     }
  
          
          fclose(fr);
          fclose(fw);

      getch();
            return 0;
}
