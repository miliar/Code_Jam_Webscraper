# include <iostream>
using namespace std;

__int64 num_boost,time_boost,num;
__int64 arr[1024];
__int64 tmp[1024];
__int64 first_boost,second_boost;

__int64 calc1()
{
	if(time_boost<=arr[first_boost])
		return (arr[first_boost+1]-arr[first_boost])/2;
	else if (time_boost>arr[first_boost+1])
		return 0;
	else
		return (arr[first_boost+1]-time_boost)/2;
}

__int64 calc2()
{
	__int64 x = calc1();
	first_boost = second_boost;
	x += calc1();
	return x;
}

void solve()
{
	if(num_boost==0)
	{
		cout<<arr[num]<<endl;
		return;
	}
	if(num_boost==1)
	{
		__int64 min = LLONG_MAX;
		for(__int64 i=0;i<num;++i)
		{
			first_boost = i;
			__int64 t=arr[num]-calc1();
			if(t<min)
				min=t;
		}
		cout<<min<<endl;
		return;
	}

	if(num_boost==2)
	{
		__int64 min = LLONG_MAX;
		for(__int64 i=0;i<num;++i)
		for(__int64 j=0;j<num;++j)
		{
			if(i==j)
				continue;
			first_boost = i;
			second_boost = j;
			__int64 t = arr[num] - calc2();
			if(t<min)
				min=t;
		}
		cout<<min<<endl;
		return;
	}
}

int main()
{
	//freopen("C:\\Documents and Settings\\bhuvan\\My Documents\\Visual Studio 2008\\Projects\\GCJ_Space_Emergency\\Debug\\a.in","r",stdin);
	__int64 T;
	cin>>T;
	for(__int64 i=0;i<T;++i)
	{
		__int64 c;
		cin>>num_boost>>time_boost>>num>>c;
		for(__int64 j=0;j<c;++j)
			cin>>tmp[j];
		arr[0] = 0;
		for(__int64 j=1;j<=num;++j)
			arr[j] = arr[j-1]+2*tmp[(j-1)%c];
		cout<<"Case #"<<i+1<<": ";
		solve();
	}
	return 0;
}
