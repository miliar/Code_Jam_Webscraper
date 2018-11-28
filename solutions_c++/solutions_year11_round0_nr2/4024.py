#include <iostream>

#include <algorithm>
#include <string>
#include <stack>
#include <deque>
#include <cstring>
#include <cstdio>
#include <vector>
 
using namespace std;
 
 
int main()
{
        freopen("B-small-attempt4.in","r",stdin);
        freopen("output.txt","w",stdout);
 
        int t;
 
cin>>t;
        for(int q=0;q<t;q++)
        {
	int c,d,n;char ne[101],set[9990],ret[204];
                int com[27][27],op[27][27];
        for(int a=0;a<26;a++)
        for(int b=0;b<26;b++)
        com[a][b]=op[a][b]=0;
gets(set);
        
                c=set[0]-'0';int v=4;if(c!=0)
          
                {
                com[set[2]-65][set[3]-65]=com[set[3]-65][set[2]-65]=set[4];v=8;d=set[v-2]-'0';}
                else d=set[v-2]-'0';
                if(d!=0)
                
                {op[set[v]-65][set[v+1]-65]=op[set[v+1]-65][set[v]-65]=1;v+=5;}else v+=2;
                if(c==0 && d==0)
                v=4;
                else
                if(c!=0 && d==0)
                v=8;
                else if(c==0 && d!=0)
                v=7;
                else if(c!=0 && d!=0)
                v=11;
                if(set[v+1]=='0')
                {n=10;v+=3;}
                else
                {n=set[v]-'0';v+=2;}
                int rr;for(rr=0;rr<n;rr++)
                ne[rr]=set[v++];ne[rr]='\0';
                for(int z=1;z<n;z++)
                for(int zz=z-1;zz>=0;zz--)
                if(ne[zz]!='0')
                {
                        if(com[ne[z]-65][ne[zz]-65]!=0)
                        {ne[zz]=com[ne[z]-65][ne[zz]-65];ne[z]='0';zz=-1;break;}
                        
                        for(int zzz=z;zzz>=0;zzz--)
                        if(op[ne[z]-65][ne[zzz]-65]==1)
                        {for(int zzzz=z;zzzz>=0;zzzz--)ne[zzzz]='0';zz=-1;}zz=-1;
                }
                ret[0]='['; int k=1;int g=0;
                        for(int mn=0;mn<n;mn++)
                        if(ne[mn]!='0')g++;
if(g==0)
                {ret[k]=']';ret[++k]='\0';}
else
                for(int aa=0;aa<=n;aa++)
                {                       
                        if(ne[aa]!='0' && ne[aa]!='\0')
                        {ret[k++]=ne[aa];ret[k++]=',';ret[k++]=' ';}
                        else
if(ne[aa-1]!='0' && ne[aa]=='\0')
                        {ret[k-2]=']';ret[--k]='\0';}
                        else
if(ne[aa-1]=='0' && ne[aa]=='\0')
                        {ret[k-2]=']';ret[--k]='\0';}
                        
                }       
 
                cout<<"Case #"<<q+1<<": "<<(ret)<<endl; 
        }
return 0;
};