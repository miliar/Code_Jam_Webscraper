#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>

using namespace std;

int main()
{
  //freopen("entrada.txt","r", stdin);
  //freopen("salida.txt","w", stdout);
  int t;

  cin>>t;

  for (int i = 0; i< t; i++)
  {
    int pt[50],n,s,p;
    cin>>n>>s>>p;
    int response = 0;
    for (int j = 0; j<n; j++)
    {
        cin>>pt[j];
    }
    for (int j = 0; j<n; j++)
    {
        //cout<<pt[j]<<"---->"<<(pt[j] % 3)<<endl;

        if (pt[j] == 0) {if (p == 0)response++;continue;}

        if ((pt[j] % 3) == 0)
        {
            if (pt[j]/3 >= p){ response++; continue;}
            if ( ( (pt[j]/3) + 1) >= p && (s>0)) {response++; s--; continue;}
        }
        if ((pt[j] % 3) == 1)
        {
            int divi = floor(pt[j] / 3);
            if (divi+1 >= p) { response++; continue;}
        }
        if ((pt[j] % 3) == 2)
        {
            int divi = floor(pt[j] / 3);
            if (divi + 2 > 10){ response++; continue;}
            if (divi + 1 >= p){ response++; continue;}
            if ((divi + 2 >= p) && (s>0))  {response++; s--; continue;}
        }
    }
    cout<<"Case #"<<(i+1)<<": "<<response<<endl;
  }

}
