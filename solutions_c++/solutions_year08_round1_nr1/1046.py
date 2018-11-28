#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<conio.h>
#include<map>

using namespace std;

int main()
{
    int T,N,i,t;
    
    fstream in("input.txt",ios::in);
    fstream out("out.txt",ios::out);
	
	in>>T;    
    cout<<"T"<<T<<endl;
    
    for(t=0;t<T;t++)
	{
		in>>N;
		cout<<"N"<<N<<endl;
		
		vector<int> a(N);
		vector<int> b(N);
		int temp1=0;
		
		for(i=0;i<N;i++)
		{
			in>>a[i];
			cout<<a[i]<<"\t";    
		}
		
		for(i=0;i<N;i++)
		{
			in>>b[i];
			cout<<b[i]<<"\t"; 
		}
		cout<<endl;
		
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		
		long sum=0;
		for(i=0;i<N;i++)
		{
			sum+=a[i]*b[N-1-i];
		}
		
		out<<"Case #"<<t+1<<": "<<sum<<endl;
	}
    in.close();
    out.close();
	system("pause");
	return 0;
}
