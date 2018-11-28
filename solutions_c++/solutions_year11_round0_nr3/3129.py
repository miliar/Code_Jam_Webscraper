#include <iostream>
#define debug 0
int N;
int vals[1010];

using namespace std;

int count(int x)
{
	int t=1;
	int pos=N-1;
	int tot0=0, tot1=0;
	int count0=0;
	int count1=0;
	while(pos>=0)
	{
		if(debug)
		{
			cout << "count: t=" << t << ", pos=" << pos << ", val = " << vals[pos] << endl;
			cout << "count0 = " << count0 << ", count1 = " << count1 << ", tot0=" << tot0 << ", tot1=" << tot1<< endl;
		}
		if(x&t) {
			tot1+=vals[pos];
			count1=count1^vals[pos];
		} else {
			tot0+=vals[pos];
			count0=count0^vals[pos];
		}
		t=t<<1;
		pos--;
	}
	if (count0==count1)
		return max(tot1, tot0);
	return -1;
}

void process(int t)
{
	int tt = 1<<N;
	int maxret=-1;
	if(debug)
		cout << "Proces: tt=" << tt << ", N=" << N << endl;
	for(int x = 1; x<tt/2; x++)
	{
		if(debug)
			cout << "Going to count for x = " << x << endl;
		int ret = count(x);
		if(ret>0) maxret = max(maxret, ret);
		if(debug)
			cout << "ret = " << ret << ", maxret = " << maxret << endl;
	}
	if (maxret > 0)
		cout << "Case #" << t << ": " << maxret << endl;
	else
		cout << "Case #" << t << ": NO" << endl;
}

int main (int argc, char * const argv[]) {
	int T;
	cin >> T;
	for(int i=0;i<T;i++)
	{
		
		cin >> N;
		for(int j=0;j<N;j++)
			cin >> vals[j];
		process(i+1);
		
	}
	return 0;
}
