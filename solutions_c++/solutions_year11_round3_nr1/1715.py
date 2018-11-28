#include<iostream>
#include <iomanip>
#include<vector>
#include<set>
#include<map>

using namespace std;
typedef vector<char> CharVec;
typedef vector<CharVec> CharVecVec;
typedef vector<long double> DblVec;

int main()
{
    int T;
    cin >> T;
   
    for(int n =0; n<T; ++n)
    {
       int R, C;
       cin >> R >>C; 
       CharVecVec tiles;    
       for(int i=0; i<R;++i)
       {
            CharVec t;   
            for(int j=0; j< C; ++j)
            {
                char c;    
                cin>> c;
                t.push_back(c);    
            }
            tiles.push_back(t);   
       }
       
       
       bool bpos = true;      
       for(int i=0; i<R;++i)
       {   
            for(int j=0; j< C; ++j)
            {
                if(tiles[i][j] == '#')
                {
                   if(j+1<C && tiles[i][j+1]=='#') 
                   {}
                   else {bpos =false; break; }   
                   if(i+1<R && tiles[i+1][j]=='#' && tiles[i+1][j+1]=='#')
                   {                         
                   }
                   else {bpos =false; break; }   
                   tiles[i+1][j]=  '\\'; tiles[i+1][j+1]=  '/';   
                   tiles[i][j] = '/';    
                   tiles[i][j+1] = '\\'; 
                }          
            }
            if(!bpos) break;
       }
       
       cout << "Case #" <<n+1<<":" <<"\n" ;
       if(!bpos)      
          cout << "Impossible" <<"\n";
       else     
       { 
         for(int i=0; i<R;++i)
           {   
                for(int j=0; j< C; ++j)
                {
                    cout<<  tiles[i][j];         
                }
                cout<<"\n";
           }
       }
       
    }
    
}
