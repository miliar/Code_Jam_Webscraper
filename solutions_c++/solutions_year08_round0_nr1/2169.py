#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;

int find_switches(string s[],string q[], int srch, int qu)
{
    int *freq = new int[srch];
    int *order = new int[srch]; 
    for(int i=0;i<srch;i++)
    {freq[i]=0;order[i]=0;}
    cout<<freq[0]<<endl;  
    int switches =0;
    for(int j=0;j<qu;j++)
    {
            for(int i=0,p=0;i<srch;i++)
             {
                    if(!s[i].compare(q[j]))
                     {
                            if(j!=0)
                                    if(s[i].compare(q[j-1]))
                                    {++freq[i] ;p=1;}
                                    else p=0;
                            else ++freq[i];
                     }
                     int x=1;
                     for(int k=0;k<srch;k++)
                     {
                             if(freq[k]==0) x=0;
                     }
                     if(x==1)
                     {
                             switches++;
                             for(int k=0;k<srch;k++)
                             {
                                     if(k!=i)
                                     freq[k]=0;
                             }         
                     }
             }
            //order[i]=i;   
    }  
    /*for(int i=0;i<srch;i++)
    {
            for(int j=i+1;j<srch-i;j++)
                    if(freq[i]>freq[j])
                       order[i]^=order[j]^=order[i]^=order[j];
    }
    */
    return switches;
    for(int j=0;j<srch;j++)
            cout<<order[j]<<"\n";
    cout<<"------------";
}

int main()
{
    ifstream ip("A-large.in");
    ofstream op("output.txt");
    int test = 0;
    int search = 0;
    int query = 0;
    string *s,*q;
    ip>>test;
    //cout<<test;
    for(int i=0;i<test; i++)
    {
            ip>>search;
            //cout<<"\ns="<<search;
            s = new string[search];
            char temp[101];
            ip.getline(temp,101);
            for(int j=0;j<search;j++)
            {
                    ip.getline(temp,101);
                    s[j]=temp;
                    //cout<<s[j]<<endl;
            }
            ip>>query;
            q = new string[query];
            ip.getline(temp,101);
            //cout<<"q="<<query;
            for(int j=0;j<query;j++)
            {
                    char temp[101];
                    ip.getline(temp,101);
                    q[j]=temp;
                    //cout<<q[j]<<endl;
            }
            op<<"Case #"<<i+1<<": "<<find_switches(s,q,search,query)<<endl;
            delete s,q;
    }    
    ip.close();
    op.close();
     
    getch();
}
