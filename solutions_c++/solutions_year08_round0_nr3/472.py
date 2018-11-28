#include <stdio.h>
#include <conio.h>
//#include <ctype.h>
#include <math.h>
//#include <stdlib.h>



/*


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


*/


float areaSq(float bot, float top, float left, float right)
{
      return (right-left) * (top-bot);
}

float areaTr(float b, float h)
{
      return b * h / 2.0;
}

float areaSg(float x2, float y2, float x1, float y1, float R)
{
      float c2 = atan(y2/x2);
      float c1 = atan(y1/x1);
      
      float c = c2 - c1;
      
      return  ( pow(R,2) / 2.0 ) * ( c - sin(c) );
}



int main(void)
{

   int N;
   float f, R, t, r, g;

  
   FILE *in, *out, *deb;

   char inPath[40] = "c:\\GJam\\C-small.in";
   char outPath[40] = "c:\\GJam\\C-small.out";
  // char inPath[40] = "c:\\GJam\\C-test.in";
   //char outPath[40] = "c:\\GJam\\C-test.out";

   char debPath[40] = "c:\\GJam\\C-deb.out";


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

       fscanf( in, "%f", &f);
       fscanf( in, "%f", &R);
       fscanf( in, "%f", &t);
       fscanf( in, "%f", &r);
       fscanf( in, "%f", &g);

       float areaT = M_PI * R * R;
       float areaV = 0;
       
       
       fprintf(deb, "Cas %i : \n", n+1);
       
       fprintf(deb, "f: %f\nR: %f\nt: %f\nr: %f\ng: %f\n", f, R, t, r, g);
       
       if (g > (2*f))      // no hi ha espai suficient perquè la mosca passi pel forat
       {
           float areaInc = 0.0;
           
           R = R - t - f;
               
           float ds = 2*r + g;
           
           
           fprintf(deb, "ds %f : \n\n", ds);
                 
           for (float y=0; y<R; y += ds)
           {
               float bot = y + r + f;
               float top = y + r + g - f;
               
               float limBot = sqrt(pow(R,2) - pow(bot,2));
               float limTop = sqrt(pow(R,2) - pow(top,2));
               
               
               for (float x=0; x<R; x+= ds)
               {
                   float left = x + r + f;
                   float right = x + r + g - f;
                   
                   float limLeft = sqrt(pow(R,2) - pow(left,2));
                   float limRight = sqrt(pow(R,2) - pow(right,2));
                   
                   if (pow(bot,2) + pow(left,2) > pow(R,2)) /// tot el quadre fora el cercle
                   {
                         areaInc = 0;
                         
                         areaV += areaInc;

                         fprintf(deb, "  Quadre (%f,%f) : tipus 0 \n", x, y);
                         fprintf(deb, "                       Area valida %f (increment %f) \n", areaV, areaInc);
                   }
                   else if (pow(top,2) + pow(right,2) < pow(R,2)) /// tot el quadre dins el cercle
                   {
                         areaInc = areaSq(bot, top, left, right);                             

                         areaV += areaInc;
                                 
                         fprintf(deb, "  Quadre (%f,%f) : tipus 1 \n", x, y);
                         fprintf(deb, "                       Area valida %f (increment %f) \n", areaV, areaInc);
                   } 
                   else // vèrtex superior dret fora el cercle
                   {
                         if (pow(bot,2) + pow(right,2) < pow(R,2)) /// vèrtex inferior dret dins del cercle
                         {
                                if (pow(top,2) + pow(left,2) < pow(R,2)) /// vèrtex superior esquerre dins del cercle
                                {
                                    areaInc = areaSq(bot, top, left, limTop);
                                    
                                    areaInc += areaSq(bot, limRight, limTop, right);
                                    
                                    areaInc += areaTr(right - limTop, top - limRight);
                                    
                                    areaInc += areaSg(limTop, top, right, limRight, R);

                                    areaV += areaInc;
                                            
                                    fprintf(deb, "  Quadre (%f,%f) : tipus 2 \n", x, y);
                                    fprintf(deb, "                       Area valida %f (increment %f) \n", areaV, areaInc);
                                }   
                                else  // vertex inferiors dins el cercle
                                {
                                    areaInc = areaSq(bot, limRight, left, right);
                                    
                                    areaInc += areaTr(right - left, limLeft - limRight);
                                    
                                    areaInc += areaSg(left, limLeft, right, limRight, R);
                                    
                                    areaV += areaInc;
                                    
                                    fprintf(deb, "  Quadre (%f,%f) : tipus 3 \n", x, y);           
                                    fprintf(deb, "                       Area valida %f (increment %f) \n", areaV, areaInc);                                                            
                                }
                         }
                         else   /// vèrtex inferior dret fora del cercle
                         {
                                if (pow(top,2) + pow(left,2) < pow(R,2)) /// vèrtex superior esquerre dins del cercle (esquerres dins dretes fora)
                                {
                                    areaInc = areaSq(bot, top, left, limTop);
                                    
                                    areaInc += areaTr(limBot - limTop, top - bot);
                                    
                                    areaInc += areaSg(limTop, top, limBot, bot, R);
                                    
                                    areaV += areaInc;
                                    
                                    fprintf(deb, "  Quadre (%f,%f) : tipus 4 \n", x, y);           
                                    fprintf(deb, "                       Area valida %f (increment %f) \n", areaV, areaInc);                                                            
                                }   
                                else  // vertex inferior esquerre dins el cercle (resta fora)
                                {
                                    areaInc = areaTr(limBot - left, limLeft - bot);
                                    
                                    areaInc += areaSg(left, limLeft, limBot, bot, R);
                                    
                                    areaV += areaInc;
                                    
                                    fprintf(deb, "  Quadre (%f,%f) : tipus 5 \n", x, y);        
                                    //fprintf(deb, "      %f %f %f %f   \n", left, right, bot, top);
                                    //fprintf(deb, "      %f %f %f %f   \n", limLeft, limRight, limBot, limTop);
                                    fprintf(deb, "                       Area valida %f (increment %f) \n", areaV, areaInc);                                
                                }
                         }
                         
                   }   // end if 
                   
                   
               }  // end x for
           } // end y for               

            
       } // end  if (g ... 



       /*
       printf( "\n - Número de buscadors %i:\n", S);
       fprintf( deb, "\n - Número de buscadors %i:\n", S);
       for(int s=0; s<S; s++)
       {
          printf( "%i %s\n", s, search[s]);
          fprintf( deb, "%i %s\n", s, search[s]);          
       }

       printf( "\n - Número de cerques %i:\n", Q);
       fprintf( deb, "\n - Número de cerques %i:\n", Q);
       for(int q=0; q<Q; q++)
       {
          printf( "%i %s\n", q, queries[q]);
          fprintf( deb, "%i %s\n", q, queries[q]);
        }
       
       
       //// Solution ////////////////////////////////////////////////////////


       */
       
       float P = 1 - ( (areaV*4) / areaT );

       fprintf(out, "Case #%i: %f\n", n+1, P);

       fprintf(deb, "\n  ------------------ SOLUCIO %f --------------------- \n\n ", P); 

   } // end N for
       


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

   if( fclose(deb) )
   {
      printf( "Error\n" );
      return 1;
   }


   getch();

   
   return 0;
  
      
}


