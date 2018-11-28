#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Data{
	double ben;
	double end;
	double speed;
};
int comp(const void*a,const void*b){
	if (((Data*)a)->speed > ((Data*)b)->speed){
		return 1;
	}else return -1;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;

	for(int t = 0; t < T; ++ t){
		int X,S,R,ti,N;
		cin>>X>>S>>R>>ti>>N;
		double ss = 0;
		double st = ti;
		int ben[1000],end[1000],speed[1000];
		for(int i = 0; i < N; ++ i){
			cin>>ben[i]>>end[i]>>speed[i];
		}
		double _ben[3000],_end[3000],_speed[3000];
		int N_ = 0;
		for(int i = 0; i < N; ++ i){
			if (i == 0){
				if (ben[i] > 0){
					_ben[N_] = 0;
					_end[N_] = ben[i];
					_speed[N_] = 0;
					++ N_;
				}
				_ben[N_] = ben[i];
				_end[N_] = end[i];
				_speed[N_] = speed[i];
				++ N_;
			}else{
				if (ben[i] > end[i - 1]){
					_ben[N_] = end[i - 1];
					_end[N_] = ben[i];
					_speed[N_] = 0;
					++ N_;
				}
				_ben[N_] = ben[i];
				_end[N_] = end[i];
				_speed[N_] = speed[i];
				++ N_;
			}
		}
		if (end[N - 1] < X){
				_ben[N_] = end[N - 1];
				_end[N_] = X;
				_speed[N_] = 0;
				++ N_;
		}
		Data data[3000];
		for(int i = 0; i < N_; ++ i){
			data[i].ben = _ben[i];
			data[i].end = _end[i];
			data[i].speed = _speed[i];
		}
		int size = sizeof(data);
		qsort(data,N_,sizeof(Data),comp);
		for(int i = 0; i < N_; ++ i){
			_ben[i] = data[i].ben;
			_end[i] = data[i].end;
			_speed[i] = data[i].speed;
		}
		for(int i = 0; i < N_; ++ i){
			double temp;
			if (st > 0){
				temp = (_end[i] - _ben[i])/(_speed[i] + R);
				if (temp > st){
					temp = st + ((_end[i] - _ben[i] - (_speed[i] + R) * st)/(_speed[i] + S));
				}
				st -= temp;
			}else{
				temp =  (_end[i] - _ben[i])/(_speed[i] + S);
			
			}
			ss += temp;
		}
		cout<<"Case #"<<t+1<<": ";
		printf("%.10lf",ss);
		cout<<endl;
	}

	return 0;
}