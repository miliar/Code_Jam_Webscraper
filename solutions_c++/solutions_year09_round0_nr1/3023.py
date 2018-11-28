
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string.h>
#include <cstring>
#include <cstdio>


using namespace std;

int main()
{
        int l,d,n,ans;
	char b[15][27];
        char temp[27];
        char a[5000][16],t[500][421];
        int j = 0, k ,p[15];
	freopen("./A-large.in","r",stdin);
	freopen("./A-large.out","w",stdout);
	
	
	scanf("%d %d %d",&l,&d,&n);
	for (int i = 0; i<d; i++)
	{
		scanf("%s",a[i]);
	}
	/*cout<<"The words in the alien dictionary are : \n";
	for (int i = 0; i<d; i++)
	{
		printf("%s\n",a[i]);
	}*/
	for(int i = 0;i<n;i++)
	{
            scanf("%s",t[i]);
    	}
    	/*cout<<"The test string are : \n";
    	for(int i = 0;i<n;i++)
	{
            printf("%s\n",t[i]);
    	}*/
        for ( int z = 0; z<n ; z++)
        {
    		cout<<"Case #"<<z+1<<": ";
                    j=0;
    		for ( int i = 0; i < strlen(t[z]); i++ )
    		{
                            
    			if( t[z][i] == '(' )
    			{
    			    i++;
    			    
    			    for( k = 0; t[z][i] != ')' ; k++ )
    			    {
    				 temp[k] = t[z][i];
    				 i++;
    			    }
    			    temp[k] = '\0';
    			    strcpy(b[j++],temp);
    			    
    			}
    			else
    			{
    			    b[j][0] = t[z][i];
    			    b[j][1] = '\0'; 
    			    j++;
    			}
    		}
    		char x[5000][16];
    		for(int i=0;i<d;i++)
    		{
                    strcpy(x[i],a[i]);
            }
    	    char tmp[5000][16];
    	    int g1,g2=d;
            for(int i=0;i<l;i++)
            {
                    
                    g1=0;
                    for(int j=0;j<strlen(b[i]);j++)
                    { 
                            for(int k=0;k<g2;k++)
                            {
                                    if(x[k][i]==b[i][j])
                                    {
                                                        strcpy(tmp[g1],x[k]);
                                                        g1++;
                                    }
                            }
                            
                    }
                    for(int k=0;k<g1;k++)
                            {
                                    strcpy(x[k],tmp[k]);
                            }
                            g2=g1;
            }
            cout<<g1<<endl;
	}
    
	    /*cout << endl;
	    for( int i = 0; i < 15; i++ )
	    {
		    cout << b[i];
		 cout << endl;
	    }*/
	return 0;
}
