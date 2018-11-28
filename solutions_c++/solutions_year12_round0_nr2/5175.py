#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;

	int ans[100];

	for(int i=0; i<T; i++)
	{
		int N, S, p;
		cin>>N>>S>>p;

		int arr[3];
		for(int j=0; j<N; j++)
			cin>>arr[j];

		int a[3][3];
		//creating perfect solutions for all the googlers
		for(int j=0; j<N; j++)
		{
			int temp = arr[j]/3;
			if(temp*3 == arr[j])
				a[j][0]=a[j][1]=a[j][2]=temp;
			else
				if(temp*3 +1 == arr[j])
				{
					a[j][0]=a[j][1]=temp;
					a[j][2]=temp+1;
				}
				else
				{
					a[j][0]=temp+0;
					a[j][1]=temp+1;
					a[j][2]=temp+1;
				}
		}

		int num =0,s=0;

		//to count the number of cases satisfied
		for(int j=0; j<N; j++)
			//if p is equal to a[j][0] or lesser than that then num++
			if(p <= a[j][0])
				num++;
			else
			{
				//if p is one greater than a[j][0]
				if(p == a[j][0] +1)
				{
					//if a[j][0] is one less than a[j][2] then p is =a[j][2]
					//else then a surprise case is made if a[j][0] and a[j][2] are equal
					if(a[j][0]+1 == a[j][2])
						num++;
					else
						if(a[j][2]!=10 && a[j][0]!=0)
						{
							a[j][0]--;
							a[j][2]++;
							s++;
							if(s<=S)
								num++;
						}
				}
				else
				{
					//if p is one greater than a[j][0] by 2
					if(p == a[j][0] +2)
					{
						//if a[j][0] is same as a[j][2] then no cases are possible
						//else then a surprise case is made if a[j][1] and a[j][2] are equal
						if(a[j][0] == a[j][2])
						{
							;
						}
						else
							if(a[j][1] == a[j][2] && a[j][2]!=10 && a[j][1]!=0)
							{
								a[j][1]--;
								a[j][2]++;
								s++;
								if(s<=S)
									num++;
							}
					}
				}
			}

		ans[i] = num;
	}

	for(int i=0; i<T; i++)
		cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;

	return 0;
}