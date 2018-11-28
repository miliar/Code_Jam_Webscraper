#include<cstdio>
#include<sstream>
#include<iostream>
#include<cstdlib>

using namespace std;
int main()
{
	int tt,nn,ii,tm[5],p,c,kk,m,a,b,ff;
	string aa,bb="";	
		scanf("%d ",&tt);
		for(ii=0;ii<tt;ii++)
		{
			
			int incr=0;
			scanf("%d %d",&a,&b);
			for(ff=a;ff<=b;ff++)
			{
				bb="";
			stringstream ss,hh;
			ss<<ff;
			aa=ss.str();
			
			p=1;
			//for(kk=0;kk<aa.size();kk++)
				{
			
					for(c=0;c<aa.size();c++)
					{
						nn=(c+p)%(aa.size());
						if(bb=="" && aa[nn]=='0') ;
						else
						bb+=aa[nn];
						//cout<<bb<<endl;
						
							
					
					
			
					}
					//cout<<bb;
					//cout<<"a"<<aa;
					if( atoi(bb.c_str())<=b && atoi(aa.c_str()) != atoi(bb.c_str()) &&  atoi(bb.c_str())>=a ) incr++;
					p++;
				}
		}
		if(aa.size()==2) incr=incr/2;
		printf("Case #%d: %d\n",ii+1,incr);
		}
		return 0;
}
