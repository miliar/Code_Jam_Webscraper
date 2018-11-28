#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long int lli;
typedef long double ld;
#define ZER(X) memset(X,0,sizeof(X));

struct interval{
	int B;
	int E;
	int w;
	bool operator < (const interval & other){
		return w<other.w;
	}
};

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){
		int X, S, R, N;
		ld t;
		cin >> X >> S >> R >> t >> N;
		vector<interval> vec;
		int position = 0;
		while(N--){
			interval in;
			cin >> in.B >> in.E >> in.w;
			in.w += S;
			if(position < in.B){
				interval in2;
				in2.B = position;
				in2.E = in.B;
				in2.w = S;
				vec.push_back(in2);
			}
			vec.push_back(in);
			position = in.E;
		}
		if(position < X){
			interval in2;
			in2.B = position;
			in2.E = X;
			in2.w = S;
			vec.push_back(in2);
		}

		sort(vec.begin(), vec.end());

		ld time=0;
		for(size_t i=0; i<vec.size(); ++i){
			int len=vec[i].E - vec[i].B;
			int w = vec[i].w;
			if(t>0)			{
				int speed = w-S+R;
				ld step_time = (ld)len/(speed);
				if(step_time > t){
					step_time = t;
					ld unfin = (ld)len - step_time*speed;
					time += step_time;
					time += unfin / w;
				}else{
					time += step_time;
				}
				t-=step_time;
			}
			else{
				time += (ld)len/w;
			}
		}

		/*for(size_t i=0; i<vec.size(); ++i){
			cerr << vec[i].B << " " << vec[i].E << " " <<vec[i].w << "\n";
		}*/

		cout.precision(16);
		cout << "Case #" << Case << ": " << time <<endl;
	}
	return 0;
}