#include<iostream> 
#include<fstream>

using namespace std;
 int main()
 {
	 ifstream fin("A-large.in");     
	 ofstream fout;
	 fout.open("result_l.out");
	 int T; 
	 fin>>T;
	 for(int n = 0 ; n < T ; n++)
	 {
	 char board[4][4];
	 bool complete = true;
	 bool x = false; 
	 bool o =false; 
	 for(int i = 0 ; i < 4 ; i ++ )
	 {
		 int x_count = 0 ; 
		 int o_count = 0 ;

		  for(int j = 0 ; j < 4 ; j ++ )
		  {
				char temp;			
				fin>>temp ;
				if(temp == '.')
					complete=false;
				else  if (temp == 'X' )
						x_count++;
					else if (temp == 'O')
						o_count++;
					 if ( temp == 'T')
					 {
						 o_count++;
						 x_count++;
					 }
				board[i][j]= temp;
		  }
		  if(x_count == 4 ) 
		  {
			  x=true;
			
		  }
		  else if(o_count == 4 ) 
		  {
			  o=true;
			
		  }

	 }
	 if(!x && !o)
	 {
		 for(int i = 0 ; i < 4 ; i ++)
		 {
			 int x_count = 0 ; 
			 int o_count = 0 ;

			 for(int j = 0 ; j < 4 ; j ++)
			{
					  if (board[j][i] == 'X' )
						x_count++;
					else if (board[j][i] == 'O')
						o_count++;
					 if ( board[j][i] == 'T')
					 {
						 o_count++;
						 x_count++;
					 }
			}
			 if(x_count == 4 ) 
			  {
				  x=true;
				  break;
			  }
			  else if(o_count == 4 ) 
			  {
				  o=true;
				  break;
			  }
		 }
	 }
	 if(!x && !o)
	 {
		 	 int x_count = 0 ; 
			 int o_count = 0 ;

			 for(int j = 0 ; j < 4 ; j ++)
			{
					 if (board[j][j] == 'X' )
						x_count++;
					else if (board[j][j] == 'O')
						o_count++;
					 if ( board[j][j] == 'T')
					 {
						 o_count++;
						 x_count++;
					 }
			}
			 if(x_count == 4 ) 
			  {
				  x=true;			
			  }
			  else if(o_count == 4 ) 
			  {
				  o=true;			
			  }
		 }
	 if(!x && !o)
	 {
		 	 int x_count = 0 ; 
			 int o_count = 0 ;
			 int ss = 3;
			 for(int j = 0 ; j <4 ; j ++)
			{
					 if (board[j][ss] == 'X' )
						x_count++;
					else if (board[j][ss] == 'O')
						o_count++;
					 if ( board[j][ss] == 'T')
					 {
						 o_count++;
						 x_count++;
					 }
					 ss--;
			}
			 if(x_count == 4 ) 
			  {
				  x=true;			
			  }
			  else if(o_count == 4 ) 
			  {
				  o=true;			
			  }
		 }
	 fout<<"Case #"<<n+1<<": ";
	 if( x ) 
	 {
		  fout<<"X won"<<endl;
	 }
	 else if(o) 
	 {
		 fout<<"O won"<<endl;
	 }
	 else if (complete)
	 {
		 fout<<"Draw"<<endl;
	 }
	 else{
		 fout<<"Game has not completed"<<endl;
	 }
	 }

	 
	 return 0 ;
 }