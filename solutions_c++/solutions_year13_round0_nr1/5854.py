#include <algorithm> 
#include <iostream>
#include <string>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;


#include<fstream>
ifstream fin("input.txt");
ofstream fout("output.txt");

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

int POWR[10] = {10, 100, 1000, 10000, 100000, 1000000, 10000000};




void run(int casenr) {
    char T[4][4];
    int i,j,k;

    for(i=0;i<=3;i++)
    {
      for (j=0;j<=3;j++)
      {
           fin >> T[i][j];
      }
    }

    int hasDot = 0;
    int count=0;
    char sym;

    i=0;

    for (j=0;j<=3;j++)
    {
        //PROCESS ROW
        sym = T[j][i];
        count = 1;
        k = i+1;

        if(sym == 'T')
        {
          sym = T[j][k];
          count++;
          k++;
        }

       if(sym == '.')
        hasDot = 1;
       else  {


        for(;k<=3;k++)
        {
            if(T[j][k] == sym || T[j][k] == 'T')
            {

              count++;
             }
           else{
                if(T[j][k] == '.')
                  hasDot = 1;
                break;
                }
        }

        if(count == 4)
         {
            if (sym == 'X')
              fout <<"Case #"<<casenr<<": X won"<<endl;
           else if (sym == 'O')
              fout <<"Case #"<<casenr<<": O won"<<endl;

               if(casenr == 5)
                cout << " SYM :: ROW " << sym<<endl;
           return;
         }
       }


         //PROCESS COLOUM
        sym = T[i][j];
        count = 1;
        k = i+1;
        if(sym == 'T')
        {
          sym = T[k][j];
          count++;
          k++;
        }
       

       if(sym == '.')
        hasDot = 1;
       else  {
    
         for(;k<=3;k++)
        {
            if(T[k][j] == sym || T[k][j] == 'T')
              count++;
           else{
                if(T[k][j] == '.')
                  hasDot = 1;
                break;
                }
        }

        if(count == 4)
         {

            if (sym == 'X')
              fout <<"Case #"<<casenr<<": X won"<<endl;
           else if (sym == 'O')
              fout <<"Case #"<<casenr<<": O won"<<endl;

              if(casenr == 5)
                cout << " SYM ::COLOUM " << sym<<endl;

              return;
         }
        }

        }


      //Process DIAGONAL 1
        sym = T[0][0];
        count = 1;
        k = 1;
        if(sym == 'T')
        {
          sym = T[k][k];
          count++;
          k++;
        }

         if(casenr == 6)
             cout << "SYM " <<sym << " k :: " << k <<"  T[k][k] " << T[k][k]<<endl;
       if(sym == '.')
        hasDot = 1;
       else  {
    
        for(;k<=3;k++)
        {
           if(casenr == 6)
             cout << "SYM " <<sym << " k :: " << k <<"  T[k][k] " << T[k][k]<<endl;


            if(T[k][k] == sym || T[k][k] == 'T')
              count++;
           else{
                if(T[k][k] == '.')
                  hasDot = 1;
                break;
                }
        }
           if(casenr == 6)
             cout << "SYM " <<sym << " count :: " << count <<endl;
        

        if(count == 4)
         {

            if (sym == 'X')
              fout <<"Case #"<<casenr<<": X won"<<endl;
           else if (sym == 'O')
              fout <<"Case #"<<casenr<<": O won"<<endl;


              return;
           }
        }

        //Process DIAGONAL 2
        sym = T[3][0];
        count = 1;
        k = 1;
        if(sym == 'T')
        {
          sym = T[3-k][k];
          count++;
          k++;
        }

        if(sym == '.')
        hasDot = 1;
       else  {

        for(;k<=3;k++)
        {
            if(T[3-k][k] == sym || T[3-k][k] == 'T')
              count++;
           else{
                if(T[3-k][k] == '.')
                  hasDot = 1;
                break;
                }

       }

        if(count == 4)
         {

            if (sym == 'X')
              fout <<"Case #"<<casenr<<": X won"<<endl;
           else if (sym == 'O')
              fout <<"Case #"<<casenr<<": O won"<<endl;


              return;
           }
        }




       if(hasDot)
        fout <<"Case #"<<casenr<<": Game has not completed"<<endl;
       else
        fout <<"Case #"<<casenr<<": Draw"<<endl;

        return;

}

int main() {
   	int n;
    //scanf("%d",&n);
    fin >> n;
    FORE(i,1,n) run(i);



    system("PAUSE");
	return 0;
}
