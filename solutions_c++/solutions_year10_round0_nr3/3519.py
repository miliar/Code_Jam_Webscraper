#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	ifstream in("a.in");
	ofstream out("out.out");
	int T,k,R,N,tot,j,ans=0;
	in>>T;
	for(int i=1 ; i<= T;i++)
	{
		in>>R>>k>>N;
		int *a=new int[N];
		tot=ans=0;
		for(j=0 ; j<N ;j++)in>>a[j]; 		
		j=0; 
		int s=0;
		while(R!=0)
		{
			tot+=a[j]; 
			if(tot<k)
			{
				if(j==N-1)j=0;
				else j++;

				if(s == j) 
				{	
					ans+=tot;
					tot=0;
					R--;
				}
				continue;
			}
			else
			{
				if(tot!=k) tot-=a[j];
				else if (j== N-1)j=0;
				else j++;
				ans+=tot;
				tot=0;
				R--;		
				s=j;
			}
		}
		out<<"Case #"<<i<<": "<<ans<<endl;
		delete a;
	}
	in.close();
	out.close();
	return 0;
}
