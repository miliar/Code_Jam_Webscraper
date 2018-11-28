#include <iostream>

using namespace std;

int gcd (int m,int n)  
{  
  if (m > n) swap(m,n); 
  while(n > 0) { 
        int r = m % n; 
        m = n; 
        n = r; 
  } 
  return m; 
} 

int main()
{
    FILE *fin;
    FILE *fout;
    fin=fopen("A-large.in","r");
    fout=fopen("A-large.out","w");
    long long n;
    int t,pd,pg,g,answer;
    int a[101];
    for (int i=1;i<=100;++i)
       a[i]=100/gcd(i,100);
       for (int i=1;i<=100;++i)        
       cout<<i<<" "<<a[i]<<endl;
    fscanf(fin,"%d",&t);
    //cin>>t;
    for (int i=1;i<=t;++i)
    {
        n=0;
        fscanf(fin,"%d%d%d",&n,&pd,&pg);
        //cin>>n>>pd>>pg;
        if(pg==100 && pd!=100)
        {
            fprintf(fout,"Case #%d: Broken\n",i);
            continue;
        }
        if(pg==0 && pd!=0)
        {
            fprintf(fout,"Case #%d: Broken\n",i);
            continue;
        }
        if(pg==0 && pd==0)
        {
            fprintf(fout,"Case #%d: Possible\n",i);
            continue;
        }
        if(n>100)
        {
            fprintf(fout,"Case #%d: Possible\n",i);
            continue;
        }
        if(n<a[pd])
        {
            fprintf(fout,"Case #%d: Broken\n",i);
            continue;
        }
        else
        {            
            fprintf(fout,"Case #%d: Possible\n",i);
            continue;
        }

    }
    system("pause");
}

