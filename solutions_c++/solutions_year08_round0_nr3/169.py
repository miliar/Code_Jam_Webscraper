//MADE BY lordmonsoon A.I.
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())

////////////////////////////////////////////////////////////////////////////////
#define X first
#define Y second
#define PUNKTD pair<double,double>
#define PI (2*acos(0))
#define EPS 1e-12

inline double lmIloczynWektorowyD(PUNKTD a,PUNKTD b,PUNKTD c)
{
      return (a.X-c.X)*(b.Y-c.Y)-(a.Y-c.Y)*(b.X-c.X);
}

inline double lmOdlegloscPunktPunktD(PUNKTD a,PUNKTD b)
{
      return sqrt((a.X-b.X)*(a.X-b.X)+(a.Y-b.Y)*(a.Y-b.Y));
}

inline double lmWycinek(PUNKTD a,PUNKTD b,double R)
{
      double ww = lmOdlegloscPunktPunktD(a,b)/(2*R);
      return (asin(ww) - sin(2*asin(ww))/2.0) * R * R;
}

int test;
double f,R,r,g,t;
double mianownik;

int main()
{
      scanf("%d",&test);
      FOR(test2,1,test)
      {
            scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
            R -= t;
            double ppb = 0.0;
            double y = r;
            mianownik = PI * (R + t) * (R + t) / 4.0;
            while(true)
            {
                  double x = r;
                  if( R * R < x * x + y * y) break;
                  while(true)
                  {
                        if( R * R < x * x + y * y) break;
                        
                        //zlicz pole
                        double nR = R - f;
                        double nX = x + f;
                        double nY = y + f;
                        double len = g - 2 * f;
                        if( len < 0.0 || nR < 0.0) break; 
                        if( nR * nR < nX * nX + nY * nY ) break;
                        
                        if(nR*nR > (nX + len) * (nX + len) + (nY + len) * (nY + len))
                        {
//                              printf("T0 %lf %lf\n",x,y);
                              ppb += len * (len / mianownik);
                        }
                        else
                        {
                              //dol, czy prawy
                              if(nR*nR < (nX + len) * (nX + len) + nY * nY )//dol
                              {
                                    double x1 = sqrt(abs(nR * nR - nY * nY));
                                    //lewy, czy gora
                                    if(nR * nR < nX * nX + (nY + len) * (nY + len))//lewy
                                    {
//                                          printf("T1 %lf %lf\n",x,y);
                                          double y1 = sqrt( abs(nR * nR  - nX * nX) );
                                          double alfa = lmWycinek(PUNKTD(x1,nY),PUNKTD(nX,y1),nR);
                                          ppb += (0.5 * (x1 - nX) * (y1 - nY) + alfa) / mianownik;
                                    }
                                    else //gora
                                    {
//                                          printf("T2 %lf %lf\n",x,y);
                                          double x2 = sqrt(abs(nR * nR - (nY + len) * (nY + len)));
                                          double alfa = lmWycinek(PUNKTD(x1,nY),PUNKTD(x2,nY + len),nR);
                                          ppb += (0.5*len*(x1 - nX + x2 - nX) + alfa) / mianownik;
//                              printf("%lf %lf %lf %lf\n",nX,nY,len,nR);
                                    }
                              }
                              else //prawy
                              {
                                    double y1 = sqrt(abs(nR * nR - (nX + len) * (nX + len)));
                                    //lewy, czy gora
                                    if(nR * nR < nX * nX + (nY + len) * (nY + len))//lewy
                                    {
//                                          printf("T3 %lf %lf\n",x,y);
                                          double y2 = sqrt( abs(nR * nR  - nX * nX) );
                                          double alfa = lmWycinek(PUNKTD(nX + len,y2),PUNKTD(nX,y1),nR);
                                          ppb += (0.5*len*(y1 - nY + y2 - nY) + alfa) / mianownik;                                          
                                    }
                                    else //gora
                                    {
//                                          printf("T4 %lf %lf\n",x,y);
                                          double x2 = sqrt(abs(nR * nR - (nY + len) * (nY + len)));
                                          double alfa = lmWycinek(PUNKTD(nX + len,y1),PUNKTD(x2,nY + len),nR);
                                          ppb += (len * (y1 - nY) + 0.5*(nY + len - y1)*(x2 - nX + len) + alfa) / mianownik;
                                    }
                              }
                        }
                        x += g + 2 * r;
                  }
                  
                  y += g + 2 * r;
            }
//            printf("%lf %lf",ppb,PI * (R + t) * (R + t) / 4.0);
            printf("Case #%d: %.6lf\n",test2,1.0 - ppb);
      }
      return 0;
}
