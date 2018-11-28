#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::string TicTacToeTomek ( const std::vector<std::string> &board )
{
   const size_t n = board.size ();

   for ( size_t i=0; i<n; i++ )
      std::cerr << board[i] << std::endl;

   size_t c = 0;
   size_t d1x = 0, d1o = 0, d1t = 0;
   size_t d2x = 0, d2o = 0, d2t = 0;

   for ( size_t i=0; i<n; i++ )
   {
      size_t rx = 0, ro = 0, rt = 0;
      size_t cx = 0, co = 0, ct = 0;

      for ( size_t j=0; j<n; j++ )
      {
         // empty
         if ( board[i][j] == '.' ) ++c;

         // row
         switch ( board[i][j] )
         {
            case 'X': ++rx; break;
            case 'O': ++ro; break;
            case 'T': ++rt; break;
         }

         // col
         switch ( board[j][i] )
         {
            case 'X': ++cx; break;
            case 'O': ++co; break;
            case 'T': ++ct; break;
         }
      }

      std::cerr << "r: " << rx << "," << ro << "," << rt << std::endl;
      std::cerr << "c: " << cx << "," << co << "," << ct << std::endl;

      if ( rx + rt == n || cx + ct == n )
         return "X won";

      if ( ro + rt == n || co + ct == n )
         return "O won";

      // diag1
      switch ( board[i][i] )
      {
         case 'X': ++d1x; break;
         case 'O': ++d1o; break;
         case 'T': ++d1t; break;
      }

      // diag2
      switch ( board[i][n-i-1] )
      {
         case 'X': ++d2x; break;
         case 'O': ++d2o; break;
         case 'T': ++d2t; break;
      }
   }

   std::cerr << "d1: " << d1x << "," << d1o << "," << d1t << std::endl;
   std::cerr << "d2: " << d2x << "," << d2o << "," << d2t << std::endl;

   if ( d1x + d1t == n || d2x + d2t == n )
      return "X won";

   if ( d1o + d1t == n || d2o + d2t == n )
      return "O won";

   std::cerr << c << std::endl;

   if ( c == 0 )
      return "Draw";

   return "Game has not completed";
}

int main ( int argc, char *argv[] )
{
   if ( argc < 2 )
   {
      std::cerr << "Usage: " << argv[0] << " <test-set>" << std::endl;
      return 1;
   }

   std::ifstream is ( argv[1] );
   char line [256] = { 0 };
   int n = 0;
   is >> n;

   for ( int i=0; i<n; i++ )
   {
      is.getline ( line, 255 );

      std::vector<std::string> v;

      for ( int j=0; j<4; j++ )
      {
         is.getline ( line, 255 );
         v.push_back ( line );
      }

      std::string s = TicTacToeTomek ( v );
      std::cout << "Case #" << i+1 << ": " << s << std::endl;
   }
}
