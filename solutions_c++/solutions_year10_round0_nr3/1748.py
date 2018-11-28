#include<iostream>
using namespace std;
int go[1024], a[1024], fen[1024];
int beg, cycle, cbeg;

void find()
{
	int visit[1024];
	memset(visit, -1, sizeof(visit));
	int s = 0, cnt = 0;
	while(visit[s]==-1)
	{
		visit[s] = cnt;
		cnt++;
		s = go[s];
	}
	cbeg = s;
	beg = visit[s], cycle = cnt - visit[s]; 
	//cout<<cbeg<<" "<<beg<<" "<<cycle<<endl;
}

long long moni(int i, int len){
	if(len==0)return 0;
	return fen[i] + moni(go[i], len-1);
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	int runs, r, n, k, cas=1; 
	for(cin >> runs; runs > 0; runs--){
		cin >> r >> k >> n;
		for(int i = 0; i < n; i++)
		{
			cin >> a[i];
		}
		for(int i = 0; i < n; i++)
		{
			int sum = 0, j;
			fen[i] = 0;
			for(j = i; j < n + i; j++)
			{
				sum += a[j%n];
				if(k < sum)break;
				fen[i] += a[j%n];
			}
			go[i] = j % n;
			//cout<<i<<" "<<go[i]<<" "<<fen[i]<<endl;
		}

		find();
		long long ans = 0;
		if(r <= beg)
			ans = moni(0, r);
		else
		{
			ans += moni(0, beg);
			r -= beg;
			ans += (r/cycle)*moni(cbeg, cycle);
			ans += moni(cbeg, r%cycle);
		}
		cout<<"Case #"<<cas++<<": "<<ans<<endl;
	}
}