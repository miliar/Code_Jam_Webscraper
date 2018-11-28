
#include <conio.h>
#include <stdio.h>
#include <math.h>

char mapping[26] = {'y',//a
                    'h',//b
                    'e',//c
                    's',//d
                    'o',//e
                    'c',//f
                    'v',//g
                    'x',//h
                    'd',//i
                    'u',//j
                    'i',//k
                    'g',//l
                    'l',//m
                    'b',//n
                    'k',//o
                    'r',//p
                    'z',//q
                    't',//r
                    'n',//s
                    'w',//t
                    'j',//u
                    'p',//v
                    'f',//w
                    'm',//x
                    'a',//y
                    'q',//z
                    };


int main() {
//	freopen("b.in", "r", stdin);

//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);

    FILE *fpI = fopen("A-small-attempt1.in", "r");
    FILE *fpO = fopen("A-large.out", "w+");
    
    char c;
    unsigned int T;
    int count = 0;
    
    if (NULL == fpI)
    {
             printf("NULL1\n");
             getch();
             return -1;
    }
    
    if (NULL == fpO)
    {
             printf("NULL2\n");
             getch();
             return -1;
    }
    
    fscanf(fpI, "%d", &T);
    printf("%d\n", T);
  
    fgetc(fpI);
  
   if ( T >= 1)
   {
       fprintf(fpO, "Case #%d: ", 1);
   }
   
	while(feof(fpI) == 0)
	{
            c = getc(fpI);
            printf("%c", c);
            if (c == '\n')
            {
                   count++;

                   if ( count < T)
                   {
                        putc(c, fpO);
                        fprintf(fpO, "Case #%d: ", count + 1);
                   }
            }
            else if (c == ' ')
            {
                 putc(c, fpO);
            }
            else if (c >= 'a' && c <= 'z')
            {
                 putc(mapping[c - 'a'], fpO);
            }
            //fprintf(fpO, "Case #%d: %d\n", (i+1), Ans); 
    }

	return 0;
}
