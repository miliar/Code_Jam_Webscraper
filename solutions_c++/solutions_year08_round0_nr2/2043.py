#include<iostream>
#include <fstream>
using namespace std;

#include <string>

#include <stdio.h>
#include <stdlib.h>
//#include <sstream>



int main (char *argv[]) {
  string line;
  int queries, turn, va, vb, tva, tvb;
  int ta = 0;
  int tb = 0, tna =0, tnb = 0;
  ifstream myfile;
  int* tca, *tcb, *tsa, *tsb;
  //string* sch = NULL;
  //int* iguais = NULL;
  
  myfile.open("teste2.txt");
  
   getline (myfile,line);
//     fscanf(myfile, "%i", queries);
//   from_string(queries,line, std::dec);
      //queries = line[0] - 48;
      //cout << line[0]<< endl;
      queries = atoi(line.c_str());
      //cout << "queries ok" << queries;
  for (int k=0; k < queries; k++){
        ta = 0;
   tb = 0; tna =0; tnb = 0;
     int firstarg=0,secondarg=0, end = 0;
      getline (myfile,line);
      //cout << line[0];
      //  fscanf(myfile, "%i", turn);
      //turn =  line[0] - 48;
      turn = atoi(line.c_str());
       //cout << "turn ok" << turn;
      
      getline (myfile,line);
      va = atoi(line.c_str());
      end = line.find(' ',0);
      line.erase(0,end+1);
        vb = atoi(line.c_str());
      /*        //get the number before the ,
        string tempnum = line.substr(0,end);
        if (end ==0 )va=atoi(tempnum.c_str());
          if (end ==1 )vb=atoi(tempnum.c_str());
        //secondarg++;
        //erase the part of the line we have gotten
       

      }*/
   //cout<< va << "||" <<vb;

       
       // fscanf(myfile, "%i %i", va, vb);
     // cout << line[0];
      //va =  line[0] - 48;
      //vb =  line[2] - 48;
      //tinva = new int[vb];
      //tinvb = new int[va];
      
      
      int nlinhas = va + vb;
      tsa = new int[va];
      tcb = new int[va];
      tsb = new int[vb];
      tca = new int[vb];
      for (int i = 0; i < va; i++){
          getline(myfile, line);
          int dhoras = (line[0] - 48)*10;
          int uhoras = (line[1] - 48);
          int dmin = (line[3] - 48)*10;
          int umin = (line[4] - 48);
          int total = (dhoras + uhoras)*60 + dmin + umin;
      //    cout << total << " | ";
          tsa[i] = total;
         //   cout << tsa[i] << " -| ";
          
           dhoras = (line[6] - 48)*10;
           uhoras = (line[7] - 48);
           dmin = (line[9] - 48)*10;
           umin = (line[10] - 48);
           total = (dhoras + uhoras)*60 + dmin + umin;
        //   cout << total << " | ";
          tcb[i] = total+ turn -1;
            //cout << tcb[i] << " -| ";
          
          }
          
       for (int i = 0; i < vb; i++){
          getline(myfile, line);
          int dhoras = (line[0] - 48)*10;
          int uhoras = (line[1] - 48);
          int dmin = (line[3] - 48)*10;
          int umin = (line[4] - 48);
          int total = (dhoras + uhoras)*60 + dmin + umin;
       //   cout << total << " | ";
          tsb[i] = total;
       //    cout << tsb[i] << " -| ";
          
           dhoras = (line[6] - 48)*10;
          uhoras = (line[7] - 48);
          dmin = (line[9] - 48)*10;
          umin = (line[10] - 48);
         total = (dhoras + uhoras)*60 + dmin + umin;
      //   cout << total << " | ";
       tca[i] = total + turn - 1;
    //  cout << tca[i] << " -| ";
          }
          
      int day = 1440;
      for (int i = 0; i< day; i++){
          for (int j = 0; j < vb; j++){
        //      if (tca[j] == i) ta++;
            
              if (tsb[j] == i) {
                         if (tb < 1) tnb++; 
                         else tb--;
                         }
              }
          for (int j = 0; j < va; j++){
             // if (tcb[j] == i) tb++;
            
              if (tsa[j] == i) {
                         if (ta < 1) tna++; 
                         else ta--;
                         }
              } 
              
              
          for (int j = 0; j < va; j++){
             if (tcb[j] == i) tb++;
            
             // if (tsa[j] == i) {
             //            if (ta < 1) tna++; 
              //           ta--;
              //           }
              } 
              
                for (int j = 0; j < vb; j++){
           if (tca[j] == i) ta++;}
      
      }
     
      ofstream myfile2;
      myfile2.open ("output.txt", ios::app);
     myfile2 <<  "Case #" << k+1 <<": " << tna << " " << tnb << endl;
  myfile2.close();

   //  cout << "Case #" << k+1 <<": " << tna << " " << tnb << endl;
     
     delete tsa;
     delete tcb;
     delete tsb;
     delete tca;// tsb = delete[];
     // tca = delete[];
}//fim for k 
    myfile.close();
  

 

  return 0;
}
