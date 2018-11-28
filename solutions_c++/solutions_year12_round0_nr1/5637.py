#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

char normal[] = {" abcdefghijklmnopqrstuvwxyz"};
char trans[] = { " ynficwlbkuomxsevzpdrjgthaq"};


int main()
{
  freopen("entrada.txt","r", stdin);
  freopen("salida.txt","w", stdout);
  int t;
  cin>>t;
  char end[120];
  cin.getline(end,110);
  for (int i = 0; i< t; i++)
  {
      cout<<"Case #"<<(i+1)<<": ";
      char g[120];
      cin.getline(g,110);
        //cout<<g;
      for (int j = 0; j<strlen(g); j++)
      {
          for (int k = 0;k<strlen(trans);k++)
            if (trans[k] == g[j])
            {
                cout<<(char)normal[k];
                break;
            }

      }
      cout<<endl;
  }
}
