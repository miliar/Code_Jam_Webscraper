#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<stdio.h>

using namespace std;
int main()
{
	int t,i,timeout,na,nb,total;
	int hr,min,time;
	int val1,val2,as,bs,ac,bc;
	char stemp[20];
	
	int c=1;
	
	FILE *f1,*f2;
	f1=fopen("B-large.in","r");
	f2=fopen("B-large.out","w");
	
	fscanf(f1,"%d\n",&t);
	while(t--)
	{
		vector < pair < int , pair < int , int > > > v;
		
		fscanf(f1,"%d\n",&timeout);
		fscanf(f1,"%d %d\n",&na,&nb);
		
		for(i=0;i<na;i++)
		{
			fgets(stemp,256,f1);
			hr=(stemp[0]-'0')*10+(stemp[1]-'0');
			min=(stemp[3]-'0')*10+(stemp[4]-'0');
			time=hr*60+min;
			v.push_back( make_pair( time, make_pair( 1 , 0 )));
			
			hr=(stemp[6]-'0')*10+(stemp[7]-'0');
			min=(stemp[9]-'0')*10+(stemp[10]-'0');
			time=hr*60+min+timeout;
			v.push_back( make_pair( time, make_pair( 0 , 2 )));
		}
		for(i=0;i<nb;i++)
		{
			fgets(stemp,256,f1);
			hr=(stemp[0]-'0')*10+(stemp[1]-'0');
			min=(stemp[3]-'0')*10+(stemp[4]-'0');
			time=hr*60+min;
			v.push_back( make_pair( time, make_pair( 2 , 0 )));
			
			hr=(stemp[6]-'0')*10+(stemp[7]-'0');
			min=(stemp[9]-'0')*10+(stemp[10]-'0');
			time=hr*60+min+timeout;
			v.push_back( make_pair( time, make_pair( 0 , 1 )));
		}
		
		sort(v.begin(), v.end());
		
		total=na+nb;
		as=bs=ac=bc=0;
		for(i=0;i<2*total;i++)
		{
			val1=v[i].second.first;
			val2=v[i].second.second;
			
			switch(val1)
			{
				case 0:
					if(val2==1) as++;
					if(val2==2) bs++;
					break;
				case 1:
					if(as==0) ac++;
					else as--;
					break;
				case 2:
					if(bs==0) bc++;
					else bs--;
					break;
			}
		}
					
						
		
		fprintf(f2,"Case #%d: %d %d\n",c,ac,bc);
		c++;
	}
	fclose(f1);
	fclose(f2);
	return 0;
}	 
				
		
		
