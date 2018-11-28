#include<iostream>
using namespace std;
int findchar(char arr[35], int count, char ch);
int main()
{
    int T, C, D, N, pos, oppos, combpos, flag;
    char string[103], oppose[30][2], comb[38][3], combine[38][2], opposing[30], newstr[103];
    cin>>T;
    for(int i=0;i<T;i++)
    {
            cin>>C;
            for(int j=0;j<C;j++)
            {
                    cin>>comb[j];
            }
            cin>>D;
            for(int j=0;j<D;j++)
            {
                    cin>>oppose[j];
            }
            cin>>N;
            cin>>string;
            pos=0;
            oppos=0;
            combpos=0;
            for(int j=0; j<N; j++)
            {
                   flag=1;
                   for(int k=0;k<combpos;k++)
                   {
                           if(string[j]==combine[k][0])
                           {
                                       for(int h=0;h<D;h++)
                                       {
                                               if(findchar(oppose[h],2,string[j-1])>=0)
                                               {
                                                    oppos--;
                                                }
            
                                        }         
                                      pos--;
                                      string[j]=combine[k][1];
                           }
                   }
                   if(findchar(opposing,oppos,string[j])>=0)
                   {
                        pos=0;
                        oppos=0;
                        combpos=0;
                        flag=0;
                    }
                    for(int k=0;k<D&&flag;k++)
                    {
                            if(findchar(oppose[k],2,string[j])>=0)
                            {
                                   if(oppose[k][0]==string[j])
                                  {
                                        opposing[oppos]=oppose[k][1];
                                  }
                                  else
                                  {
                                       opposing[oppos]=oppose[k][0];
                                  }
                                  oppos++;
                            }
                    }  
                    for(int k=0;k<C&&flag;k++)
                    {
                            combpos=0;
                            if(findchar(comb[k],2,string[j])>=0)
                            {
                                  if(comb[k][0]==string[j])
                                  {
                                          combine[combpos][0]=comb[k][1];
                                  }
                                  else
                                  {
                                          combine[combpos][0]=comb[k][0];
                                  }
                                  combine[combpos][1]=comb[k][2];
                                  combpos++;
                            }
                    }  
                    if(flag)
                    {
                            newstr[pos]=string[j];
                             pos++;
                    }         
            }               
            cout<<"Case #"<<i+1<<": [";
            if(pos>0)
            {
                    for(int k=0;k<pos-1;k++)
                    cout<<newstr[k]<<", ";
            cout<<newstr[pos-1]<<"]\n";
            }
            else
                cout<<"]\n";
     }
     return 0;
}
int findchar(char arr[35], int count, char ch)
{
    int flag=-1;
    for(int a=0;a<count;a++)
    {
            if(arr[a]==ch)
                          flag=a;
    }
    return flag;
}
