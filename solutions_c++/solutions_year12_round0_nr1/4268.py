#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
main()
{
      FILE *ifp, *ofp;
      char ich, och;
      char ach[3];
      int i = 1 , j=0;
      ifp = fopen("A-small-attempt1.in","r");
      ofp = fopen("outputfile.txt","w");
      while ((ich = fgetc(ifp)) !='\n'){
            fgetc(ifp);
            
      }
      fprintf(ofp, "Case #%d: ",i);
      i++;
      while ((ich = fgetc(ifp)) != EOF)
      {
            switch(ich){
                        case ' ':
                             fputc(ich,ofp);
                             //fputc(ofp, "%c" , ich);
                             break;
                        case '\n':
                             if(i == 31 )
                                  break;
                             fputc(ich,ofp);
                             fprintf(ofp, "Case #%d: ",i);
                             printf("case %d complete\n",i);
                             i++;
                             //fputc(ofp, "%c" , ich);
                             break;
                        case 'a': och = 'y';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'b': och = 'h';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'c': och = 'e';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'd': och = 's';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'e': och = 'o';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'f': och = 'c';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'g': och = 'v';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'h': och = 'x';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'i': och = 'd';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'j': och = 'u';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'k': och = 'i';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'l': och = 'g';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'm': och = 'l';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'n': och = 'b';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'o': och = 'k';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'p': och = 'r';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'q': och = 'z';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'r': och = 't';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 's': och = 'n';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 't': och = 'w';
                             fputc(och,ofp);  
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'u': och = 'j';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'v': och = 'p';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'w': och = 'f';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'x': och = 'm';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'y': och = 'a';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        case 'z': och = 'q';
                             fputc(och,ofp);
                             //fputc(ofp, "%c" , och);
                             break;
                        default:
                                break;
                        }
            }
            printf(" all cases are done\n");
            getch();
            fclose(ifp);
            fclose(ofp);
      }
