#include<scc/simple.h>
int main() {
	int T(in);
	for (int t=1;  t<=T;  t++) {
		cout << "Case #" << t << ": ";
		long N(in);
		vlong  seq(N*2);   

		// read
		for (long n=0;  n<N*2;  n+=2) {
			char c(in); 
			if(c=='O')	seq[n]=0;
			else		seq[n]=1;
			cin >> seq[n+1];
		}

		vlong	pos	{1,1};
		vlong	time	{0,0};
		long	now	{0};


		// play
		for (long n=0;  n<N*2;  n+=2) {
			long  r=seq[n];
			long  p=seq[n+1];
			long  need_time=abs(pos[r]-p);
			if (time[r] + need_time >= now)
				now = time[r] + need_time;
			now ++;
			time[r] = now;
			pos[r] = p;
		}			
		cout << now;


		cout << endl;
	}
}
