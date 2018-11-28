#include<fstream>
using namespace std;
void clear(char *a,int n)
{
     for(int i=1;i<=n;i++)
     a[i]=0;
}
int jbin(char *a, int i, char b[][4],int x)//judge
{
     for(int j=1;j<=x;j++)
     {
             if(a[i]==b[j][1]&&a[i-1]==b[j][2])
             return j;
             if(a[i]==b[j][2]&&a[i-1]==b[j][1])
             return j;
     }
     return 0;
}
void replace(char *a,int i,char b[][4],int x)
{
     if(a[i]==b[x][1]||a[i]==b[x][2])
     {
                                     a[i-1]=b[x][3];
                                     a[i]=0;
     }
}     
bool jopp(char* a,int i,char b[][3], int x)
{
          for(int j=1;j<=x;j++)
          {
          for(int n=1;n<i;n++)
          if((a[i]==b[j][1]&&a[n]==b[j][2])||(a[i]==b[j][2]&&a[n]==b[j][1]))
          return true;
          }
          return false;
}
          
int main()
{
    ifstream in("B-large.in");
    ofstream out("out.txt");
    int T;
    int temp;
    in>>T;
    int C,D,N;
    char c;
    char bin[50][4]={0},opp[50][3]={0};
    char sam[101][150]={0};
    for(int i=0;i<T;i++)
    {
            in>>C;
            for(int j=1;j<=C;j++)
            {
                    in>>c;
                    bin[j][1]=c;
                    in>>c;
                    bin[j][2]=c;
                    in>>c;
                    bin[j][3]=c;
            }
            in>>D;
            for(int j=1;j<=D;j++)
            {
                    in>>c;
                    opp[j][1]=c;
                    in>>c;
                    opp[j][2]=c;
            }
            in>>N;
            for(int j=1;j<=N;j++)
            in>>sam[i][j];
            for(int x=1;x<=N;x++)
            {
                    if(temp=jbin(sam[i],x,bin,C))
                    {
                                                 replace(sam[i],x,bin,temp);
                                                 continue;
                    }
                    if(jopp(sam[i],x,opp,D))
                    clear(sam[i],x);
            }
            for(int val=1;val<=C;val++)
            {
                    bin[val][1]=0;
                    bin[val][2]=0;
                    bin[val][3]=0;
            }
            for(int val=1;val<=D;val++)
            {
                    opp[val][1]=0;
                    opp[val][2]=0;
            }
    }
    for(int i=0;i<T;i++)
    {
            out<<"Case #"<<i+1<<": [";
            for(int j=1,p=0;j<150;j++)
                    if(p==0&&sam[i][j])
                    {
                                       out<<sam[i][j];
                                       p++;
                    }
            else if(sam[i][j]!=0)
            out<<", "<<sam[i][j];
            out<<"]"<<endl;
    }
    in.close();
    out.close();
    return 0;
}
            
                    
                    
                    
                    
            
            
    
