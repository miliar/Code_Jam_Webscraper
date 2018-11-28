#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int digits(int x)
{
	int count=0;
	while(x>0)
	{
		count++;
		x/=10;
	}
	return count;
}

int main(){
    int d=0;
    int m=0,n=0;
    int result =0;
    int dig=0;
    cin>>d;
    //printf("%d\n",d);
    
    for(int i=0;i<d;i++)
    {
            cin>>n;
            cin>>m;
            result =0;
            for(int c=n;c<=m;c++){

            	int cur = c;
            	dig = digits(cur);
            	for(int d=dig;d>1;d--)
            	{
            		int f= cur%10;
//            		if(f!=0)
//            		{
            			cur/=10;
            			cur += f*pow(10,dig-1);
            			if(cur>=n && cur<=m)
            			{	if(cur>c)
            				{
            					result++;
      //      					cout<<"\nadded "<<c<<" and "<<cur<<" and n and m "<<n<<"  "<<m;
            				}
            			}
//            		}
            	}
            }
            
            printf("Case #%d: %d\n",i+1,result);
    }
    return 0;   
}

