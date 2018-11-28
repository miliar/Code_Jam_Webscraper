#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
typedef long long I;
int arr[3][3];
int main ()
{
     set<vector<pair<int,int> > >  s;
     for( int i1 =0 ; i1<3; i1++) 
     for( int i2 =0 ; i2<3; i2++) 
     for( int i3 =0 ; i3<3; i3++) 
     for( int j1 =0 ; j1<3; j1++) 
     for( int j2 =0 ; j2<3; j2++) 
     for( int j3 =0 ; j3<3; j3++)
     {
          if( (i1 + i2 + i3 )%3 != 0 ) continue;
          if( (j1 + j2 + j3 )%3 != 0 ) continue;
          vector<pair<int, int> > v;
          v.push_back( make_pair( i1, j1 ) );
          v.push_back( make_pair( i2, j2 ) );
          v.push_back( make_pair( i3, j3 ) );
          sort( v.begin(), v.end() );
          s.insert( v );
     }
     vector<vector< pair<int,int> > > possible (s.begin(), s.end());
   /*  for( int i =0 ;i<possible.size(); i++)
     {
         for( int j =0 ; j<3; j++)
          cout<<" ( "<<possible[i][j].first<<" , "<<possible[i][j].second<<") ";    
          cout<<endl;
     }*/
     
 int tc ; 
 cin>>tc;
 for( int cse = 1; cse <=tc; cse ++)
 {
     I n , A, B , C , D , x0, y0, M, X, Y;
     cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
     vector<I> VX, VY; X = x0, Y = y0;
     VX.push_back( X );
     VY.push_back( Y );
   //  cout<<X<<" "<<Y<<endl;
     for( int i =1 ; i <n ; i++)
     {
          X = ( A * X + B ) % M;
          Y = ( C * Y + D ) % M;
        //  cout<<X<<" "<<Y<<endl;
          VX.push_back( X );
          VY.push_back( Y );
     }
     memset( arr, 0, sizeof arr);
     
     for( int i =0 ; i<n ;i++) 
     {
          I left = VX[i]%3;
          I right = VY[i]%3;
          arr[left][right] ++;     
     }
     
     I result = 0;
     for( int i =0 ; i<possible.size() ; i++)
     {
          int a[3][3]; memset( a , 0 , sizeof a );
          for ( int j =0 ; j<3; j++) 
           a[possible[i][j].first][possible[i][j].second] ++;
           
           int valid = 1; I cur = 1;
          for( int ii =0 ; ii<3; ii++)
           for ( int jj =0 ;jj<3 ; jj++)
            {
                 if( a[ii][jj] == 0 ) continue;
                 if( a[ii][jj] > arr[ii][jj] ) valid = 0;
                 switch ( a[ii][jj] )
                 {
                        case 1 : cur *= arr[ii][jj]; break;
                        case 2 : cur *= (arr[ii][jj] * (arr[ii][jj]-1) ) /2; break;
                        case 3 : cur *= (arr[ii][jj] * (arr[ii][jj]-1) * (arr[ii][jj]-2)) /6; break;        
                 }
            }     
            if( valid)
                result += cur;
     }
     cout<<"Case #"<<cse<<": "<<result<<endl;
 }
return 0;    
}
