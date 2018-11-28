#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
using namespace std;
struct nodo{
 double val;
 int name;
 int izq,der;
 };
 nodo arbol[10000];
 char pal[1000];
 int h,ID,MID;
 map< string, int > ma;
 vector < double > v;
 void make(int id)
 {
    if( v[h++]==-1 )
    {
      arbol[id].val=v[h++];
      if( v[h]==-2 )
       arbol[id].name=-(1<<30);
      else
       {
          arbol[id].name=(int)v[h++];
          ID++;
          arbol[id].izq=ID;
          make( ID );
          ID++;
          arbol[id].der=ID;
          make( ID );          
       }
       h++;
    }
 }
 
 void mete(string s)
  {
     if(!s.size())    
      return;
     if(  s=="(" )
      v.push_back(-1);
     else
     if(s==")")
     v.push_back(-2);
     else
     if(s[0]>='0' && s[0]<='9')
      {
         double temp;
         sscanf(s.c_str(),"%lf",&temp);
         v.push_back(temp);
      }
     else
     {
         if(  !ma.count(s) )    
          ma[s]=MID--;
          v.push_back(ma[s]);
     }
  }
 double busca(int nod, set < int > vt)
  {
      if(  vt.count( arbol[nod].name ) )
       {
           if( arbol[nod].name==-(1<<30) )    
            return arbol[nod].val;
           return arbol[nod].val*busca(  arbol[nod].izq,vt );
       }
      else
       {
           if( arbol[nod].name==-(1<<30) )    
            return arbol[nod].val;
           return arbol[nod].val*busca(  arbol[nod].der,vt );
       }       
  }
int main()
{
    int n,m,l,p;
    gets(pal);
    sscanf(pal,"%d",&n);
    for(int j=0;j<n;j++)
     {
            h=ID=0;
            MID=-3;
            v.clear();
            ma.clear();
        if(j)
       gets(pal);
       gets(pal);
       sscanf(pal,"%d",&m);
     //  printf("MMM %d\n",m);
        for(int k=0;k<m;k++)
         {
            gets(pal);
            string s=pal,ss;
            for(int r=0;r<s.size();r++)    
             {
                if( s[r]==' ' )
                  mete(ss),ss="";
                else
                if( s[r]=='(' )
                mete(ss),mete("("),ss="";
                else
                if( s[r]==')' )
                mete(ss),mete(")"),ss="";                
                else
                ss+=s[r];
             }
             mete(ss);
         }
         make(0);
         scanf("%d",&l);
         printf("Case #%d:\n",j+1);
         for(int r=0;r<l;r++)
         {
           set< int > vt;
           scanf("%s",pal);
           scanf("%d",&p);
            for(int c=0;c<p;c++)
            {
               scanf("%s",pal);
               string ss=pal;   

               if( !ma.count(ss) )
                ma[ss]=MID--;
               vt.insert(ma[ss]);
            }
           printf("%lf\n",busca(0,vt));
         }
     }
}
