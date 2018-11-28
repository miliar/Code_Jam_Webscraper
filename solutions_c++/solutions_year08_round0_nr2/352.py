#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
#define pb push_back
#define mp make_pair
#define f first
#define s second

int cs,c,na,nb,i,a,b,x,t,v;
bool f;
char str[11];

int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d",&t);
	scanf("%d %d",&na,&nb);
	vector <pair<int,int> > V;
	for(i=0;i<na;i++)
	{
	  scanf("%s",str);
	  V.pb(mp(600*(str[0]-'0')+60*(str[1]-'0')+10*(str[3]-'0')+str[4]-'0',2));
	  scanf("%s",str);
	  V.pb(mp(600*(str[0]-'0')+60*(str[1]-'0')+10*(str[3]-'0')+str[4]-'0'+t,0));
	}
	for(i=0;i<nb;i++)
	{
	  scanf("%s",str);
	  V.pb(mp(600*(str[0]-'0')+60*(str[1]-'0')+10*(str[3]-'0')+str[4]-'0',3));
	  scanf("%s",str);
	  V.pb(mp(600*(str[0]-'0')+60*(str[1]-'0')+10*(str[3]-'0')+str[4]-'0'+t,1));
	}
	sort(V.begin(),V.end());
	v=V.size();
	a=0;
	while(a<na)
	{
	  x=a;
	  f=1;
	  for(i=0;i<v;i++)
	    if(V[i].s==2)
		  if(x==0)
		  {
		    f=0;
			break;;
		  }
		  else
		    x--;
		else if(V[i].s==1)
		  x++;
	  if(f)
	    break;
	  a++;
	}
	b=0;
	while(b<nb)
	{
	  x=b;
	  f=1;
	  for(i=0;i<v;i++)
	    if(V[i].s==3)
		  if(x==0)
		  {
		    f=0;
			break;;
		  }
		  else
		    x--;
		else if(V[i].s==0)
		  x++;
	  if(f)
	    break;
	  b++;
	}
	printf("Case #%d: %d %d\n",c+1,a,b);
  }  
  return 0;
}
