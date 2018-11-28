#define DIM 110
#include<iostream>
#include<fstream>
using namespace std;

    char code[DIM][DIM];
    int altitude[DIM][DIM];
    bool visited[DIM][DIM];
    int T,W,H;
    char nextcode='b';

class point
{
      public:
             int x,y;
};

void printcode()
{
 int l,m;
                                  for(l=0;l<H;l++)
                             {
                              for(m=0;m<W;m++)
                              {
                                    cout<<code[l][m];
                                    if(m!=W-1)
                                    cout<<" ";
                              }
                              cout<<"\n";
                              }
                              }


inline point willflow(int j,int k)
{
                          int smallj=j;
                         int smallk=k;
                         point temp;
                         if(j>0 && altitude[smallj][smallk]>altitude[j-1][k])
                         {
                                smallj=j-1;
                                smallk=k;
                         }
                         if(j<(H-1)&& altitude[smallj][smallk]>altitude[j+1][k])              
                         {
                                      smallj=j+1;
                                      smallk=k;
                         }
                         if(k>0 && altitude[smallj][smallk]>altitude[j][k-1])
                         {
                                smallk=k-1;
                                smallj=j;
                         }
                         if(k<(W-1) && altitude[smallj][smallk]>altitude[j][k+1])
                         {
                                    smallk=k+1;
                                    smallj=j;
                         }
                                               if(altitude[j][k]==altitude[smallj][smallk])
                                               {
                                                                                           temp.x=j;
                                                                                           temp.y=k;
                                               }
                                               else if(j>0 && altitude[j-1][k]==altitude[smallj][smallk])
                                               {
                                                      temp.x=j-1;
                                                      temp.y=k;
                                               }
                                               else if(k>0 && altitude[j][k-1]==altitude[smallj][smallk])
                                               {
                                                      temp.x=j;
                                                      temp.y=k-1;
                                               }
                                               else if(k<(W-1) && altitude[j][k+1]==altitude[smallj][smallk])
                                               {
                                                    temp.x=j;
                                                    temp.y=k+1;
                                               }
                                               else if(j<(H-1) && altitude[j+1][k]==altitude[smallj][smallk])
                                               {
                                                    temp.x=j+1;
                                                    temp.y=k;
                                               }
                                               return temp;

}

void colorarena(int j,int k)
{
                                  //  cout<<"\n colorarena called with "<<j<<" "<<k;
                                    if(visited[j][k]==true)
                                    return;
                                    visited[j][k]=true;
                                    point currentpoint=willflow(j,k);
                                    point temppoint;
                                    code[currentpoint.x][currentpoint.y]=code[j][k];
                                    //cout<<"\n"<<j<<" "<<k<<" "<<currentpoint.x<<" "<<currentpoint.y<<"\n";
                                    //printcode();
                                                         if(j>0)
                                                         {
                                                                temppoint=willflow(j-1,k);
                                                                    if(temppoint.x==j && temppoint.y==k)
                                                                    {
                                                                                      code[j-1][k]=code[j][k];
                                                                                      
                                                                                      colorarena(j-1,k);
                                                                    }
                                                         }           
                                                         if(j<(H-1))
                                                         {
                                                                    temppoint=willflow(j+1,k);
                                                                    if(temppoint.x==j && temppoint.y==k)
                                                                    {
                                                                                      code[j+1][k]=code[j][k];
                                                                                      colorarena(j+1,k);
                                                                    }
                                                         }
                                                         if(k>0)
                                                         {
                                                                temppoint=willflow(j,k-1);
                                                                if(temppoint.x==j && temppoint.y==k)
                                                                {
                                                                                  code[j][k-1]=code[j][k];
                                                                                  colorarena(j,k-1);
                                                                }
                                                         }
                                                         if(k<(W-1))
                                                         {
                                                                    temppoint=willflow(j,k+1);
                                                                    if(temppoint.x==j && temppoint.y==k)
                                                                    {
                                                                    code[j][k+1]=code[j][k];
                                                                    colorarena(j,k+1);
                                                                    }
                                                         }
                                    colorarena(currentpoint.x,currentpoint.y);
     
}
int main()
{

    int smallj,smallk;
    int i,j,k,l,m,n;
    ifstream input("input.txt");
    ofstream output("output.txt");
    input>>T;
    //cout<<T;
    point currentpoint;
    point temppoint;
    for(i=0;i<T;i++)
    {
                    input>>H>>W;
                    //cin>>n;
                    //cout<<"\n New turn";
                    for(j=0;j<H;j++)
                    {
                                    for(k=0;k<W;k++)
                                    {
                                                    input>>altitude[j][k];
                                                    code[j][k]=0;
                                                    visited[j][k]=false;
                                    }
                    }
    nextcode='b';
    code[0][0]='a';
    colorarena(0,0);
    for(j=0;j<H;j++)
    {
                    for(k=0;k<W;k++)
                    {
                                   //cout<<"\n IN THE LOOP";
                                    if(code[j][k]==0)
                                    {
                                                     
                                                     code[j][k]=nextcode++;
                                                     colorarena(j,k);
                                                  //  printcode();
                                                     
                                    }                                                   

                                    
                    }
    }
   // printcode();
    output<<"Case #"<<(i+1)<<": \n";
    for(j=0;j<H;j++)
    {
                    for(k=0;k<W;k++)
                    {
                                    output<<code[j][k];
                                    if(k!=W-1)
                                    output<<" ";
                    }
                    output<<"\n";
    }
}
 
return 0;
}                                                      
                                               
