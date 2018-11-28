#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
const int N = 105;
const double eps = 1e-8;
double r;
struct p{
	double v,len,g;
}o,fr;
bool operator<(const p& A,const p& B)
{    
	return (r-A.g)*((B.g+B.v)*(r+B.v))<(r-B.g)*((A.g+A.v)*(r+A.v))+eps;
}
int V[N],LEN[205];
int main()
{
	//freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T,n,x,a,b,i,j,ca=1;
    double t,v,s;
    scanf("%d",&T);
    while(T--)
    {
    	priority_queue<p>q;
    	scanf("%d%lf%lf%lf%d",&x,&s,&r,&t,&n);
    	for(i=1;i<=x;i++)V[i]=0;
    	for(i=0;i<n;i++)
    	{
    		scanf("%d%d%lf",&a,&b,&v);
    		for(j=a+1;j<=b;j++)
    		{
    			V[j]=v;
    		}
    	}
    	//for(i=1;i<=x;i++)
    		//printf("i:%d v:%d \n",i,V[i]);
    	memset(LEN,0,sizeof(LEN));
  		for(i=1;i<=x;i++)
  			LEN[V[i]]++;
  		for(i=0;i<205;i++)
  			if(LEN[i])
  			{
  				o.v=i;
  				o.g=s;
  				o.len=LEN[i];
  				//printf(" v:%lf  len:%lf \n",o.v+o.g,o.len);
  				q.push(o);
  			}
    	while(t>eps)
    	{
    		fr=q.top();
    		if(fr.g+eps>r)break;
    		q.pop();
    		if(fr.len/(r+fr.v)+eps<t)
    		{
    			fr.g=r;
    			t-=fr.len/(r+fr.v);
    			q.push(fr);
    		}
    		else
    		{
    			fr.len-=t*(r+fr.v);
    			q.push(fr);
    			o.len=t*(r+fr.v);
    			o.g=r;
    			o.v=fr.v;
    			q.push(o);	
    			break;
    		}
    	}
    	double res=0;
    	while(!q.empty())
    	{
    		fr=q.top();
    		q.pop();
    		//printf("fr.v:%lf len:%lf \n",fr.v+fr.g,fr.len);
    		res+=(fr.len/(fr.v+fr.g));
    	}
    	printf("Case #%d: %.9lf\n",ca++,res);
    }	
    return 0;
}
