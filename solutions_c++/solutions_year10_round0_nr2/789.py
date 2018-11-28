#include<iostream>
#include<fstream>
using namespace std;
typedef int uint64;
uint64 gcd(uint64 u, uint64 v)
 {
     int shift;

     /* GCD(0,x) := x */
     if (u == 0 || v == 0)
       return u | v;

     /* Let shift := lg K, where K is the greatest power of 2
        dividing both u and v. */
     for (shift = 0; ((u | v) & 1) == 0; ++shift) {
         u >>= 1;
         v >>= 1;
     }

     while ((u & 1) == 0)
       u >>= 1;

     /* From here on, u is always odd. */
     do {
         while ((v & 1) == 0)  /* Loop X */
           v >>= 1;

         /* Now u and v are both odd, so diff(u, v) is even.
            Let u = min(u, v), v = diff(u, v)/2. */
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
        int i,j,d,r,d1;
        ifstream fin("B-small.in");
        ofstream fout("output.out");
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
                d=t[0]-t[1];
                if(d<0)
                d=-d;
                r=t[0]%d;
                if(r!=0)
                {
                d=d-r;
                fout<<"Case #"<<j<<": "<<d<<endl;
                }
                else
                fout<<"Case #"<<j<<": 0"<<endl;

            }
            else if(n==3)
            {
                d=t[0]-t[1];
                if(d<0)
                d=-d;
                d1=t[0]-t[2];
                if(d1<0)
                d1=-d1;
                d=gcd(d,d1);
                r=t[0]%d;
                if(r!=0)
                {
                d=d-r;
                fout<<"Case #"<<j<<": "<<d<<endl;
                }
                else
                fout<<"Case #"<<j<<": 0"<<endl;

            }

            j++;
            c--;
        }
}
