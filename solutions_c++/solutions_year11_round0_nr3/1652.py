#include<fstream>
using namespace std;
#define D 20
void convert(long x[],int n,int y[][D])
{
     long t;
     for(int i=1;i<=n;i++)
     {
             t=x[i];
             for(int j=0;j<D;j++)
             {
                     y[i][j]=t%2;
                     t=t/2;
                     if(t==0)
                     break;
             }
     }
}
long sumV(int a[][D],int V,int n)
{
     long t=0;
     for(int i=1;i<=n;i++)
     t+=a[i][V];
     return t;
}                     
long Min(long a[],int x)
{
     long temp=a[1];
     for(int i=2;i<=x;i++)
     if(temp>a[i])
     temp=a[i];
     return temp;
}     
int main()
{
    ifstream in("C-large.in");
    ofstream out("out.txt");
    int T;
    in>>T;
    int N;//num of integers
    long sum=0;
    long temp;
    long dec[1200]={0};;
    int bin[1200][D]={0};
    int result[110]={0};
    for(int i=0;i<T;i++)
    {
            in>>N;
            sum=0;
            for(int j=1;j<=N;j++)
            {
                    in>>temp;
                    dec[j]=temp;
                    sum+=temp;
            }
            convert(dec,N,bin);
            for(int j=0;j<D;j++)
            if(sumV(bin,j,N)%2==1)
            {
                                   result[i]=-1;
                                  break;
                                 
            }
            if(result[i]!=-1)
            result[i]=sum-Min(dec,N);
            for(int j=1;j<=N;j++)
            {
                    dec[j]=0;
                    for(int x=0;x<D;x++)
                    bin[j][x]=0;
            }
    }
    for(int i=0;i<T;i++)
    {
            out<<"Case #"<<i+1<<": ";
            if(result[i]==-1)
            out<<"NO";
            else
            out<<result[i];
            out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
            
            
            
            
            
             
    
    
