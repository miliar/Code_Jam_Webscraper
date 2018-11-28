#include<iostream>
#include<cmath>

using namespace std;


main()
{

	long long int T,L,P,C,count,num;

	cin >> T;	
	for(long long int l=0;l<T;l++)
	{
		cin >> L >> P >> C;
		count=0;

		while(P>L)
		{
			if(P%C > 0) P=1 + (P/C);
			else P=P/C;
			if(P>L) count++;
		}
		if(count==0)cout<<"Case #"<<l+1<<": "<<"0\n";
		else if(count==1)cout<<"Case #"<<l+1<<": "<<"1\n";
		else if(count==2)cout<<"Case #"<<l+1<<": "<<"2\n";
		else if(count >2) cout<<"Case #"<<l+1<<": "<<ceil(log2(count+1)) <<'\n';
	}
}	
				
				
