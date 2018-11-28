#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<list>
#include<sstream>
#include<utility>
#include<string>
using namespace std;

int main()
{
	char dummy,ch,str[105];
	long t,n,o[101],b[101],i,j,k,v,time,obfr,bbfr,cas=0/*,OH[102],BH[102]*/,ot,bt;
//	freopen("A-large.in","r",stdin);
 //   freopen("A-small-attempt9.out","w",stdout);
	scanf("%ld",&t);
	while(t--)
	{
		scanf("%ld%c",&n,&dummy);
		for(i=0,j=0,k=0;i<n;i++)
		{
			scanf("%c%ld%c",&ch,&v,&dummy);
			if(ch=='O'){o[j++]=v;}
			else{b[k++]=v;}
			str[i]=ch;
		}
		str[i]='\0';
//		for(i=1;i<=100;i++){OH[i]=0;BH[i]=0;}
		time=bt=ot=0;
		j=k=0;
		obfr=bbfr=1;
		if(str[0]=='O')
		{
			time+=abs(1-o[j])+1;
//			OH[o[j]]=1;
			obfr=o[j];
			ot+=abs(1-o[j])+1;
			j++;			
		}
		else
		{
			time+=abs(1-b[k])+1;
//			BH[b[k]]=1;
			bbfr=b[k];
			bt+=abs(1-b[k])+1;
			k++;			
		}
		for(i=1;i<n;i++)
		{
			if(str[i]=='O'&&str[i-1]=='B')
			{
				if(bt>=abs(obfr-o[j])/*&&OH[o[j]]==0*/)
				{
					time++;
		   // 		OH[o[j]]=1;
					obfr=o[j];
					ot=1;
				}
				else// if(OH[o[j]]==0)
				{
					time+=abs(obfr-o[j])-bt+1;
	//				OH[o[j]]=1;
                    ot=abs(obfr-o[j])-bt+1;
					obfr=o[j];					
				}
				bt=0;
				j++;
			}
			else if(str[i]=='B'&&str[i-1]=='O')
			{
				if(ot>=abs(bbfr-b[k])/*&&BH[b[k]]==0*/)
				{
					time++;
		//			BH[b[k]]=1;
					bbfr=b[k];
					bt=1;
				}
				else// if(BH[b[k]]==0)
				{
					time+=abs(bbfr-b[k])-ot+1;
			//		BH[b[k]]=1;
					bt=abs(bbfr-b[k])-ot+1;
					bbfr=b[k];					
				}
				ot=0;
				k++;
			}
			else
			{
				if(str[i]=='O')
				{
		//			if(OH[o[j]]==0)
		//			{
						time+=abs(obfr-o[j])+1;
		//				OH[o[j]]=1;
						ot+=abs(obfr-o[j])+1;
						obfr=o[j];						
		//			}
					j++;
				}
				else
				{
		//			if(BH[b[k]]==0)
		//			{
						time+=abs(bbfr-b[k])+1;
		//				BH[b[k]]=1;
						bt+=abs(bbfr-b[k])+1;
						bbfr=b[k];						
		//			}
					k++;
				}
			}
		}
		printf("Case #%ld: %ld\n",++cas,time);
	}
	return 0;
}