#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

bool checkDancer (int number,int& surprice,int max){
     if (number-max<0)
        return false;
     else if (((number-max)/2)+2>max)
        return true;
     else if ((surprice!=0)&&(((number-max)/2 +2)==max)){
          surprice = surprice-1;
          return true;
          }
     return false;
}


int main(int argc, char *argv[])
{
    int row;
  int dancers;
  int surprice;
  int max;
  int all;
  
  scanf("%i", &row);
  all = row;
  char word[100];
  while (row!=0){ 
          int total=0;
          scanf("%i",&dancers);
          scanf("%i",&surprice);
          scanf("%i",&max);      
          do{
                int temp;
                scanf("%i",&temp);
                if (checkDancer(temp,surprice,max))
                   total=total+1;            
                dancers=dancers-1;      
          }while (dancers!=0); 
          printf("Case #%i: %i\n",all-row+1,total);
    row=row-1;
  }
    return EXIT_SUCCESS;
}
