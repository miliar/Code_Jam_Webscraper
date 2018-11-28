#include <iostream>
#include <stdlib.h>
using namespace std;

const unsigned LARGE=100000;

unsigned H=0, W=0;
unsigned *hts_p=NULL;
char *basins_p=NULL;
char curBasin='A';
unsigned lowestNb=LARGE;

#define hts(i,j) (hts_p)[(W*(i)+(j))]
#define basins(i,j) (basins_p)[(W*(i)+(j))]

char mark(unsigned, unsigned);

int main()
{
   unsigned numTest=0;

   cin >>  numTest;
   for (unsigned i=1; i<=numTest; i++)
   {
      cout << "Case #" << i << ":" << endl;
      curBasin='a';
      cin >> H >> W;
      unsigned size=H*W;
      unsigned hts[H][W];
      hts_p=&hts[0][0];

      for(unsigned j=0; j<size; j++)
        cin >> hts[j/W][j%W];

      char basins[H][W];
      basins_p=&basins[0][0];

      for(unsigned h=0; h<H; h++)
      for(unsigned w=0; w<W; w++)
         basins[h][w]='.';

      for(unsigned h=0; h<H; h++)
      for(unsigned w=0; w<W; w++)
       {
//        cout << h << ":" << w  << endl ;
          if (basins[h][w]=='.') mark(h,w);

       }
 /* 
      for(unsigned h=0; h<H; h++)
      {
       for(unsigned w=0; w<W; w++)
       {
        cout << hts(h,w) << " ";
       }
       cout << endl;
      }
*/
  
  
      for(unsigned h=0; h<H; h++)
       for(unsigned w=0; w<W; w++)
       {
        cout << basins[h][w];
        if (w==W-1) cout << endl;
        else cout << " ";
       }

   }
   return 0;
}

char mark(unsigned h, unsigned w)
{
  if (basins(h,w)!='.') return basins(h,w);

  lowestNb=LARGE;
//cout << "Marking " << h << "," << w << endl;

  if (h>0)
       if (lowestNb > hts(h-1,w) )
       { 
	 lowestNb=hts(h-1,w);
	 basins(h,w)='N'; 
       }

  if (w>0)
       if (lowestNb > hts(h,w-1) )
       { 
	 lowestNb=hts(h,w-1);
	 basins(h,w)='W'; 
       }

  if (w < W-1)
       if (lowestNb > hts(h,w+1)) 
       { 
	 lowestNb=hts(h,w+1);
	 basins(h,w)='E'; 
       }

  if (h < H-1)
       if (lowestNb > hts(h+1,w)) 
       { 
	 lowestNb=hts(h+1,w);
	 basins(h,w)='S'; 
       }


// cout << lowestNb << " " << basins[h][w] << endl;

   if (lowestNb>=hts(h,w)) 
   {
    basins(h,w) = curBasin;
//  cout << " New basin " << curBasin << endl;
    return curBasin++;
   }

// cout << " Water leaks to " << basins(h,w) << endl;
   switch (basins(h,w))
   {
      case 'N' : 
                 { basins(h,w)=mark(h-1,w);
//                 cout << " in basin " << basins(h,w) << endl;
                   return basins(h,w);
                 }
      case 'W' : 
                 { basins(h,w)=mark(h,w-1);
//                 cout << " in basin " << basins(h,w) << endl;
                   return basins(h,w);
                 }
      case 'S' :
                 { basins(h,w)=mark(h+1,w);
//                 cout << " in basin " << basins(h,w) << endl;
                   return basins(h,w);
                 }
      case 'E' :
                 { basins(h,w)=mark(h,w+1);
//                 cout << " in basin " << basins(h,w) << endl;
                   return basins(h,w);
                 }
   }   
   cout << "Error" << endl;
   exit (1);
}

