#include<iostream>
#include<fstream>
using namespace std;
//int data[1004];

int main()
{
	fstream f;
	f.open("a.txt");
	int t,cnt = 1,data;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		scanf("%d",&data);
		int temp =data;
		int min = data;
		int sum = data;
		for(int i =1;i<n;i++)
		{
			scanf("%d",&data);
			temp = temp^data;
			if(min>data)min=data;
			sum+=data;
		}
		if(temp==0)
			f<<"Case #"<<cnt++<<": "<<sum-min<<endl;
		else
			f<<"Case #"<<cnt++<<": NO"<<endl;
	}
	f.close();
	system("pause");
	return 0;
}
