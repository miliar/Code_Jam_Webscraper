#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
struct point
{
   int startime;
   int endtime;
   int flag;
   bool counted;
   bool operator < (const point Q) const
   {
      return startime<Q.startime||(endtime<Q.endtime&&startime==Q.startime);
   }
}p1;
typedef vector<point> VP;
int gettime(string str)
{
    return ((str[0]-'0')*10+(str[1]-'0'))*60+(str[3]-'0')*10+(str[4]-'0');
}
int main()
{
	freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);
	int i,j,Case,num ,NA,NB,T,ansa,ansb;
	VP train;
	string str1,str2;
	cin>>Case;  	 
	num=1;
	while (Case--)
	{
	    cin>>T>>NA>>NB;
        train.clear();
		ansa=0;
		ansb=0;
		p1.flag=0;
		p1.counted=true;
		for (i=0;i<NA;i++)
		{
          cin>>str1>>str2;
		  p1.startime=gettime(str1);
		  p1.endtime=gettime(str2);
		  train.push_back(p1);  
		}
		p1.flag=1;
		for (i=0;i<NB;i++)
		{
          cin>>str1>>str2;
		  p1.startime=gettime(str1);
		  p1.endtime=gettime(str2);
		  train.push_back(p1);  
		}
		sort(train.begin(),train.end());
		for(i=0;i<train.size();i++)
		{
			if(train[i].counted)
			{
			  if(train[i].flag==0)
				  ansa++;
			  else if(train[i].flag==1)
				  ansb++;
			}
			for(j=i+1;j<train.size();j++)
			{
			   if(!train[j].counted)
				   continue;
			   if(train[i].flag!=train[j].flag)
			   {
				   if(train[i].endtime+T<=train[j].startime)
				   {
					  train[j].counted=false;
                      break;				   
				   }
			   }
			}
		}
		printf("Case #%d: %d %d\n",num++,ansa,ansb);	
	}
	return 0; 
}