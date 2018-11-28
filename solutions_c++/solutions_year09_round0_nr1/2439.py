#include <iostream>
#include <string>
#include <vector>

using namespace std;

int busca(vector <string> mapa, const string &a,string b,int pos,int apos)
{
    if( mapa.size()==0 )
    {
	   return 0;
    }
    if(pos==a.size())
    {
	   if(mapa[0]==b)
	   {
		  return 1;
	   }
	   return 0;
    }
    if(a[pos]=='(')
    {
	   int i, j, w, ans=0;
	   for(w=pos+1; a[w]!=')'; w++)
	   {		  
	   }
	   w++;
	   vector <string> mapaO=mapa;
	   for(i=pos+1; a[i]!=')'; i++)
	   {
		  mapa=mapaO;
		  for(j=0; j<mapa.size(); j++)
		  {
			 if(mapa[j][apos]!=a[i])
			 {
				mapa.erase(mapa.begin()+j);
				j=0;
			 }
		  }
		  ans+=busca(mapa,a,b+a[i],w,apos+1);
	   }
	   return ans;
    }
    int i;
    for(i=0; i<mapa.size(); i++)
    {
	   if(mapa[i][apos]!=a[pos])
	   {
		  mapa.erase(mapa.begin()+i);
		  i--;
	   }
    }
    return busca(mapa,a,b+a[pos],pos+1,apos+1);
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int n, d, l;
    int i, j;
    vector <string> mapa;
    string a;
    scanf("%d%d%d",&l,&d,&n);
    for(i=0; i<d; i++)
    {
	   cin >> a;
	   mapa.push_back(a);
    }
    for(i=1; i<=n; i++)
    {
	   cin >> a;
	   printf( "Case #%d: %d\n",i,busca(mapa,a,"",0,0) );
    }
    return 0;
}