#include <stdio.h>
#include <conio.h>
//#include <ctype.h>
//#include <math.h>
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



typedef struct 
{
       int h;
       int m;
} time;


FILE *in, *out, *deb;

//----------------------------------------------------------------------------------

int fScanTime(FILE* f, time* t)
{
    char c1, c2;
    
    fscanf( f, "%c", &c1);
    fscanf( f, "%c", &c2);
    
    //printf("caracters: %c %c    valor: %i %i\n", c1, c2, c1-48, c2-48);
       
    t->h = (c1-48)*10 + (c2-48);
    
    fscanf( f, "%c", &c1); /// :
    
    fscanf( f, "%c", &c1);
    fscanf( f, "%c", &c2);
    
    t->m = (c1-48)*10 + (c2-48);
   
    fscanf( f, "%c", &c1);  /// espai o salt de línia

    return 0;
} 

int addTurnAroundTime(time *t, int T)
{
    t->m += T;
    
    if (t->m >= 60) 
    {
            t->h++;
            t->m = t->m - 60;
    }
    
    return 0;
}



int compTime(time t1, time t2)
{
    int comp = -999;

    if (t1.h<t2.h) comp = -1;
    else 
    {  
        if (t1.h>t2.h) comp = 1;
        else 
        {
            if (t1.h == t2.h) 
            {
                 if (t1.m<t2.m) comp = -1;
                 else
                 {
                    if (t1.m>t2.m) comp = 1;
                    else
                    {
                        if (t1.m == t2.m) comp = 0;             
                    }
                 }    
            }
        }
    }       
    
    return comp;
}


void copyTime(time *t1, time t2)
{
     t1->h = t2.h;
     t1->m = t2.m;
}

int getMinTime( time* timeTable , int n, time* minTime)
{
    int minI;
    
    minTime->h = 999; minTime->m = 999;
    
    
    for (int i=0; i<n; i++)
    {

       // fprintf(deb, "comparant   %i:%i  -  %i:%i  ---- > %i\n", timeTable[i].h, timeTable[i].m, 
       //                                                          minTime->h, minTime->m, compTime(timeTable[i],*minTime) );

        if ( compTime(timeTable[i],*minTime) < 0 )
        {
             copyTime(minTime, timeTable[i]);
             
             minI = i;
        }
    }

    return minI;
}


//---------------------------------------------------------------------------------------------------------------------------------------------------

