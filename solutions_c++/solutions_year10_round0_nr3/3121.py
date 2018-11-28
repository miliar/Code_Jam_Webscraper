#include <iostream>
using namespace std;

int main()
{

  freopen("C-small-attempt5.in","r",stdin);
  freopen("C-small-attempt5.out","w",stdout);
  int casos;  
  long r,k,n,suma,euros,t;
  long a[11] = {0};
  long a1[11] = {0};
 cin >> casos;
   for (int i = 1; i <= casos; i++)
    {
       cin >> r >> k >> n;       
       //llenamos arreglo
       for (int j = 1; j<=n; j++)
          cin >> a[j];
        //listo
         suma = 0;
         euros = 0;
       for (int j = 1; j<= r; j++)
        {
           //numero de veces q se pasean   
            int z=0;
            suma = 0;
            if (n == 1) // si es 1; el Z se caga...xD.
              euros = r;
            else
             {
        /*    while(suma <= k)
             {     
               z++;//z = 1,2,3
               suma = suma + a[z];
               if (z > n) break;
             }  
             if (suma > k)
               {
               suma = suma - a[z];
                z--;
               }
               else
                z=n;
                
          */
            for (int t = 1; t <= n;t++)
             {
               suma = suma + a[t];
               if (suma > k)
                {
                 suma = suma-a[t];
                 z = t-1;
                 break;
                 }   
                if (suma <= k)
                   z = t; 
             }
                
            euros = euros + suma;           
          //formando el Nuevo arreglo:
          //movemos z elementos.
          //z indica la cantidad de personas
          //que subieron (indices).
          //usamos : w,x,y
          for (int w = 1; w <= n-z; w++)
             a1[w] = a[w+z];
              
          int x = n;
          for (int w = 1; w <= z; w++)
          {
             a1[x-z+1] = a[w];
             x++;
          }       
          for (int w = 1; w<=n; w++)
             a[w] = a1[w];   
              
           //for (int w = 1; w<=n; w++)
             // cout << a[w] << " ";
              //cout << endl;   
              }          
        }//end del For J
     cout <<"Case #"<< i <<": "<<euros<<endl; 
    }   //end del For I
return 0;
}
