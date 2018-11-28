#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int note;
	cin>>note;
	for(int caseno=1;caseno<=note;caseno++)
	{
		int n;
		cin>>n;
                int min=-1;
		int no=0;
		int ans=0;
		int xorans=0;
		for(int i=1;i<=n;i++)
		{
			cin>>no;
			ans+=no;
			if(min==-1||min>no)
				min=no;
			xorans^=no;

		}
		if(xorans==0)
			cout<<"Case #"<<caseno<<": "<<ans-min<<endl;
		else
			cout<<"Case #"<<caseno<<": "<<"NO"<<endl;

	}
}
//3  0011
//5  0101
//6  0110
//---------
//14 1110     
//---------
//11 1011
//3  0011
//
//1 2 3 4 5 6 7 8 9
//
//0011
//2 - 0010|
//3 - 0011|
//4 - 0100|
//5 - 0101|   0000   0010
//12
//
