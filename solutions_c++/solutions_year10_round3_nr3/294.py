#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctime>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

int a[255];
void init()
{
    a['0']=0;
    a['1']=1;
    a['2']=2;
    a['3']=3;
    a['4']=4;
    a['5']=5;
    a['6']=6;
    a['7']=7;
    a['8']=8;
    a['9']=9;
    a['A']=10;
    a['B']=11;
    a['C']=12;
    a['D']=13;
    a['E']=14;
    a['F']=15;
}
int main() 
{ 
//    freopen("..\\A.in","r",stdin); 
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout); 
//   freopen("A-small-practice.in","r",stdin);freopen("A-small-practice.out","w",stdout); 
//    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout); 
//    freopen("..\\A-small.in","r",stdin);freopen("..\\A-small.out","w",stdout);
    int T;
    int M,N;
    init();
    while (scanf ("%d",&T)!=EOF)
    {
          for (int count=1;count<=T;count++)
          {
                cin>>M>>N;
                vector <string> s;
                for (int i=0;i<M;i++)
                {
                    string temp;
                    cin>>temp;
                    string t="";
                    //cout<<temp<<endl;
                    for (int j=0;j<temp.size();j++)
                    {
                        int num=a[temp[j]];
                        //cout<<num<<endl;
                        //system("pause");
                        string tt="";
                        for (int k=0;k<4;k++)
                        {
                            
                            if (num%2==0)
                                tt+="0";
                            else
                                tt+="1";
                            //cout<<tt<<endl;
                            
                            num=num/2;    
                        }    
                        reverse(tt.begin(),tt.end());
                        t+=tt;
                    }
                    s.push_back(t);
                    
                }
                /*for (int i=0;i<M;i++)
                {
                    for (int j=0;j<N;j++)
                        cout<<s[i][j];
                    cout<<endl;
                }*/
                bool flag[M][N];
                memset(flag,0,sizeof(flag));
                vector <int> maxSize;
                vector <int> maxNum;
                int Size,Num;
                int res=0;
                Size=min(M,N);
                for (int k=Size;k>=1;k--)
                {
                    Num=0;
                    for (int i=0;i<M-k+1;i++)
                    {
                        for (int j=0;j<N-k+1;j++)
                        {
                                bool f=true;
                                for (int l=i;l<k+i;l++)
                                {
                                    for (int m=j;m<k+j;m++)
                                    {
                                        f=!flag[l][m];
                                        if (m+1<k+j&&s[l][m]==s[l][m+1]&&flag[l][m]==false)
                                            f=false;
                                        else if (l+1<k+i&&s[l][m]==s[l+1][m]&&flag[l][m]==false)
                                            f=false;
                                        if (f==false)
                                            break;
                                        
                                    }    
                                    if (f==false)
                                    
                                        break;
                                }
                                if (f==true)
                                {
                                    Num++;
                                    for (int l=i;l<k+i;l++)
                                        for (int m=j;m<k+j;m++)
                                            flag[l][m]=true;
                                       // cout<<endl;
                                    /*for (int l=0;l<M;l++)
                                    {
                                        for(int m=0;m<N;m++)
                                            cout<<flag[l][m];
                                        cout<<endl;
                                        
                                    } */  
                                    //system("pause"); 
                                }
                        }    
                    }
                    if (Num!=0)
                    {
                        res++;
                        maxSize.push_back(k);
                        maxNum.push_back(Num);    
                    }
                }   
              cout<<"Case #"<<count<<": "<<res<<endl;
              for (int i=0;i<maxSize.size();i++)
                cout<<maxSize[i]<<" "<<maxNum[i]<<endl;
          }      
    }
    return 0; 
} 



                 
