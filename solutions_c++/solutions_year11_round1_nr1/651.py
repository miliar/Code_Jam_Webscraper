#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int n_case;
 long long  int top_bound;
int p1,p2;

int main()
{
	freopen("in.txt","r",stdin); 
	ofstream  cout("out.txt");
	cin>>n_case;
	for(int i=0;i<n_case;i++)
	{
		cin>>top_bound>>p1>>p2;
		cout<<"Case #"<<i+1<<": ";
        if((p2==100&&p1!=100)||(p1!=0&&p2==0))
			cout<<"Broken"<<endl;
		else{
			int done=0;
			if(top_bound<100)
			{
				for(int t=1;t<=top_bound;t++)
					if(t*p1%100==0)
					{  done=1; break;}
			}
			else 
			   done=1;
			if(done)
				cout<<"Possible"<<endl;
			else cout<<"Broken"<<endl;
		}
	}
}