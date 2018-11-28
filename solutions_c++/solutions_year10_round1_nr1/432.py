#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
using namespace std;

int main()
{
    string ret[4];
    ret[0] = "Red";
    ret[1] = "Blue";
    ret[2] = "Neither";
    ret[3] = "Both";
    int t;
    cin>>t;
    int num = t;
    while(t--)
    {
      int n , k;
      cin>>n>>k;
      vector<string> init;
      vector<string> final;
      init.resize(n);
      final.resize(n);
      for(int i = 0 ; i < n ; i++)
      {
	  cin>>init[i];
	  for(int j = 0 ; j < n ; j++)
	    if( init[i][j] == '.' )
	      init[i][j] = ' ';
	  string temp1 , temp;
	  stringstream ss;
	  ss<<init[i];
	  while( ss>>temp1 )
	  {
	    temp+=temp1;
	  }
	  
	  
	  reverse(temp.begin() , temp.end() );
	  
	  int l = temp.size();
	  
	  temp.resize(n);
	  
	  for(int j = l ; j < n ; j++)
	      temp[j] = '.';
	  
	  final[i] = temp;
	// cout<<final[i]<<endl;
	  
          
      }
    //  cout<<endl;
      vector<string> end;
      end.resize(n);
      for(int i = n-1 ; i >= 0 ; i--)
      {
	for(int j = n-1 ; j >= 0 ; j--)
	{
	    end[i].push_back( final[j][i] );
	}
	//cout<<end[i]<<endl;
      }
      bool red , blue;
      red = blue = false;
      int x , y;
      for(int i = 0 ; i < n ; i++)
	for(int j = 0 ; j < n ; j++)
	{
	    bool r1 , b1;
	    r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i+m-1;
		y = j;
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	    if( b1 )
	      blue = true; 
	    
	    r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i-(m-1);
		y = j;
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true; 
	     
	    r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i;
		y = j + (m-1);
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true;  
	     
	    r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i;
		y = j - (m-1);
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true;  
	     
	    r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i + (m-1);
		y = j + (m-1);
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true; 
	     
	     r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i - (m-1);
		y = j - (m-1);
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true; 
	     
	     r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i + (m-1);
		y = j - (m-1);
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true; 
	     
	     
	     r1 = b1 = true;
	    for(int m = 1 ; m <= k ; m++)
	    {
		x = i - (m-1);
		y = j + (m-1);
		if( ( ! ( 0 <= x && x < n && 0 <= y && y < n ) ) )
		{
		    r1 = b1 = false;
		    break;
		}
		if( end[x][y] != 'R' )
		  r1 = false;
		if( end[x][y] != 'B' )
		  b1 = false;
	    }
	     if( r1 )
	      red = true;
	     if( b1 )
	      blue = true; 
	}
	
	
	int val;
	if( red && blue )  
	  val = 3;
	else if( ( ! red  ) && (! blue) )
	  val = 2;
	else if( red && (!blue) )
	  val = 0;
	else if( blue && (!red ) )
	  val = 1;
	  
	cout<<"Case #"<<(num-t)<<": "<<ret[val]<<endl;  
	  
	  
    }
  

    return 0;
}