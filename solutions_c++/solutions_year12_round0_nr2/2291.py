#include<iostream.h>
#include<stdlib.h>

int compare(const void *a,const void *b)
{
  return(*(int*)b-*(int*)a );
}

int main()
{
    int T=0,arr[101],N,S,p,i,j=1,c,tmp;
    cin>>T;
    while(T>0)
    {
              cin>>N>>S>>p;
              for(i=0;i<N;i++)
                              cin>>arr[i];
              qsort(arr,N,sizeof(int),compare);
              c=0;
              if(p>1)
              {
                     while(arr[c]>(p-1)*3 && c<N)
                          c++;
              }
              else
              {
                  while(arr[c]>=p && c<N)
                                  c++;
              }
              if(p>2)
              {
                     while(arr[c]>(((p-2)*3)+1) && S>0 && c<N)
                     {
                          c++;
                          S--;
                     }
              }
              else
              {
                  while(arr[c]>=p && S>0 && c<N)
                  {
                                  c++;
                                  S--;
                  }
              }
              cout<<"Case #"<<j++<<": "<<c<<"\n";
              T--;
    }
    return 0;
}
