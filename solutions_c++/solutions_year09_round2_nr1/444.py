#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int si[1000];
int no[1000];
int papa[1000];
double val[1000];
string palabra[200];
double prob(int donde,vector<string>&pal)
{  
     if(donde==-1)return 1;
     bool z=0;
     for(int i=0;i<pal.size();i++)if(pal[i]==palabra[donde]){z=true;break;}
     if(donde==0)z=true;
     if(z)
     {
           //cout<<donde<<si[donde]<<" "<<val[donde]<<endl;
           return val[donde]*prob(si[donde],pal);   
     }
     
     //cout<<donde<<no[donde]<<" "<<val[donde]<<endl;
     return val[donde]*prob(no[donde],pal);       
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    scanf("%d\n",&N);
    for(int caso=1;caso<=N;caso++)
    {
        int L;
        char x;
        for(int i=0;i<1000;i++)no[i]=si[i]=val[i]=-1;
        val[0]=1;
        int donde=0;
        int mx=0;
        papa[0]=-1;
        scanf("%d\n",&L);
        int l=0;
        while(l<L)
        {
              scanf("%c",&x);
              if(x=='\n'){l++;continue;}
              if(x==')')
              {
                   donde=papa[donde];     
                   continue;      
              }
              if(x=='(')
              {
                  mx++;
                 
                  scanf("%lf",&val[mx]);
                  // cout<<donde<<mx<<" "<<val[donde]<<endl;
                  if(si[donde]==-1){
                                    si[donde]=mx;
                                    papa[mx]=donde;
                                    }
                  else
                                    {
                                        no[donde]=mx;
                                        papa[mx]=donde;               
                                    }
                  donde=mx;
                  continue;
              }
              if(x<='z'&&x>='a')
              {
                  palabra[donde]="";
                  while(x<='z'&&x>='a')
                  {
                       palabra[donde]+=x;                
                       scanf("%c",&x);                     
                  }
              }
              if(x=='\n'){l++;continue;}
              if(x=='(')
              {
                  mx++;
                  scanf("%lf",&val[mx]);
                  if(si[donde]==-1){
                                    si[donde]=mx;
                                    papa[mx]=donde;
                                    }
                  else
                                    {
                                        no[donde]=mx;
                                        papa[mx]=donde;               
                                    }
                  donde=mx;
                  continue;
              }
                  
                 
        }
        int n;
        scanf("%d\n",&n);
        vector<vector<string> >pal;
        for(int i=0;i<n;i++)
        {
               char A[100];
               scanf("%s",A);
               int p;
               scanf(" %d ",&p);
               vector<string>temp;
               for(int j=0;j<p;j++)
               {
                  scanf("%s",A);     
                  temp.push_back(A);        
               }
               pal.push_back(temp);     
        }
        scanf("\n");
        cout<<"Case #"<<caso<<":\n";
        for(int i=0;i<n;i++)printf("%.7lf\n",prob(0,pal[i]));   
        
            
    }
    return 0;    
}
