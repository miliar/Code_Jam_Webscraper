#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
main()
{
      FILE *fp_in, *fp_out;
      char ch_in, ch_out;
      char ch_an[3];
      int i = 1 , j=0;
      fp_in = fopen("file_input.txt","r");
      fp_out = fopen("file_out.txt","w");
      while ((ch_in = fgetc(fp_in)) !='\n'){
            fgetc(fp_in);
            
      }
      fprintf(fp_out, "Case #%d: ",i);
      i++;
      while ((ch_in = fgetc(fp_in)) != EOF)
      {
            switch(ch_in){
                        case ' ':
                             fputc(ch_in,fp_out);
                             break;
                        case '\n':
                             if(i == 31 )
                                  break;
                             fputc(ch_in,fp_out);
                             fprintf(fp_out, "Case #%d: ",i);
                             i++;
                             break;
                        case 'a': ch_out = 'y';
                             fputc(ch_out,fp_out);
                             break;
                        case 'b': ch_out = 'h';
                             fputc(ch_out,fp_out);
                             break;
                        case 'c': ch_out = 'e';
                             fputc(ch_out,fp_out);
                             break;
                        case 'd': ch_out = 's';
                             fputc(ch_out,fp_out);
                             break;
                        case 'e': ch_out = 'o';
                             fputc(ch_out,fp_out);
                             break;
                        case 'f': ch_out = 'c';
                             fputc(ch_out,fp_out);
                             break;
                        case 'g': ch_out = 'v';
                             fputc(ch_out,fp_out);
                             break;
                        case 'h': ch_out = 'x';
                             fputc(ch_out,fp_out);
                             break;
                        case 'i': ch_out = 'd';
                             fputc(ch_out,fp_out);
                             break;
                        case 'j': ch_out = 'u';
                             fputc(ch_out,fp_out);
                             break;
                        case 'k': ch_out = 'i';
                             fputc(ch_out,fp_out);
                             break;
                        case 'l': ch_out = 'g';
                             fputc(ch_out,fp_out);
                             break;
                        case 'm': ch_out = 'l';
                             fputc(ch_out,fp_out);
                             break;
                        case 'n': ch_out = 'b';
                             fputc(ch_out,fp_out);
                             break;
                        case 'o': ch_out = 'k';
                             fputc(ch_out,fp_out);
                             break;
                        case 'p': ch_out = 'r';
                             fputc(ch_out,fp_out);
                             break;
                        case 'q': ch_out = 'z';
                             fputc(ch_out,fp_out);
                             break;
                        case 'r': ch_out = 't';
                             fputc(ch_out,fp_out);
                             break;
                        case 's': ch_out = 'n';
                             fputc(ch_out,fp_out);
                             break;
                        case 't': ch_out = 'w';
                             fputc(ch_out,fp_out);  
                             break;
                        case 'u': ch_out = 'j';
                             fputc(ch_out,fp_out);
                             break;
                        case 'v': ch_out = 'p';
                             fputc(ch_out,fp_out);
                             break;
                        case 'w': ch_out = 'f';
                             fputc(ch_out,fp_out);
                             break;
                        case 'x': ch_out = 'm';
                             fputc(ch_out,fp_out);
                             break;
                        case 'y': ch_out = 'a';
                             fputc(ch_out,fp_out);
                             break;
                        case 'z': ch_out = 'q';
                             fputc(ch_out,fp_out);
                             break;
                        default:
                                break;
                        }
            }
            getch();
            fclose(fp_in);
            fclose(fp_out);
      }
