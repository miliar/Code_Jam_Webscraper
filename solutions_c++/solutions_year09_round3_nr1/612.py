#include <cstdlib>
#include <iostream>
#include <string>
#include <stdio.h>
#include <set>
  #include <cstdio>
   #include <cstring>
   #include <algorithm>

#include <vector>
#define ll long long int
using namespace std;



const int BASE = 1000000000; /* podstawa */
   const int DIGS = 9; /* liczba cyfr dziesietnych kazdej cyfry w zapisie
                          przy powyzszej podstawie */
   const int LEN = 1000; /* stala dlugosc liczb */

  struct liczba
  {
    int t[LEN];
    int l; /* faktyczna dlugosc liczby */
  };


  void wypisz(liczba x)
  {
    printf("%d", x.t[x.l - 1]);
    for (int i = x.l - 2; i >= 0; i--)
      printf("%0*d", DIGS, x.t[i]);
 }
   void czytaj(liczba &x,string ss)
   {
     char s[LEN * DIGS + 1];
 //    sscanf(ss,"%s", s); /* czytamy lancuch - zakladamy, ze nie ma zer wiodacych */
 for(int i=0;i<ss.length();i++)
 s[i]=ss[i];
     /* Ustalamy dlugosc liczby */
     int j = strlen(s); /* pozycja w lancuchu s */
     if (j % DIGS == 0)
       x.l = j / DIGS;
     else
      x.l = j / DIGS + 1;
    j--;
    for (int i = 0; i < x.l; i++)
    {
      /* ustalamy i-ta cyfre */
      x.t[i] = 0;
      for (int k = max(0, j - DIGS + 1); k <= j; k++)
          x.t[i] = 10 * x.t[i] + (s[k] - '0');
      j -= DIGS;
    }
  }

liczba operator+ (liczba x, liczba y)
   {
     liczba z; /* wynik */
     /* Do dlugosci mniejszej z liczb: */
     z.l = min(x.l, y.l);
     int c = 0; /* na poczatek zerowy bit przeniesienia */
     for (int i = 0; i < z.l; i++)
     {
       z.t[i] = (x.t[i] + y.t[i] + c) % BASE;
      c = (x.t[i] + y.t[i] + c) / BASE;
    }
    /* Jezeli liczba x jest dluzsza: */
    while (z.l < x.l)
    {
      z.t[z.l] = (x.t[z.l] + c) % BASE;
      c = (x.t[z.l] + c) / BASE;
      z.l++;
    }
    /* Jezeli liczba y jest dluzsza: */
    while (z.l < y.l)
    {
      z.t[z.l] = (y.t[z.l] + c) % BASE;
      c = (y.t[z.l] + c) / BASE;
      z.l++;
    }
    /* Jezeli pozostalo jakies przeniesienie (to c=1): */
    if (c > 0)
    {
      z.t[z.l] = c;
      z.l++;
    }
    return z;
  }

liczba operator* (liczba x, int y)
   {
     liczba z;
     z.l = x.l;
     int c = 0;
     for (int i = 0; i < x.l; i++)
     {
       z.t[i] = int(((long long)(x.t[i]) * y + c) % BASE);
      c = int(((long long)(x.t[i]) * y + c) / BASE);
    }
    while (c > 0)
    {
      z.t[z.l] = c % BASE;
      c /= BASE;
      z.l++;
    }
    return z;
  }



   liczba operator* (liczba x, liczba y)
   {
     liczba z;
     z.l = 1; z.t[0] = 0; /* z to pocz¹tkowo 0 */
     for (int i = 0; i < y.l; i++)
     {
       liczba pom(x * y.t[i]);
       /* przesuwamy liczbe pom, dodajac i zer na koncu */
       for (int j = pom.l - 1; j >= 0; j--)
        pom.t[j + i] = pom.t[j];
      for (int j = 0; j < i; j++)
        pom.t[j] = 0;
      pom.l = pom.l + i;
      z = z + pom;
    }
    return z;
  }








int t,n,pod,k;
string s;
vector<int> T;
set<char>S;

int V[305];
int main(int argc, char *argv[])
{
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
            
      S.clear();T.clear();
      cin>>s;
     // cout<<s;
      n=s.size();

      for(int i=0;i<n;i++)
      S.insert(s[i]);
      pod=S.size();
     // cout<<pod;  
      for(int i=0;i<300;i++)V[i]=-1;
      V[s[0]]=1;
      
      
      int curr=0;
      for(int i=0;i<n;i++)
      {
      if(curr==1)curr++;
      if(V[s[i]]==-1)
        { V[s[i]]=curr;curr++;} 
    //    cout<<V[s[i]];
      T.push_back(V[s[i]]);  
      }
      if(pod==1)pod=2;
      liczba res,wyk;
      
      czytaj(res,"0");
      czytaj(wyk,"1");
     // res.l=1; wyk.l=1;
     // res.t[0]=0; res.t[0]=1;
      
      for(int i=n-1; i>=0;i--)
      {
 //     cout<<T[i];
      //cout<<res<<" "<<wyk<<endl;
      res=res+wyk*T[i];
      wyk=wyk*pod;  
//      cout<<wyk<<endl;      
              
      }
      
      
      
         
        
            
    printf("Case #%d: ",i);  
    wypisz(res);     
    printf("\n"); 
    }
    
    
 //   system("PAUSE");
    return 0;
}
