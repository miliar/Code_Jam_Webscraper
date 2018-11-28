#include <vector>
#include <iostream>
#include <string> 
#include <limits>

using namespace std;

int main()
{
	int T;
	cin>> T;

	

	for(int t = 0; t<T;++t) {
		int C;
		double D;
		cin>>C;
		cin>>D;
		vector<double> left(C, 0);
		vector<double> right(C, 0);
		vector<double> maxv(C, 0);
		for (int c = 0; c < C; ++c) {
			double P;
			double V;
			cin>>P;
			cin>>V;
			left[c] = P - (V-1)/2.0*D;
			right[c] = P + (V-1)/2.0*D;
			maxv[c] = (V-1)/2.0*D;
		}
		int i = 0;
		while (i < left.size()-1) {
			if (right[i] + D >= left[i+1] ) {
				double tomove = right[i] + D - left[i+1];
				if(maxv[i] > maxv[i+1]) {
					double tmp = maxv[i]-maxv[i+1];
					left[i+1] += min(tomove, tmp);
					right[i+1] += min(tomove, tmp);
					maxv[i+1] += min(tomove, tmp);
					tomove -= min(tomove, tmp);
				}
				else
				{
					double tmp = maxv[i+1]-maxv[i];
					left[i] -= min(tomove, tmp);
					right[i] -= min(tomove, tmp);
					maxv[i] += min(tomove, tmp);
					tomove -= min(tomove, tmp);
				}
				left[i+1] += tomove/2;
				right[i+1] += tomove/2;
				maxv[i+1] += tomove/2;
				left[i] -= tomove/2;
				right[i] -= tomove/2;
				maxv[i] += tomove/2;
				right[i] = right[i+1];
				maxv[i] = max(maxv[i], maxv[i+1]);
				for(int j = i+1; j<left.size()-1; ++j) {
					left[j] =left[j+1];
					right[j] =right[j+1];
					maxv[j] =maxv[j+1];
				}
				left.resize(left.size()-1);
				right.resize(left.size()-1);
				maxv.resize(left.size()-1);
				if(i>0) {
					--i;
				}
			}
			else
			{
				i++;
			}
		}

		double maximum = 0;
		for (int c = 0; c < left.size(); ++c) {
			maximum = max(maximum, maxv[c]);
		}
		cout<<"Case #"<<t+1<<": "<<maximum<<endl;
	}
}
