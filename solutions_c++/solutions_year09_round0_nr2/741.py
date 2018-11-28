#include <iostream>
#include <cstring>

#define MAX_T 100
#define MAX_H 100
#define MAX_W 100

using namespace std;

int T; //Test case number

int H; //Map height
int W; //Map width

FILE *fin = fopen("B-small.in", "r");
FILE *fout = fopen("result.txt", "w");

int map[MAX_H][MAX_W]; //Store map in memory

int components[MAX_H][MAX_W]; //Component (basin) array
int componentCount;  //Component count

struct coords
{
   int x, y;
};

bool squareExist(coords curr)
{
   if ((curr.x < 0) || (curr.x >= H)) return false; //There is no square here
   if ((curr.y < 0) || (curr.y >= W)) return false; //Also
   
   return true;
}
int getElevation(coords curr)
{
   if (!squareExist(curr)) return -1;
   
   return map[curr.x][curr.y];
}

coords getPourDownCoords(coords start)
{
   int currElevation = getElevation(start);
   
   coords neighbourCoords[4];
   neighbourCoords[0].x = start.x-1;
   neighbourCoords[0].y = start.y;
   
   neighbourCoords[1].x = start.x;
   neighbourCoords[1].y = start.y-1;
   
   neighbourCoords[2].x = start.x;
   neighbourCoords[2].y = start.y+1;
   
   neighbourCoords[3].x = start.x+1;
   neighbourCoords[3].y = start.y;
   
   
   int neighbourElevation[4];
   neighbourElevation[0] = getElevation(neighbourCoords[0]); //North
   neighbourElevation[1] = getElevation(neighbourCoords[1]); //West
   neighbourElevation[2] = getElevation(neighbourCoords[2]); //East
   neighbourElevation[3] = getElevation(neighbourCoords[3]); //South
   
   //Fill water downwards
   int pourDownTo = -1;
   int pourDownValue = currElevation;
   
   for (int i =0; i < 4; i++)
   {
      if ((neighbourElevation[i] < pourDownValue) && (neighbourElevation[i] > -1)) 
      {
         pourDownTo = i;
         pourDownValue = neighbourElevation[i];
      }
   }
   
   coords tmp;
   
   //Ohere we set return val.
   if (pourDownTo == -1) 
   {
      tmp.x = -1;
      tmp.y = -1;
   }
   else tmp = neighbourCoords[pourDownTo];
   
   return tmp;
}
void fillRecursively(coords start, int newComponent)
{
    //Get current elevation
   int currentElevation = getElevation(start);
   
   if (!squareExist(start)) return; //No such square
   
   //Assign to component
   if (components[start.x][start.y] > 0) return; // No need to double assign.
   
   components[start.x][start.y] = newComponent;
   
   coords neighbourCoords[4];
   neighbourCoords[0].x = start.x-1;
   neighbourCoords[0].y = start.y;
   
   neighbourCoords[1].x = start.x;
   neighbourCoords[1].y = start.y-1;
   
   neighbourCoords[2].x = start.x;
   neighbourCoords[2].y = start.y+1;
   
   neighbourCoords[3].x = start.x+1;
   neighbourCoords[3].y = start.y;
   
   //Fill downwards
   
   coords fillDownTo = getPourDownCoords(start);
   
   fillRecursively(fillDownTo, newComponent);
   
   //Try Fill Upwards
   
   for (int i=0; i < 4; i++)
   {
      coords tmpDownCoords = getPourDownCoords(neighbourCoords[i]);
      if ((tmpDownCoords.x == start.x) && (tmpDownCoords.y == start.y))
      {
         fillRecursively(neighbourCoords[i], newComponent);
      }
   }
}

void flood_fill ()
{
   memset(components, 0, sizeof(components)); //Unset components array from previous test case
   componentCount = 0; //There are no components yet.
   
   for (int i=0; i < H; i++)
   {
      for (int j=0; j < W; j++)
      {
         if (components[i][j] == 0) //We havent reached this one yet?
         {
            componentCount++; //This will be a new component
            
            coords tmp;
            tmp.x = i;
            tmp.y = j;
            
            fillRecursively(tmp, componentCount);
         }
      }
   }
}
void writeAnswer (int caseNo)
{
   char * alphabet = "abcdefghijklmnopqrstuvwxyz";
   
   fprintf(fout, "Case #%d:\n", caseNo+1);
   for (int i =0; i < H; i++)
   {
      for (int j=0; j < W; j++)
      {
         fprintf(fout, "%c", alphabet[components[i][j]-1]);
         
         if (j == W-1) fprintf(fout, "\n");
         else fprintf(fout, " ");
      }
   }
}

int main ()
{
   //----------------------------------------
   // Reading
   //----------------------------------------
   
   fscanf(fin, "%d\n", &T);
   for (int k = 0; k < T; k++)
   {
      memset(map, 0, sizeof(map)); //Clear our map.
      
      //Read the map
      
      fscanf(fin, "%d %d\n", &H, &W);
      
      for (int i=0; i < H; i++)
      {
         for (int j=0; j < W; j++)
         {
            fscanf(fin, "%d", &map[i][j]);
         }
      }
      
      //Flood fill
      flood_fill();
      
      writeAnswer(k);
      
   }
  
   
   fclose(fin);
   fclose(fout);
   
   return 0;
}
