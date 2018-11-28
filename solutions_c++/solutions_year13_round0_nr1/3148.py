 /* Copyright NTU GIEE 2012. All Rights Reserved. */
 /* =====================================================================================
 *       Filename:  B.cpp
 *    Description:  
 *        Created:  04/14/2012 12:42:55 PM CST
 *         Author:  Bo-Han Gary Wu (NTU GIEE), researchgary@gmail.com
 * ===================================================================================== */

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <cassert>
#include <vector>

using namespace std;

int main(int argc, char* argv[]){
   ifstream ifile(argv[1]);
   if ( argc != 2 ){
      cout << "Error" << endl;
      return 0;
   }

   ofstream ofile("A.out");
   int T, N, S, p;
   ifile >> N;
   for ( uint32_t i = 0 ; i < N ; ++i ){
      char M[4][4];
      for ( uint32_t j = 0 ; j < 4 ; ++j ){
         for ( uint32_t k = 0 ; k < 4 ; ++k ){
            ifile >> M[j][k];
         }
      }
      bool diff = false;
      bool rst = false, ontheway=false;
      // check row 
      for ( uint32_t j = 0 ; j < 4 ; ++j ){
         int nX = 0, nO = 0;
         for ( uint32_t k = 0 ; k < 4 ; ++k ){
            if ( M[j][k] == '.' ){
               ontheway = true;
               break;
            }
            nX += (M[j][k]=='X' || M[j][k]=='T');
            nO += (M[j][k]=='O' || M[j][k]=='T');
         }
         if ( nX == 4 ){
            ofile << "Case #" << i+1 << ": X won" << endl;
            cout << "Case #" << i+1 << ": X won"  << endl;
            rst = true;
            break;
         }else if ( nO == 4 ){
            ofile << "Case #" << i+1 << ": O won" << endl;
            cout << "Case #" << i+1 << ": O won"  << endl;
            rst = true;
            break;
         }
      }
      if ( rst )
         continue;
      for ( uint32_t k = 0 ; k < 4 ; ++k ){
         int nX = 0, nO = 0;
         for ( uint32_t j = 0 ; j < 4 ; ++j ){
            if ( M[j][k] == '.' )
               break;
            nX += (M[j][k]=='X' || M[j][k]=='T');
            nO += (M[j][k]=='O' || M[j][k]=='T');
         }
         if ( nX == 4 ){
            ofile << "Case #" << i+1 << ": X won" << endl;
            cout << "Case #" << i+1 << ": X won"  << endl;
            rst = true;
            break;
         }else if ( nO == 4 ){
            ofile << "Case #" << i+1 << ": O won" << endl;
            cout << "Case #" << i+1 << ": O won"  << endl;
            rst = true;
            break;
         }
      }
      if ( rst )
         continue;

      // diagonal
      vector<pair<int,int> > d1(4), d2(4);
      int nX = 0, nO = 0;
      d1[0]=make_pair(0,0); d1[1]=make_pair(1,1); d1[2]=make_pair(2,2); d1[3]=make_pair(3,3);
      d2[0]=make_pair(0,3); d2[1]=make_pair(1,2); d2[2]=make_pair(2,1); d2[3]=make_pair(3,0);
      for ( uint32_t j = 0 ; j < 4 ; ++j ){
         char c = M[d1[j].first][d1[j].second];
         if ( c == '.' )
            break;
         nX += (c=='X' || c=='T');
         nO += (c=='O' || c=='T');
         if ( nX == 4 ){
            ofile << "Case #" << i+1 << ": X won" << endl;
            cout << "Case #" << i+1 << ": X won"  << endl;
            rst = true;
            break;
         }else if ( nO == 4 ){
            ofile << "Case #" << i+1 << ": O won" << endl;
            cout << "Case #" << i+1 << ": O won"  << endl;
            rst = true;
            break;
         }
      }
      if ( rst )
         continue;

      nX = 0, nO = 0;
      for ( uint32_t j = 0 ; j < 4 ; ++j ){
         char c = M[d2[j].first][d2[j].second];
         if ( c == '.' )
            break;
         nX += (c=='X' || c=='T');
         nO += (c=='O' || c=='T');
         if ( nX == 4 ){
            ofile << "Case #" << i+1 << ": X won" << endl;
            cout << "Case #" << i+1 << ": X won"  << endl;
            rst = true;
            break;
         }else if ( nO == 4 ){
            ofile << "Case #" << i+1 << ": O won" << endl;
            cout << "Case #" << i+1 << ": O won"  << endl;
            rst = true;
            break;
         }
      }
      if ( rst )
         continue;

      if ( ontheway ){
         ofile << "Case #" << i+1 << ": Game has not completed" << endl;
         cout << "Case #" << i+1 << ": Game has not completed"  << endl;
      }else{
         ofile << "Case #" << i+1 << ": Draw" << endl;
         cout << "Case #" << i+1 << ": Draw"  << endl;
      }
   }

   ofile.close();
   ifile.close();
   return 0;
}
