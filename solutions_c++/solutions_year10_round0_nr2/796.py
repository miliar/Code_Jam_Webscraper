#include<iostream>
#include<fstream>
using namespace std;
typedef int uint64;
uint64 gcd(uint64 u, uint64 v)
 {
     int shift;
     if (u == 0 || v == 0)
       return u | v;

     for (shift = 0; ((u | v) & 1) == 0; ++shift) {
         u >>= 1;
         v >>= 1;
     }

     while ((u & 1) == 0)
       u >>= 1;
     do {
         while ((v & 1) == 0)  /* Loop X */
           v >>= 1;
         if (u < v) {
             v -= u;
         } else {
             uint64 diff = u - v;
             u = v;
             v = diff;
         }
         v >>= 1;
     } while (v != 0);

     return u << shift;
 }

int main()
{
        unsigned int c,n,t[100];
        int i,j,diff,r,dif1;
        ifstream fin("B-small.in");
        ofstream fout("output_b_small.out");
        fin>>c;
        j=1;
        while(c)
        {
            fin>>n;
            for(i=0;i<n;i++)
            {
                fin>>t[i];
            }
            if(n==2)
            {
                diff=t[0]-t[1];
                if(diff<0)
                diff=-diff;
                r=t[0]%diff;
                if(r!=0)
                {
                diff=diff-r;
                fout<<"Case #"<<j<<": "<<diff<<endl;
                }
                else
                fout<<"Case #"<<j<<": 0"<<endl;

            }
            else if(n==3)
            {
                diff=t[0]-t[1];
                if(diff<0)
                diff=-diff;
                dif1=t[0]-t[2];
                if(dif1<0)
                dif1=-dif1;
                diff=gcd(diff,dif1);
                r=t[0]%diff;
                if(r!=0)
                {
                diff=diff-r;
                fout<<"Case #"<<j<<": "<<diff<<endl;
                }
                else
                fout<<"Case #"<<j<<": 0"<<endl;

            }

            j++;
            c--;
        }
}
