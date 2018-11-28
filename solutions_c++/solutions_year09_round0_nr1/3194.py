#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
   // freopen("A-small.in", "rt", stdin);
freopen("A-small.out", "wt", stdout);
	
	int l,d,n;
	cin>>l>>d>>n;
      const int L=l,D=d,N=n;
char dictionary[D][L];

  
  //  cin>>L>>D>>N;
    for(int i=0;i<D;i++)
    {
            cin>>dictionary[i];
            
    }
    
    
    char token[N][600];
    
     for(int i=0;i<N;i++)
    {
            cin>>token[i];
            
    } //cout<<endl<<token[1][2];
  //hhhh
    char str[N][L][27];
    str[0][0][0]=token[1][2];
    
    for(int j=0;j<N;j++)
    {
    int k=0,flag=0;
      int x=0;
      while(x<L)
      {
      if(token[j][k]=='(' )
        {flag=1; k++;}
      if(token[j][k]==')')
      {flag=0;  k++;x++;}
      if(flag==1)
      {   int y=0;
          while(token[j][k] != ')')
          { 
          str[j][x][y++]=token[j][k++];                    
          }       
      }       
      if(flag==0 && token[j][k]!='(')
      {
      str[j][x++][0]=token[j][k++]; 
      //str[j][x-1][1]='\0';          
      }           
      }
        
    }
   // cout<<endl<<str[0][2][2]<<endl<<str[1][2][0]<<endl<<str[2][2][0]<<endl<<str[3][2][0]<<endl<<endl;
  //ygi 
    for(int x=0;x<N;x++)
    {
               int count=0,true1;
                   for(int i=0;i<D;i++)
                      { true1=0;
                          for(int j=0;j<L;j++)
                          {
                                for(int y=0;y<26;y++)
                                    {
                                      if(dictionary[i][j]==str[x][j][y])
                                        {true1++;  break;}            
                                    }                
                          }      
                         if(true1==L)
                         {
                          count++; 
                                
                         }
                     }    
                       cout<<"Case #"<<x+1<<": "<<count<<endl;             
    }
   
      system("PAUSE");
    return EXIT_SUCCESS;
}
