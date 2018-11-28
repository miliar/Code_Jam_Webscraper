#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

void selectionSortASC ( int* arr, int size )
{
   int indexOfMin;
   int pass;
   int j;

   for ( pass = 0; pass < size - 1; pass++ )
   {
           indexOfMin = pass;

           for ( j = pass + 1; j < size; j++ )
               if ( arr[j] < arr[indexOfMin] )
                   indexOfMin = j;

           swap ( arr[pass], arr[indexOfMin] );
   }
}

void selectionSortDSC ( int* arr, int size )
{
   int indexOfMax;
   int pass;
   int j;

   for ( pass = 0; pass < size - 1; pass++ )
   {
           indexOfMax = pass;

           for ( j = pass + 1; j < size; j++ )
               if ( arr[j] > arr[indexOfMax] )
                   indexOfMax = j;

           swap ( arr[pass], arr[indexOfMax] );
   }
}

// swap function for integers
void swap ( int& x, int& y )
{
   int temp;
   temp = x;
   x = y;
   y = temp;
} 

int main(int argc, char *argv[])
{
    int n = 0;
    cin >> n;
    for(int i = 0; i < n; i++){
            int x = 0;
            cin >> x;
            int* v1 = new int[x];
            int* v2 = new int[x];
            
            for (int j = 0; j < x; j++){
                cin >> v1[j];
            }
            
            for (int j = 0; j < x; j++){
                cin >> v2[j];
            }
            selectionSortASC(v1,x);
            selectionSortDSC(v2,x);
            int total = 0;
            for (int j = 0; j < x; j++)
            {
                total+= v1[j]*v2[j];
            }
    
            cout << "Case #" << i +1 <<": " << total << endl;
    }    
    return EXIT_SUCCESS;
}
