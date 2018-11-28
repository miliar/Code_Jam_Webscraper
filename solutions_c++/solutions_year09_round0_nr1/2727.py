// AlienC.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;
int count=0;
//char t[1000];
string t;
string tocheck;
vector <set<char> > memo(16, set<char>() );
int n;
set<string> myset;
bool mat[15][30][30];

void bt(int ini,int pos){
    int i=0,j;
    int posA;
    int nn=t.length();
    for(i=ini;i<nn;i++)
    {
        if(t[i]=='(')
        {
            for(j=i+1;t[j]!=')';j++){}

            i++;
            while(t[i]!=')')
            {      
                if(pos==0)
                {
                    tocheck[pos]=t[i];                
                    bt(j+1, pos+1);                                
                }
                else if(mat[pos-1][tocheck[pos-1]-'a'][t[i]-'a']==true)
                {
                    tocheck[pos]=t[i];                
                    bt(j+1, pos+1);                                
                    
                }
                i++;
            }
            return;
    
        }
        else
        {
            if(pos==0)
            {
                tocheck[pos]=t[i];
                pos++;
            }
            else if(mat[pos-1][tocheck[pos-1]-'a'][t[i]-'a']==true )
            {
                tocheck[pos]=t[i];
                pos++;
            }
            else
            {
                return;
            }
        }
    }
    
    
    if(myset.count(tocheck)>0){ 
        count++;
    }
    return;

}

int _tmain(int argc, _TCHAR* argv[])
{
    int l,d,i,j;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    memset(mat,false,sizeof(mat));
    scanf("%d%d%d", &l,&d,&n);
    for(i=0;i<d;i++)
    {   
        char tmp[20];
        string stmp;

        scanf("%s",tmp);
        stmp+=tmp;
        myset.insert(stmp);
        
        for(j=0;j<stmp.length()-1;j++)           
            mat[j][tmp[j]-'a'][tmp[j+1]-'a']=true;

    }

    for(i=0;i<n;i++)
    {
             
        
        char tmp[1000];
        memset(&t,0,sizeof(t));
        memset(&tocheck,0,sizeof(t));
        scanf("%s",tmp);
        t.clear();
        t+=tmp;
        tocheck.clear();
        tocheck.resize(l);

        count=0;
        bt(0,0);
    
        printf("Case #%d: %d\n",i+1,count);    
        
    
        
        
        //bt(0);        
        

    }
    

	return 0;
}

