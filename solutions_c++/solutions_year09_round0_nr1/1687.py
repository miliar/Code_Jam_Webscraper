#include <cstdio>
using namespace std;


int main()
{
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	char DS[5000][15];
	
	for(int i=0; i < D; i++)
	  scanf("%s ",DS[i]);
    
    for(int i=0; i < N; i++)
    {
    	int ML[15]={0};
    	char buf[2000];
    	scanf("%s ",buf);
    	bool bflag=false;
    	int l=0;
    	for(int j=0; buf[j]; j++)
    	{
    		if(buf[j] == '(')
    		{
    		bflag=true;
    		continue;
    		}
    		else if(buf[j] == ')')
    		{
    		bflag=false;
    		l++;
    		continue;	
    		}
    		
    		if(bflag == false)
    		{
    			ML[l]=1<<(buf[j]-97);
    			l++;
    		}
    		else
    			ML[l]=ML[l]|(1<<(buf[j]-97));
    	}
    	
    	int c=0;
    	for(int j=0; j < D; j++)
    	{
    		int k=0;
    		for(k=0; k < L; k++)
    		{
    			if( (1<<(DS[j][k]-97)) & ML[k])
    			continue;
    			else
    			break;
    		}
    	  	if(k == L)
    	  	c++;
    	}
    	
    	printf("Case #%d: %d\n",(i+1),c);
   }
    
   
	return 0;
}
