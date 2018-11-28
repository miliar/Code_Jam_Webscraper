#include<iostream>
using namespace std;
int main()
{
	long long cases,bad,surp,ar[105][3],gog,sum[105],grtr,les,cs=0,a;
	
	cin>>cases;
	while(cases--)
	{
		char abc[105];
	    for(int i=0;i<105;i++)
	    {
	    	abc[i]='0';
    	//	cout<<abc[i]<<" ";
    	}
		cs++;
		cin>>gog>>surp>>bad;
		for(int i=0;i<gog;i++)
		cin>>sum[i];
		for(int i=0;i<gog;i++)
		{
			a=sum[i];
			ar[i][0]=a/3;
			a-=ar[i][0];
			ar[i][1]=a/2;
			a-=ar[i][1];
			ar[i][2]=a;
                    //  cout<<ar[i][0]<<" "<<ar[i][1]<<" "<<ar[i][2]<<endl;
		}
		grtr=0;
		les=0;
		for(int i=0;i<gog;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(ar[i][j]>=bad)
				{
					abc[i]='>';//cout<<ar[i][j]<<" ";
					grtr++;
					break;
				}
			}		
	}
	
			for(int i=0;i<gog;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(ar[i][j]==(bad-1)&&abc[i]!='>'&&sum[i]>=(3*bad-4)&&sum[i]>0)
				{
					abc[i]='<';
					les++;//cout<<ar[i][j]<<endl;
					break;
				}
			}		
		}
          /*     for(int i=0;i<gog;i++)
               {
        cout<<ar[i][0]<<" "<<ar[i][1]<<" "<<ar[i][2]<<" "<<abc[i]<<endl;
                } 
               cout<<"grtr="<<grtr<<" surp="<<surp<<" les="<<les<<endl;
                 cout<<"bad="<<bad<<endl;*/
		if(les>=surp)
		cout<<"Case #"<<cs<<": "<<(surp+grtr)<<endl;
	//	printf("Case #%lld: %lld\n",cs,(surp+grtr));
		else
		cout<<"Case #"<<cs<<": "<<(les+grtr)<<endl;
	//	printf("Case #%lld: %lld\n",cs,(les+grtr));
}
}
