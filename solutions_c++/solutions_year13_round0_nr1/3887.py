#include <iostream>

using namespace std;

char board[4][4];

int hori(const int Case, const int i)
{
    char a;
    if( board[i][0] == 'T')
        a = board[i][1];
    else
        a = board[i][0];
        
    if( a == '.')
       return 0;
				
    int j=1;
    for ( ; j<4; ++j)
        if ( !((a == board[i][j]) || ('T' == board[i][j]) ) )
           break;
    if(j==4)
    {
      printf("Case #%d: %c won\n",Case, a);
      return 1;
      }
    return 0;     
}

int vert(const int Case, const int j)
{
    char a; 
    if( board[0][j] == 'T')
        a = board[1][j];
    else
        a = board[0][j];
        
    if( a == '.')
       return 0;
        
    int i=1;
    for ( ; i<4; ++i)
        if ( !((a == board[i][j]) || ('T' == board[i][j]) ) )
           break;
    if(i==4)
    {
      printf("Case #%d: %c won\n",Case, a);
      return 1;
      }
    return 0;     
}

int dia1(const int Case)
{
    char a; 
    if( board[0][0] == 'T')
        a = board[1][1];
    else
        a = board[0][0];
        
    if( a == '.')
       return 0;
        
    int i=1,j=1;
    for ( ; i<4; ++i, ++j)
        if ( !((a == board[i][j]) || ('T' == board[i][j]) ) )
           break;
    if(i==4)
    {
      printf("Case #%d: %c won\n",Case, a);
      return 1;
      }
    return 0;     
}

int dia2(const int Case)
{
    char a; 
    if( board[0][3] == 'T')
        a = board[1][2];
    else
        a = board[0][3];
        
    if( a == '.')
       return 0;
        
    int i=1,j=2;
    for ( ; i<4; ++i, --j)
        if ( !((a == board[i][j]) || ('T' == board[i][j]) ) )
           break;
    if(i==4)
    {
      printf("Case #%d: %c won\n",Case, a);
      return 1;
      }
    return 0;     
}

int draw(const int Case)
{
    for ( int i=0; i<4; ++i)
       for (int j=0; j<4; ++j)
         if ( board[i][j] == '.' )
           return 0;           
           
    printf("Case #%d: Draw\n",Case);
    return 1;     
}

int main(int argc, char *argv[])
{
    int T, Case = 0, i, j;
    char a;    
    scanf("%d\n", &T);
    do
    {
       for(i=0; i<4 ; ++i)
       {
           for(j=0; j<4; ++j)
           {
              scanf("%c",&board[i][j]);
              //printf("%c",board[i][j]);
              }
           scanf("%c\n", &a);
           //printf("\n");
       } 
      if( hori(++Case,0) )
        continue;
      else if( hori(Case,1) )
        continue;
      else if( hori(Case,2) )
        continue;
      else if( hori(Case,3) )
        continue;
      else if( vert(Case,0) )
        continue;
      else if( vert(Case,1) )
        continue;
      else if( vert(Case,2) )
        continue;
      else if( vert(Case,3) )
        continue;
      else if( dia1(Case) )
        continue;
      else if( dia2(Case) )
        continue;
      else if ( draw(Case) )
        continue;
      else 
        printf("Case #%d: Game has not completed\n",Case, a);      
        
    }while(--T);
}