int main(void)
{
    int N;
    
    
    int trAvA = 0, trAvB = 0;
    int trNeA = 0, trNeB = 0;
  
    int T;

    int nAB, nBA;
    
    time AB[101][2];
    time BA[101][2];
    
    int nDeptA, nArrB, nDeptB, nArrA;
    
    time deptA[101];
    time arrB[101];
    
    time deptB[101];
    time arrA[101];

  

   char c;

  
   char inPath[40] = "c:\\GJam\\B-large.in";
   char outPath[40] = "c:\\GJam\\B-large.out";

//   char inPath[40] = "c:\\GJam\\B-small.in";
//   char outPath[40] = "c:\\GJam\\B-small.out";
//  char inPath[40] = "c:\\GJam\\B-test.in";
   //char outPath[40] = "c:\\GJam\\B-test.out";

   char debPath[40] = "c:\\GJam\\B-deb.out";


   in = fopen( inPath, "r" );    if( !in )   {      printf( "Error\n" );      return 1;   }

   out = fopen( outPath, "w" );  if( !out )   {      printf( "Error\n" );      return 1;   }

   deb = fopen( debPath, "w" );   if( !deb )   {      printf( "Error\n" );      return 1;   }



   fscanf( in, "%i", &N);

   for(int n=0; n<N; n++)
   {

      trAvA = 0, trAvB = 0;
      trNeA = 0, trNeB = 0;
           

       nDeptA = 0, nArrB = 0, nDeptB = 0, nArrA = 0;

 //      printf("\n\nCAS : %i \n", n);

       fscanf( in, "%i", &T);
   //    printf("T : %i \n", T);

       fscanf( in, "%i", &nAB);
     
       fscanf( in, "%i", &nBA);

  //     printf("AB: %i BA: %i \n", nAB, nBA);
       
       fscanf(in, "%c", &c);
       
       for (int i=0; i<nAB; i++)
       {        
               //fScanTime( in, &AB[i][0]);    
               //fScanTime( in, &AB[i][1]);    

               fScanTime( in, &deptA[i]);    
               fScanTime( in, &arrB[i]);
               
               nDeptA++;
               nArrB++;
               
               addTurnAroundTime(&arrB[i], T);

               //printf("sortida: %i:%i arribada %i:%i\n", deptA[i].h, deptA[i].m, arrB[i].h, arrB[i].m);

               //printf("%i:%i %i:%i\n", AB[i][0].h, AB[i][0].m, AB[i][1].h, AB[i][1].m);
       }
       
       for (int i=0; i<nBA; i++)
       {
               fScanTime( in, &deptB[i]);    
               fScanTime( in, &arrA[i]);

               nDeptB++;
               nArrA++;
               
               addTurnAroundTime(&arrA[i], T);
               
               //fScanTime( in, &BA[i][0]);      
               //fScanTime( in, &BA[i][1]);      
               //printf("%i:%i %i:%i\n", BA[i][0].h, BA[i][0].m, BA[i][1].h, BA[i][1].m);
       }
       
       
       
      while (nDeptA>0 || nDeptB>0 || nArrA>0 || nArrB>0)
      {
            
            int p[4];
            time minTableTime[4];     
            
            int first;
            time firstT;
            
            p[0] = getMinTime( arrA , nArrA, &minTableTime[0]);
            p[1] = getMinTime( arrB , nArrB, &minTableTime[1]);

            p[2] = getMinTime( deptA , nDeptA, &minTableTime[2]);
            p[3] = getMinTime( deptB , nDeptB, &minTableTime[3]);

            first = getMinTime( minTableTime, 4, &firstT );
            
           // printf("    Temps min ----  ArrA: %i:%i ArrB: %i:%i   SortA: %i:%i SortB: %i:%i    \n", 
            //                                                                                  arrA[p[0]].h, arrA[p[0]].m,
             //                                                                                 arrB[p[1]].h, arrB[p[1]].m,
               //                                                                               deptA[p[2]].h, deptA[p[2]].m,
                 //                                                                             deptB[p[3]].h, deptB[p[3]].m  );


            
            switch (first)
            {
                   case 0: //printf("Arriba tren a estacio A a les %i:%i \n", arrA[p[first]].h, arrA[p[first]].m);
                   
                        trAvA++;

                        if (nArrA>1) copyTime(&arrA[p[first]], arrA[nArrA-1]);
                        nArrA--;
                        
                        break;
                    
                   case 1: //printf("Arriba tren a estacio B a les %i:%i \n", arrB[p[first]].h, arrB[p[first]].m);
                   
                        trAvB++;
                   
                        if (nArrB>1) copyTime(&arrB[p[first]], arrB[nArrB-1]);
                        nArrB--;
                        
                        break;
                        
                   case 2:// printf("Surt tren de estacio A a les %i:%i \n", deptA[p[first]].h, deptA[p[first]].m);
                   
                        if (trAvA>0) trAvA--; else trNeA++;
                   
                        if (nDeptA>1) copyTime(&deptA[p[first]], deptA[nDeptA-1]);
                        nDeptA--;
                        
                        break;

                   case 3: //printf("Surt tren de estacio B a les %i:%i \n", deptB[p[first]].h, deptB[p[first]].m);
                   
                        if (trAvB>0) trAvB--; else trNeB++;
                   
                        if (nDeptB>1) copyTime(&deptB[p[first]], deptB[nDeptB-1]);
                        nDeptB--;

                        break;
                   
            } 
            
            //printf("Trens Necessaris (A: %i B: %i) Disponibles (A: %i B:%i) \n\n", trNeA, trNeB, trAvA, trAvB);
            
      }
      


    
       
       
       //// Solution ////////////////////////////////////////////////////////


       
       
     

       fprintf(out, "Case #%i: %i %i\n", n+1, trNeA, trNeB);

      // fprintf(deb, "\n  ------------------ SOLUCIO  --------------------- \n\n "); 

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


