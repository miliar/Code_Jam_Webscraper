#include <iostream>
#include <stack>
#include <utility>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <utility>


using namespace std;

int T;

#define mx 1006

#define idf pair<int, double>


double W,H;
int n;

double px[mx];
double py[mx];
double px2[mx];
double py2[mx];
double rd[mx]; 
double h[2][mx];
double rs[2][mx];
double ls[2][mx];
idf hc[mx];

bool comp(double a, double b)
{
	return a > b;
}

bool comp2(idf a, idf b)
{
	return a.second > b.second;
}



int main()
{
	cin >> T;
	for(int ti = 1; ti <= T; ti++)
	{
		cin >> n >> W >> H;
		for(int i=0;i<n; i++){
			cin >> rd[i];
			rd[i] += 0.01;
			hc[i].first = i;
			hc[i].second = rd[i];
		}
		
		
		sort(rd, rd+n, comp);
		sort(hc, hc+n, comp2);
		int pid = 1;
		int np = 0;
		px[0] = py[0] = 0;
	
		h[0][0] = rd[0];
		rs[0][0] = rd[0];
		ls[0][0] = 0;
		np = 1;
		double lf = rs[0][0];
		for(int i = 1; i< n; i++)
		{
			if(pid>=n)break;
			if(lf+rd[pid] < W){
				px[pid] = lf+rd[pid];
				py[pid] = 0;
			//	printf("1px: %lf py:%lf rd:%lf\n", px[pid], py[pid], rd[pid]);
				lf = px[pid]+rd[pid];
				h[0][np] = rd[pid];
				rs[0][np] = px[pid]+min(rd[pid], W-px[pid]);
				ls[0][np] = px[pid]-rd[pid];
				np++;
				pid++;
			}else{
				break;
			}
		}
		if(rs[0][np-1] < W)rs[0][np-1] = W-0.001;
		while(pid < n)
		{
			np--; 
			int np2 = 0;
			px[pid] = W-0.0001;
			py[pid] = h[0][np]+rd[pid];
		//	printf("2px: %lf py:%lf rd:%lf\n", px[pid], py[pid], rd[pid]);
			h[1][np2] = py[pid]+rd[pid];
			rs[1][np2] = W- 0.001;
			ls[1][np2] = px[pid]-rd[pid];
			double rg = px[pid]-rd[pid];
			np2++;
			pid++;
			if(pid>=n)break;
			while(pid < n && rg > 0)
			{
				if(rg - rd[pid]  > 0)
				{
					px[pid] = rg-rd[pid];
					rg = px[pid] - rd[pid];
					double ch = h[0][np];
					while(np> 0 && rg < ls[0][np]){
						np--;		
						ch = max(ch, h[0][np]);
					}
					py[pid] = ch+rd[pid];
			//		printf("3px: %lf py:%lf rd:%lf\n", px[pid], py[pid], rd[pid]);
					rs[1][np2] = ls[1][np2-1];
					ls[1][np2] = px[pid]-rd[pid];
					h[1][np2] = py[pid]+rd[pid];
					np2++;
					pid++;
				}
				else
				{
					break;
				}
			}
			if(pid>=n)break;
			np2 --;
			np = 0;
			px[pid] = 0;
			py[pid] = h[1][np2]+rd[pid];
		//	printf("4px: %lf py:%lf rd:%lf\n", px[pid], py[pid], rd[pid]);
			h[0][np] = py[pid]+rd[pid];
			rg = rs[0][np] = rd[pid];
			ls[0][np] =0;
			np++;
			pid++;
			if(pid>=n)break;
			while(pid < n && rg < W)
			{
				if(rg + rd[pid]  < W)
				{
					px[pid] = rg+rd[pid];
					rg = px[pid] + rd[pid];
					double ch = h[1][np2];
					while(np2> 0 && rg > rs[1][np2]){
						np2--;		
						ch = max(ch, h[1][np2]);
					}
					py[pid] = ch+rd[pid];
			//		printf("5px: %lf py:%lf rd:%lf\n", px[pid], py[pid], rd[pid]);
					ls[0][np] = rs[0][np-1];
					rs[0][np] = px[pid]+rd[pid];
					h[0][np] = py[pid]+rd[pid];
					np++;
					pid++;
				}
				else
				{
					break;
				}
			}
			rs[0][np-1] = W-0.001;
		}			
	
		for(int i=0; i<n; i++){
			int pos = hc[i].first;
			px2[pos] = px[i];
			py2[pos] = py[i];
		}
		

		cout << "Case #"<<ti<<":";
		cout.precision(5);
 		cout.setf(ios::fixed,ios::floatfield);
			
		for(int i=0; i<n; i++){
			cout <<" "<< px2[i] << " " << py2[i];
			if(px[i] > W || py[i] > H)cout<<"!!";
		} 
		cout << endl;
	}	
	return 0;
}
