#include <iostream>
#include <fstream>

int main (){
	int t,r,k,n,g[10],temp[10],euro,i,j,y,z,p,pp;

   ifstream in("C-small-attempt1.in");
  	if(!in) {
    	cout << "Cannot open file.\n";
    	return 1;
  	}

   ofstream out("test.out");
   if(!out) {
   	cout << "Cannot open file.\n";
      return 1;
   }

   in >> t;

   for (i = 0; i < t; i++){
   	in >> r >> k >> n;

      for (j = 0; j < n; j++){
      	in >> g[j];
      }

      euro = 0;
      for (j = 0; j < r; j++){
         y = 0; p = 0;
         while (p < n){
         	y += g[p];
            if (y > k){
            	y -= g[p];
               break;
            }
            else{
            	temp[p] = g[p];
            }
            p++;
         }
         pp = 0;
         for (z = p; z < n; z++){
         	g[pp] = g[z];
            pp++;
         }
         for (z = 0; z < p; z++){
         	g[pp] = temp[z];
            pp++;
         }
         euro += y;
      }
      out << "Case #" << (i+1) << ": " << euro << endl;
   }

   in.close();
   out.close();
	cin.get();
   cin.sync();
   cin.clear();
   return 0;
}