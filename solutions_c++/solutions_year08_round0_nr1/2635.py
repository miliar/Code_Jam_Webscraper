#include <iostream>

using namespace std;

int main()

{
  char a[101][101], b[1001][101], f[2];
  int n, s, q, i, x[101], t, k, j, rez[21];
  freopen("A-large.in", "r", stdin);
  //freopen("input.txt ", "r", stdin);   
  cin >> n;
    for (i = 1; i<=n; i++)  
      {
         rez[i] = -1;
         cin >> s;
         gets (f);
         //cout << s;
           for (j = 0; j< s; j++)
{             gets(a[j]);
              x[j] = 1001;}
             //cout << a[0];
         cin >> q;
         t = q;
         gets (f);
         //cout << q;
           for (j = 0; j < q; j++)
             {
              gets(b[j]);
              
             }
             //cout << b[0];
         do
         //while (t>0); 
           {
           for (j = 0; j < s; j++)
            // for (k =  q-1; k >= q-t; k--)
             for (k = q-1; k>=q-t; k--)
               if (strcmp(a[j],b[k])==0)
                 {x[j] = k;
                 //cout<<x[j]<<" ";
                 }
                 //cout<<x[0];                 
             for (j = 1; j < s; j++)
               if (x[j] > x[0])
                 x[0]=x[j];
           //if (x[0] < q)
             rez[i]=1+rez[i];
             t=q-x[0];
             for (j = 0; j<s; j++)
              x[j] = 1001; 
          }                  
         while (t>=0);
      }
    freopen("output.txt", "w", stdout);  
    for (i = 1; i <= n; i++)
      
      cout << "Case #" << i << ": " << rez[i] << endl;
      
    return 0;
}
