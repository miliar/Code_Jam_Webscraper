#include<iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void fileIO()
{
    freopen("input2.txt","r",stdin);
    freopen("output.txt","w",stdout);
}

main()
{
	int t,a,b,m;
	int i,j,k,l,max,digits[6],count,temp,ans,previous[10],iteration;
	fileIO();

	cin >> t;
	for(i=0;i<t;i++)
	{
		cin >> a >> b;
		ans=0;
		m=a;
		while(m<b)
		{
			j=m;
			count=0;
			iteration=0;
			while(j)
			{
				digits[count++]=j%10;
				j=j/10;
			}
			for(k=0;k<count-1;k++)
			{
				temp=digits[count-1];
				for(l=count-1;l>0;l--)
					digits[l]=digits[l-1];
				digits[0]=temp;
				temp=0;
//				cout << temp<< " ";
				for(l=count-1;l>0;l--)
					temp=(temp+digits[l])*10;
				
				temp=temp+digits[0];
				if(temp>m && temp <=b)
				{
//					cout << m << " " << temp << " " << count <<"\n";
					for(l=0;l<iteration;l++)
						if(temp==previous[l])
							break;
					if(l==iteration)
					{
						previous[iteration++]=temp;
						ans++;
					}
				}
			}
			m++;
			
		}
		cout << "Case #"<< i+1 << ": " << ans << "\n";
	}
	
}

