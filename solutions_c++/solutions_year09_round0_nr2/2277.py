#include<iostream>
#include<queue>
using namespace std;


int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };

int flow[100][100];
char polje[100][100];

int h, w;
char novo;
bool change;

void rek ( int x, int y, char slovo ) {
      
      if( polje[x][y] != slovo && polje[x][y] != '.' && !change ){
          change = true; novo = polje[x][y]; return;
      }
      
      if( polje[x][y] == slovo )return;
      
      polje[x][y] = slovo;
      
      int Min = flow[x][y], x2 = x, y2 = y, xx, yy;
      
      for( int i = 0; i < 4; i++ ) {
          xx = x + dx[i], yy = y + dy[i];
          if( xx < 0 || xx >= h || yy < 0 || yy >= w )continue;
          if( flow[xx][yy] < Min ) { 
              Min = flow[xx][yy];
              x2 = xx, y2 = yy;
          }
      }

      rek( x2, y2, slovo );

};



int main(){
    
    freopen( "ulaz.txt", "r", stdin );
    freopen( "sol.txt", "w", stdout );
    
    int t;
    scanf("%d", &t );
    
    for( int c = 1; c <= t; c++ ){
           
         scanf("%d %d", &h, &w );
         
         for( int i=0; i < h; i++ )
           for( int j=0; j < w; j++ ){
             scanf("%d", &flow[i][j] );
             polje[i][j] = '.';
           }
         
         char slovo = 'a'-1;
          
         for( int i=0; i < h; i++ )
            for( int j=0; j < w; j++ ){
               if( polje[i][j] == '.'){
   
                      ++slovo; change = false;
                      rek( i, j, slovo );
                      
                      if( change ) { 
                          rek( i, j, novo ); -- slovo;
                      }  
                 }
            }
         
         cout << "Case #" <<c<<":"<<endl;  
         for(int i=0; i < h; i++ ){
            for(int j=0; j < w; j++ )cout << polje[i][j] << " ";
            cout << endl;
         }            
    }  
                            
    return 0;
}   
                                      
