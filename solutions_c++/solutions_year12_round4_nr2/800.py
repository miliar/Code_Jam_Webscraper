#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

typedef long long LL;

string tostr(double x) {
	char buf[20];
	sprintf(buf, "%.11f", x);
	size_t l=strlen(buf);
	while (l>2 && buf[l-2]!='.' && buf[l-1]=='0') {
		l--;
	}
	return string(buf,l);
}
double dist2(double x0,double y0,double x1,double y1) {
	double a=x1-x0;
	double b=y1-y0;
	return (a*a+b*b);
}
double touch(double x0,double y0,int r0,double x1,double y1,int r1) {
	double d=dist2(x0,y0,x1,y1);
	double r2=(r0+r1);
	r2=r2*r2;
	return d<r2;
}
int main() {
	int T;
	cin >> T;


	for (int tcase=1; tcase<=T; tcase++) {
		int N,W,H;
		cin>>N>>W>>H;

		vector<pair<int,int> > rs(N);
		for (int i=0;i<N; i++) {
			cin>>rs[i].first;
			rs[i].second=i;
		}
		sort(rs.begin(), rs.end(), greater<pair<int,int> >());
		vector<double> xs(N),ys(N);
		int i=0;
cerr<<"TCASE "<<tcase<<" W="<<W<<", H="<<H<<endl;
		while (i<N) {
			int r=rs[i].first;
			double xx=i==0? 0.0 : xs[i-1]+rs[i-1].first+r;//+0.0001
			if (xx<=W) {
				xs[i]=xx;
				ys[i]=0;
//				cerr<<"Placed(1) #"<<i<<" at ("<<xx<<",0)"<<endl;
				i++;
			} else {
				break;
			}
		}
		cerr<<"i="<<i<<" after step 1"<<endl;
		int atBottom=i;
		double nextx = W;
		while (i<N && nextx>0) {
			int r=rs[i].first;
			int y=H;
			bool t=false;
			for (int j=0; !t && j<atBottom; j++) {
				t=touch(nextx,y,r,xs[j],ys[j],rs[j].first);
			}
			if (!t) {
				xs[i]=nextx;
				ys[i]=y;
//				cerr<<"Placed(2) #"<<i<<" at ("<<nextx<<","<<y<<")"<<endl;
				if (i+1<N) {
					nextx=nextx-rs[i].first-rs[i+1].first; //000.1
				}
				i++;
			} else {
				break;					
			}
		}
		cerr<<"i="<<i<<" after step 2"<<endl;
		int randomStart = i;
//			bool placed = false;
//			while (!placed) {
restart:
		cerr<<"Starting random case "<<tcase<<" for "<<(N-i)<<" out of "<<N<<endl;
			i = randomStart;
			while (i<N) {
				int attempt=0; bool ok=false;
				double randx,randy;
				while (attempt<1000 && !ok) {
					int r = rs[i].first;
//					cerr<<" trying "<<randx<<","<<randy<<"...";
					randx=((double)rand() / RAND_MAX) * W;
					randy=((double)rand() / RAND_MAX) * H;
					bool t=false;
					for (int j=0; !t && j<i; j++) {
						t=touch(randx,randy,r,xs[j],ys[j],rs[j].first);
					}
					ok = !t;
					attempt++;
				}
				if (!ok) {
					goto restart;
				}
				cerr<<"Placed(3) #"<<i<<" at ("<<randx<<","<<randy<<")"<<endl;
				xs[i] = randx;
				ys[i] = randy;
				i++;
			}
			//ok!!!
//			}

		// validate
		bool err = false;
		if (i!=N) {
			cerr<<"ERROR i!=N";
			err=true;
		}
		for (int i=0; i<N; i++) {
			if(xs[i]<0) {
				cerr<<"ERROR xs["<<i<<"]min = "<<xs[i]<<endl;
				err=true;
			}
			if(xs[i]>W) {
				cerr<<"ERROR xs["<<i<<"]max = "<<xs[i]<<endl;
				err=true;
			}
			if(ys[i]<0) {
				cerr<<"ERROR ys["<<i<<"]min = "<<ys[i]<<endl;
				err=true;
			}
			if(ys[i]>H) {
				cerr<<"ERROR ys["<<i<<"]max = "<<ys[i]<<endl;
				err=true;
			}
			for (int j=0; j<N; j++) {
				if (j==i) {
					continue;
				}
				if (touch(xs[i],ys[i],rs[i].first,xs[j],ys[j],rs[j].first )){
					cerr<<"ERROR "<<i<<" touches "<<j<<":";
					cerr<<i<<"@("<<tostr(xs[i])<<","<<tostr(ys[i])<<") r="<<rs[i].first<<" ";
					cerr<<j<<"@("<<tostr(xs[j])<<","<<tostr(ys[j])<<") r="<<rs[i].first<<" ";
					cerr<<endl;
					err=true;
				}
			}
		}
		if (err) {
			exit(1);
		}



		vector<int> ids(N);
		for (int i=0; i<N; i++) {
			ids[rs[i].second] = i;
		}

		cout << "Case #" << tcase << ":";
		for (int i=0; i<N; i++) {
			cout<<" "<<tostr(xs[ids[i]])<<" "<<tostr(ys[ids[i]]);
		}
		cout<<endl;
	}


}