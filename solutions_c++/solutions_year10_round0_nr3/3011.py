#include<iostream>
#include<fstream>

using namespace std;
int main()
{
    int T,R,k,N,i,j=0,l,x=0,xold=0,cena,y,m,z,v=0,s=0;
    int* tab;
    ifstream input;
    ofstream output;
    input.open("C-small.in");
    output.open("plik2.txt");
    input>>T;
    for(i=0;i<T;i++)
    {
                    cena=0;
                    input>>R;
                    input>>k;
                    input>>N;
                    tab = new int [N];
                    for(j=0;j<N;j++)
                    {
                                    input>>tab[j];
                    }
                    for(l=0;l<R;l++)
                    {
                                    v=0;
                                    x=0;
                                    while((v<N)&&(k>=x))
                                    {
                                              xold=x;
                                              x+=tab[v];
                                              y=v;
                                              v++;
                                    }
                                  if(k<x) cena+=xold;
                                  else cena+=x;
                                  //cout<<cena<<" ";
                                  for(m=0;m<y;m++)
                                  {
                                                   s=0;
                                                   while(s<N-1)
                                                   {
                                                            z=tab[s];
                                                            tab[s]=tab[s+1];
                                                            tab[s+1]=z;
                                                            s++;
                                                   }
                                  }
                    }
                    output<<"Case #"<<i+1<<": "<<cena<<endl;
    }
    system("pause");
    return 0;
}
