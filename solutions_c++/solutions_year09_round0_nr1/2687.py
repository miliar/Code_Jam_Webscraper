#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

int main()
{
    int l,d,n;
    
    
    
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    
    in>>l>>d;
    in>>n;
    int a[l][2];
    
    /*for(int i=0;i<l;i++)
    {
            a[i][1]=0;
            a[i][2]=0;
    }*/
    
    string w[d];
    for(int i=0;i<d;i++)
    in>>w[i];
    /*for(int i=0;i<d;i++)
    {
            for(int j=0;j<d-1-i;j++)
            {
                    if(w[j]>w[j+1])
                    {
                                   string temp=w[j];
                                   w[i]=w[j+1];
                                   w[j+1]=temp;
                    }
            }
    }*/
    
    
    string test;
    for(int i=0;i<n;i++)
    {
            in>>test;
            int t=0,total=1,ok=0;
            
            for(int j=0;test[j]!='\0';j++)
            {
                    if(test[j]!='(' && test[j]!=')')
                    {
                                    a[t][1]=j;
                                    a[t][2]=1;
                                    t++;
                    }
                    else if(test[j]=='(')
                    {
                         j++;
                         a[t][1]=j;
                         int count=0;
                         while(test[j]!=')')
                         {
                                            count++;
                                            j++;
                         }
                         a[t][2]=count;
                         t++;
                    }
            }
            for(int j=0;j<d;j++)
            {
                    int signal=0;
                    for(int k=0;k<l;k++)
                    {
                            signal=0;
                            for(int v=0;v<a[k][2];v++)
                            {
                                    int temp=a[k][1]+v;
                                    if(test[temp]==w[j][k])
                                    {signal=1;break;}
                            }
                            if(signal!=1)
                            break;
                    }
                    if(signal==1)
                    ok=ok+1;
            }
            out<<"Case #"<<i+1<<": "<<ok<<endl;
                         
            
    }
    
    
    
    
    in.close();
    out.close();
    system("pause");
    return 0;
}
