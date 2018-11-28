#include <stdio.h>
#include <conio.h>
//#include <ctype.h>
//#include <math.h>
//#include <stdlib.h>



#define n_max 30
#define m_max 30

int N, S, Q;
char search[100][50];
char queries[1000][50];

int nextS[100];
int position;
int changes;
int actual;





int readLine(FILE* f, char* a)
{
    int i=0;
    char c;
    
    do 
    {
        fscanf(f, "%c", &c);
        a[i] = c; 

        i++;

    } while (c!='\n');
    
    i--;
    a[i] = '\0';
    
    return i;
}



int equal(char *a, char *b)
{
     int i=0;
     
     while ( ! (a[i]!=b[i] || (a[i]=='\0' && b[i]=='\0')) )
     {
           i++;
     } 
    
     return (a[i]=='\0' && b[i]=='\0');
}


int main(void)
{

    
  
   FILE *in, *out, *deb;

   char inPath[40] = "c:\\GJam\\A-large.in";
   char outPath[40] = "c:\\GJam\\A-large.out";

//   char inPath[40] = "c:\\GJam\\A-small.in";
//   char outPath[40] = "c:\\GJam\\A-small.out";
 //  char inPath[40] = "c:\\GJam\\A-test.in";
 //  char outPath[40] = "c:\\GJam\\A-test.out";

   char debPath[40] = "c:\\GJam\\A-deb.out";



   char c;


   in = fopen( inPath, "r" );
  
   if( !in )
   {
      printf( "Error\n" );
      return 1;
   }

   out = fopen( outPath, "w" );

   if( !out )
   {
      printf( "Error\n" );
      return 1;
   }

   deb = fopen( debPath, "w" );

   if( !deb )
   {
      printf( "Error\n" );
      return 1;
   }


   fscanf( in, "%i", &N);

   for(int n=0; n<N; n++)
   {

       fscanf( in, "%i", &S);
  
       fscanf( in, "%c", &c);

       for(int s=0; s<S; s++)
       {
          //fscanf( in, "%s", search[s]);
          readLine( in, search[s]);
        
       }

       fscanf( in, "%i", &Q);

       fscanf( in, "%c", &c);

       for(int q=0; q<Q; q++)
       {
          readLine( in, queries[q]);
        
       }
       

       //printf( "\n - Número de buscadors %i:\n", S);
       fprintf( deb, "\n - Número de buscadors %i:\n", S);
       for(int s=0; s<S; s++)
       {
          //printf( "%i %s\n", s, search[s]);
          fprintf( deb, "%i %s\n", s, search[s]);          
       }

       //printf( "\n - Número de cerques %i:\n", Q);
       fprintf( deb, "\n - Número de cerques %i:\n", Q);
       for(int q=0; q<Q; q++)
       {
          //printf( "%i %s\n", q, queries[q]);
          fprintf( deb, "%i %s\n", q, queries[q]);
        }
       
       
       //// Solution ////////////////////////////////////////////////////////
       
       
//       printf("\n\n---------------------------------------------- \n");
       
       position = 0;
       changes = 0;
       actual = -1;
       

       while ( position < Q )
       {

           int max = 0;
                    
           for(int s=0; s<S; s++)
           {
                int q = 0;
                                
                while ( !equal(search[s], queries[position+q]) && (position+q)!= Q)
                {
                  q++;
                }
                   
                if (q > max && actual != s) 
                {  
                      max = q;
                      actual = s;
                }
                
                //nextS[s] = q;
           }

           position += max;
                    
           changes++;
           
           //printf(" Salt de %i cerques, posicio %i \n", max, position);
           fprintf(deb, " Salt de %i cerques, posicio %i \n", max, position);
       }
       
       if (changes>0) changes--;
       


       fprintf(out, "Case #%i: %i\n", n+1, changes);


/*       printf("\n\n Propera cerca \n");
       for(int s=0; s<S; s++)
       {
            printf("%s    %i\n", search[s], nextS[s]);
       }      
*/

   //    printf("\n\n------------- changes : %i --------------------------------- \n", changes);
       fprintf(deb, "\n\n------------- changes : %i --------------------------------- \n", changes);

   }
       


   if( fclose(in) )
   {
      printf( "Error\n" );
      return 1;
   }

   if( fclose(out) )
   {
      printf( "Error\n" );
      return 1;
   }



   getch();

   
   return 0;
  
      
}


