#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

ifstream input;

bool empty = false;
char arr[5][5];
char token[10];

char result[4][25] ={"X won", "O won", "Draw", "Game has not completed"};

void gettoken(){
	int  i = 0 ;
	char c = input.get() ;
	/* Skip all spaces */
    
	while(!input.eof() && (c==' '|| c == '\n' || c == '\t' ))
		c=input.get();	
	while(c != ' ' && c != '\t' &&	c!= '\n' )
	{  	   
	   token[i++] = c;
	   if(c == '.')
       empty = true;
     c = input.get();
	   
	   if(input.eof())
		   break;
	}  token[i] = '\0';
	
}

int iswonh(int i)
{
  int x = 0, o = 0, t = 0;

  for(int j = 0;j<4;j++)
    {
      if(arr[i][j] == 'X' )
        x++;
      if(arr[i][j] == 'O' )
        o++;
      if(arr[i][j] == 'T' )
        t++;
   }

  if(x == 4 || (x == 3 && t == 1))
    return 0; 

  if(o == 4 || (o == 3 && t == 1))
    return 1;

  else
    return -1;
}

int iswonv(int i)
{
  int x = 0, o = 0, t = 0;

  for(int j = 0;j<4;j++)
    {
      if(arr[j][i] == 'X' )
        x++;
      if(arr[j][i] == 'O' )
        o++;
      if(arr[j][i] == 'T' )
        t++;
   }

  if(x == 4 || (x == 3 && t == 1))
    return 0; 

  if(o == 4 || (o == 3 && t == 1))
    return 1;

  else
    return -1;
}

int iswond1()
{
  int x = 0, o = 0, t = 0;

  for(int j = 0;j<4;j++)
    {
      if(arr[j][j] == 'X' )
        x++;
      if(arr[j][j] == 'O' )
        o++;
      if(arr[j][j] == 'T' )
        t++;
   }

  if(x == 4 || (x == 3 && t == 1))
    return 0; 

  if(o == 4 || (o == 3 && t == 1))
    return 1;

  else
    return -1;
}

int iswond2()
{
  int x = 0, o = 0, t = 0;
  int i=0,j=0;

  for(j = 0, i = 3; j < 4, i >= 0; j++, i--)
    {
      if(arr[j][i] == 'X' )
        x++;
      if(arr[j][i] == 'O' )
        o++;
      if(arr[j][i] == 'T' )
        t++;
   }

  if(x == 4 || (x == 3 && t == 1))
    return 0; 

  if(o == 4 || (o == 3 && t == 1))
    return 1;

  else
    return -1;
}



int solution()
{
  int sol = 0, l =0;
  for(int i = 0; i<4; i++)
     {
       l = iswonh(i); 
       if (l != -1)
          break;
     }
  
  sol = l;

  if(sol == -1)
  {
     for(int i = 0; i<4; i++)
        {
           l = iswonv(i); 
           if (l != -1)
             break;
        }
  
     sol = l;

  }


 if(sol == -1)
  {
      l = iswond1(); 
        
     sol = l;

  }

  
 if(sol == -1)
  {
      l = iswond2(); 
  
     sol = l;

  }


 if(sol == -1)
  {
    if(empty == false)
       sol = 2;
    if(empty == true)
       sol = 3;    
  
  }

  return sol;
}

int main()
{
    input.open("A-large.in", ios::in);
    int start, end;
    gettoken();
    int testCases = atoi(token);
    for(int i = 0; i<testCases; i++)
    {
      for (int k = 0; k < 4; k++)
      {
        gettoken();
        for(int j =0; j<4 ; j++)
          arr[k][j] = token[j];
        arr[k][4] = '\0';
      }
       
     cout<<"Case #"<<i+1<<": "<<result[solution()]<<"\n";

      empty = false; 
    }
    
	return 0;
}