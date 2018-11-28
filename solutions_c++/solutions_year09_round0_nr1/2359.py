#include <stdio.h>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

map <string,bool> k;
vector <vector <string> > x;
map <char,bool> kk[100];

int cosa(int pos,string f,int y)
{
    //cout<<f<<"\n";
    if(k[f]==false)
        return 0;
    if(pos==x[y].size())
    {
        if(k[f])
            return 1;
        else
            return 0;
    }
    int res=0;
    for(int i=0;i<x[y][pos].size();i++)
         if(kk[pos][x[y][pos][i]])
            res+=cosa(pos+1,f+x[y][pos][i],y);   
    return res;   
}

int main()
{
    int l,d,n;
    freopen("A.txt","r",stdin);
    scanf("%d%d%d\n",&l,&d,&n);
     freopen("input.txt","w",stdout);

    string aux;
    k[""]=true;
    for(int i=0;i<d;i++)
    {
        cin>>aux;
        for(int j=0;j<aux.size();j++)
            kk[j][aux[j]]=true;   
        string aux2="";
        for(int j=0;j<aux.size();j++)
        {
            aux2+=aux[j];
            k[aux2]=true; 
          //  cout<<aux2<<"\n";  
        }
        k[aux]=true;
    }
   
    for(int i=0;i<n;i++)
    {
        cin>>aux;
        vector <string> xx;
        for(int j=0,jj=0;j<aux.size();j++,jj++)
        {
          //  cout<<jj<<"\n";
            if(aux[j]=='(')
            {
                j++;
                xx.push_back("");
                if(kk[jj][aux[j]])
                    xx[xx.size()-1]+=aux[j];
                j++;
                while(aux[j]!=')')
                { 
                     if(kk[jj][aux[j]])
                        xx[xx.size()-1]+=aux[j];
                      j++;
                }
            }
            else
            {
                    
                xx.push_back("");
                if(kk[jj][aux[j]])
                    xx[xx.size()-1]+=aux[j];
            }      
        }
      
        x.push_back(xx);
        int res=cosa(0,"",i);
        
        printf("Case #%d: %d\n",i+1,res);
    }
    return 0;
}   
