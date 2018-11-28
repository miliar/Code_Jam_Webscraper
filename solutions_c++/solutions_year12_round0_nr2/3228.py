#include <iostream>
#include<string.h>
#include<algorithm>
#include<stdio.h>
using namespace std;

bool sorter(int a,int b)
{
	return (a>b);
}

int n,s,p;

void distribute(int hold[])
{
	int i;
	int mx=-100000000,mn = 100000000,k,l;
	for(i=0;i<3;i++)
	{
		if(hold[i] >mx)
		{
			mx = hold[i];
			k=i;
		}
		if(hold[i] <mn)
		{
			mn = hold[i];
			l=i;
		}
	}

	if(mn +2 > mx)
		return;

	int mid = (mx+mn)/2;

	hold[l] = mn + (mx - mid);
	hold[k] = mid;

	distribute(hold);
}

void maximize(int hold[])
{

	sort(hold,hold+3);

	if(hold[2] > hold[1])
        return;

    if(hold[1] ==0)
        return;

    hold[2] += 1;
    hold[1] -= 1;


}

void diff(int hold[105][3], int differ[])
{
	int mx;
	int i,j;
	for(i=0;i<n;i++)
	{
		mx = 0;
		for(j=0;j<3;j++)
		{
			if(hold[i][j] >= p)
			{
				mx = -1000000;
				break;
			}
			else
			{
					mx += hold[i][j];
			}
		}
		differ[i] = mx;
	}
}

void sortByNeed(int hold[105][3])
{
	int differ[105];
	int tmp[3],j,temp;
	bool swapped = false;
	diff(hold,differ);

	do
	{
		swapped = false;
		for(int i=1;i<n;i++)
		{
			if(differ[i-1] < differ[i])
			{
                temp = differ[i];
                differ[i] = differ[i-1];
                differ[i-1] = temp;


				for(j=0;j<3;j++)
					tmp[j] = hold[i][j];

				for(j=0;j<3;j++)
					hold[i][j] = hold[i-1][j];

				for(j=0;j<3;j++)
					hold[i-1][j] = tmp[j];

				swapped = true;
			}
		}
	}while(swapped);
}

int main()
{
    int i,t,k,j,cnt;
    int arr[105];

	int hold[105][3];

	freopen ("out.txt","w",stdout);
	freopen("in.txt","r",stdin);

    scanf("%d",&t);
    k=1;
    while(t--)
    {

        scanf("%d",&n);
        scanf("%d",&s);
        scanf("%d",&p);

		cnt=0;

		memset(hold,0,sizeof(int)*105*3);

		cout<<"Case #"<<k<<": ";

        for(i=0;i<n;i++)
		{
			cin>>arr[i];
		}

		sort(arr,arr+n);

		for(i=0;i<n;i++)
		{
			int h=arr[i];

			for(j=0;j<3;j++)
			{
				h = h - p;
				if(h> 0)
				{
					hold[i][j] = p;
				}
				else
				{
					hold[i][j] = h+p;
					break;
				}

			}

			distribute(hold[i]);

		}

		sortByNeed(hold);

        for(i=0;i<s;i++)
		{
			maximize(hold[i]);
		}

		for(i=0;i<n;i++)
		{
			for(j=0;j<3;j++)
			{
				if(hold[i][j] >= p)
				{
					cnt++;
					break;
				}
			}

		}



        cout<<cnt<<"\n";

        k++;
    }

    return 0;

}
