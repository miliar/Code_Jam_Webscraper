#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define forsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define dforsn(i,s,n) for(int i = (int)n; i>= (int)(s);i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define esta(a,c) (find(c.begin(),c.end(), a) != c.end())
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define MAX 2147483647
#define caso(x,y) "Case #"<<x<<": " <<y<<endl

int a[15000];
int ma[15000][300];
int d,l,n,m;/*
int r(int ii,int jj)
{
    if (ma[ii][jj] != -1) return ma[ii][jj];

    if (ii == n) return 0;
    if (abs(jj-a[ii+1]) <= m)
    {
        ma[ii][jj] = r(ii+1,a[ii+1]);
        return ma[ii][jj];
    }

    int mejor = MAX;
    forsn(j, max(0, jj-m), min(256,jj+m))
    {
        int ca = r(ii+2,j) + d;
        if (ca < mejor ) mejor = ca;
    }

    forn(j, 256)
    {
       int aux;
          if (m != 0)
                {
            aux = (abs(jj-j) / m);
            if (abs(a[i]-a[i+j+1]) % m != 0) aux++;
            int mejor = min(l*max(0, (aux-1)),  max ( abs(a[i]-a[i+j+1])- m,0));
             if (ma[i+j+1] >   ma[i] + j * d + mejor)
                ma[i+j+1] =  ma[i] + j * d + mejor;
                }
            else
            {
                int mejor = abs(a[i]-a[i+j+1]);
                 if (ma[i+j+1] >   ma[i] + j * d + mejor)
                ma[i+j+1] =  ma[i] + j * d + mejor;
            }
        int ca = r(ii+1,j) + max (0,abs(jj-j)- m );

        if (ca < mejor ) mejor = ca;
    }


    ca = r(ii+1,a[jj+1]) + l *  aux;
    if (mejor > ca)
    {
         cout<<ii<<"inserto"<<l *  aux <<endl;

        mejor = ca;
    }
    ma[ii][jj] = mejor;
    return ma[ii][jj];
}*/
int main()
{
    int t;
    cin>>t;
    forn(cc,t)
    {
        cin>>d>>l>>m>>n;
       // cout<<d<<" " <<l<<" "<<m<<" "<<n<<endl;
        forn(i,n)
        {
            cin>>a[i+1];
        //    cout<<a[i+1]<<" ";
        }
       // cout<<endl;
        forn(i,n+2)
        {
            forn(j,256)
                ma[i][j]= MAX;

        }
 forn(j,256)
 ma[0][j] = 0;
        forn(i,n+2)
        {
            forn(j,256)
            {
                //delete
                if (ma[i+1][j] > ma[i][j] + d)
                    ma[i+1][j] = ma[i][j] + d;

                 forsn(k, max(0, j-m), min(256,j+m+1))
                    {
                        int mejor;

                        mejor = abs(a[i+1]-k);

                        int ca = ma[i][j] + mejor;
                        if (ca < ma[i+1][k] ) ma[i+1][k] = ca;
                    }
                    if (m != 0)
                forn(k, 256)
                    {

                        int mejor;

                            int aux;
                            aux = (abs(a[i]-k) / m);
                            if (abs(a[i]-k)  % m != 0) aux++;

                            mejor = l*max(0, (aux-1)) +  max (abs(a[i+1]-k),0);


                        int ca = ma[i][j] + mejor;
                        if (ca < ma[i+1][k] ) ma[i+1][k] = ca;
                    }
             //   if (j < 8)
             //   cout<<ma[i][j]<<" ";
/*

                forn(k,256)
                {
                        if (ma[i+1][k] > ma[i][j] + abs(a[i+1]-k) )
                            ma[i+1][k] > ma[i][j] + abs(a[i+1]-k);
                }*/

            }
         //   cout<<endl;
        }
      /*  forn(i,n+1)
        {
            ma[i] = min (ma[i], d * i);
            forn(j,n-i)
            {
                int aux;
                if (m != 0)
                {
            aux = (abs(a[i]-a[i+j+1]) / m);
            if (abs(a[i]-a[i+j+1]) % m != 0) aux++;
            int mejor = min(l*max(0, (aux-1)),  max ( abs(a[i]-a[i+j+1])- m,0));
             if (ma[i+j+1] >   ma[i] + j * d + mejor)
                ma[i+j+1] =  ma[i] + j * d + mejor;
                }
            else
            {
                int mejor = abs(a[i]-a[i+j+1]);
                 if (ma[i+j+1] >   ma[i] + j * d + mejor)
                ma[i+j+1] =  ma[i] + j * d + mejor;
            }





             cout<< ma[i+j+1]<< " " << i<< " " << i+j+1<< " " <<abs(a[i]-a[i+j+1])- m<<" "<< l*max(0, (aux-1))<< " //";
            }
            cout<<ma[i]<<" "<<endl;
        }*/
//cout<<endl;
        int mejor = MAX;
        forn(i,256)
            if (ma[n][i] < mejor) mejor = ma[n][i];
        cout<<caso(cc+1,mejor);
    }

	return 0;

}
