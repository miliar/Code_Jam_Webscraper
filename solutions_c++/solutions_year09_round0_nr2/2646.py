#include <iostream>
#include <fstream>

using namespace std;

class map
{
public:
  int** m;
  int h,w;
  map(int H, int W)
  { h = H; w = W;
    m = new int*[h]; 
    for( int i = 0 ; i < h; i++)
         m[i] = new int[w];
  }
  ~map()
  {
        for( int i = 0; i < h; i++)
             delete [] m[i];
        delete [] m;  
        }  
};

class answer
{
public:
       unsigned int** m;
       int h,w;
  answer(unsigned int H, unsigned int W)
  { h = H; w = W;
    m = new unsigned int*[h]; 
    for( int i = 0 ; i < h; i++)
         m[i] = new unsigned int[w];
    for( int j = 0 ; j < h; j++)
         for( int k = 0; k < w; k++)
              m[j][k] = 0;
  }
  ~answer()
  {
        for( int i = 0; i < h; i++)
             delete [] m[i];
        delete [] m; 
        }     
      
};

void swap( answer & a,int l, int s)
{
         for( int j = 0; j < a.h; j++)
         {
              for( int k = 0; k< a.w; k++)
              {
                   if(a.m[j][k] == l)
                       a.m[j][k] = s;
              }     
         }
}


int main(int argc, char* argv[])
{
	
	ifstream inputf( argv[1]);
	ofstream outputf("B-smallOut.out");
    int T;
    inputf>>T;
    for( int i = 0; i < T; i++)
    {
         int H,W;
         inputf>>H;
         inputf>>W;
         map m = map(H,W);
         answer a = answer(H,W);

         for( int j = 0; j < H; j++)
         {
              for( int k = 0; k< W; k++)
              {
                   inputf>>m.m[j][k];
              }     
         }
         
         a.m[0][0] = 1; 
         char current = 1;
         for( int j = 0; j < H; j++)
         {
              for( int k = 0; k< W; k++)
              {
                   
                   int min = m.m[j][k];
                   int jt = j;
                   int kt = k;
                   
                   if( j != 0 && m.m[j-1][k] < m.m[j][k] )
                   {
                       jt = j-1; min = m.m[j-1][k];
                   }
                   
                   if( k!= 0 && m.m[j][k-1] < min)
                   {
                       jt = j; kt = k-1; min = m.m[j][k-1];
                   }
                   
                   if( k!= W-1 && m.m[j][k+1] < min)
                   {
                       jt = j; kt = k+1; min = m.m[j][k+1];   
                   }
                  
                   if( j!=H-1 && m.m[j+1][k] < min )
                   {
                       jt = j+1; kt = k ; 
                   }
                  
                   
                   if( jt == j && kt == k && a.m[j][k]== 0)
                   {
                       a.m[j][k] = ++current; continue;
                   }
				  
				   if( a.m[j][k]== 0 && a.m[jt][kt] == 0)
				   {
					   a.m[j][k] = a.m[jt][kt] = ++current; continue;
				   }
                   
                   if( a.m[j][k] != 0 && a.m[jt][kt]== 0 )
                   {
                       a.m[jt][kt] = a.m[j][k]; continue;   
                   }

                   if( a.m[j][k] == 0 && a.m[jt][kt] != 0 )
                   {
                       a.m[j][k] = a.m[jt][kt]; continue;   
                   }
                   
                   if( a.m[j][k]!= 0 && a.m[jt][kt]!= 0 && a.m[j][k]!= a.m[jt][kt] )
                   {
                           if( a.m[j][k] < a.m[jt][kt] ) 
                               swap(a, a.m[jt][kt],a.m[j][k]);
                           else
                               swap(a, a.m[j][k], a.m[jt][kt] );
                   }
                   
              }     
         }

         bool ba[1001];
         for( int z = 0; z < 1001; z++)
              ba[z] = false;
         for( int j = 0; j < H; j++)
         {
              for( int k = 0; k< W; k++)
              {
                   ba[a.m[j][k]] = true; 
              }     
         }
         int prev = 1;
         for( int l = 1; l< 1001 ; l++)
         {
              if( ba[l] )
              {
				  if( l!= prev )
					swap(a,l,prev);
				  prev++;
              }
         }

         outputf<<"Case #"<<i+1<<":"<<endl;
         for( int j = 0; j < H; j++)
         {
              for( int k = 0; k< W; k++)
              {
                   outputf<<(char)(a.m[j][k]+96)<<" ";
              }   
              outputf<<endl;
         }
         
    }
    outputf.close();
    inputf.close();
	return 0;
}

