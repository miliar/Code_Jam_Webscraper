#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;
int main() {

	int T;

	cin >> T;
	for (int t=1;t<=T;t++) {
		int maxk=0;
		int R, C, D;
		cin >> R >> C >> D;
		vector<string> grid;
		for (int r=0;r<R;r++) {
			string row;
			cin >> row;
			grid.push_back(row);
		}

		for (int r=0;r<R;r++) {
			
			for (int c=0;c<C;c++) {

				for (int k=3;(c<=C-k)&&(r<=R-k);k++) {
					int r2=r+k;
					int c2=c+k;

					int rc2=r*2+k-1;
					int cc2=c*2+k-1;
					int rrr=0, ccc=0;
					for (int i=r;i<r2;i++) {
						//if (r==1 && c==1 && k==5) clog << (r*2-rc2) << endl;
						for (int j=c;j<c2;j++) {
							// is corner?
							if ((i==r) && ((j==c)||(j==c2-1))) continue;
							if ((i==r2-1) && ((j==c)||(j==c2-1))) continue;
							
							rrr+=(i*2-rc2)*(grid[i][j]-'0');
							ccc+=(j*2-cc2)*(grid[i][j]-'0');
						}
					}
					//if (r==1 && c==1 && k==5) clog << k << " " << r << " " << c << " " << rrr << " " << ccc << endl;
					if (rrr==0 && ccc==0) if (maxk<k) maxk=k;
				}
			}
		}

		cout << "Case #" << t << ": ";
		if (maxk==0) cout << "IMPOSSIBLE";
		else cout << maxk;
		cout << endl;
	}
}
/*
int main() {

	
	int T;

	cin >> T;
	double maxerr=0, minerr=1;
	for (int t=1;t<=T;t++) {


		

		int R, C, D;
		cin >> R >> C >> D;
		vector<string> grid;
		for (int r=0;r<R;r++) {
			string row;
			cin >> row;
			grid.push_back(row);
		}
		vector<vector<int> > totals;
		vector<vector<double> > horc, verc;
		int maxk=0;
		for (int r=0;r<R;r++) {
			if (r%10==0) clog << t << ": " << r << endl;
			int rowtotal=0;
			double rowc=0;
			totals.push_back(vector<int>());
			horc.push_back(vector<double>());
			verc.push_back(vector<double>());
			for (int c=0;c<C;c++) {
				int w=grid[r][c]-'0';

				if (rowtotal==0) rowc=c;
				else rowc=(rowtotal*rowc+w*c)/(rowtotal+w); // rows new horizontal centre of mass

				rowtotal+=w;
				if (r==0) {
					horc[r].push_back(rowc);
					totals[r].push_back(rowtotal);
					verc[r].push_back(r);
				}
				else {
					if (totals[r-1][c]==0) horc[r].push_back(rowc);
					else horc[r].push_back((rowc*rowtotal+horc[r-1][c]*totals[r-1][c])/(rowtotal+totals[r-1][c]));

					if (totals[r-1][c]==0) verc[r].push_back(r);
					else verc[r].push_back((r*rowtotal+verc[r-1][c]*totals[r-1][c])/(rowtotal+totals[r-1][c]));

					totals[r].push_back(totals[r-1][c]+rowtotal);

				}



				int K=min(r,c)+1;
				double totss, horss, verss, totsl, horsl, versl, totls, horls, verls;
				for (int k=3;k<=K;k++) {
					if (r+1==k || c+1==k) {
						totss=0;
						horss=0;
						verss=0;
					}
					else {
						totss=totals[r-k][c-k];
						horss=horc[r-k][c-k];
						verss=verc[r-k][c-k];
					}
					if (r+1==k) {
						totsl=0;
						horsl=0;
						versl=0;
					}
					else {
						totsl=totals[r-k][c];
						horsl=horc[r-k][c];
						versl=verc[r-k][c];
					}
					if (c+1==k) {
						totls=0;
						horls=0;
						verls=0;
					}
					else {
						totls=totals[r][c-k];
						horls=horc[r][c-k];
						verls=verc[r][c-k];
					}
					int gss=(grid[r-k+1][c-k+1]-'0'), gsl=(grid[r-k+1][c]-'0'), gls=(grid[r][c-k+1]-'0'), gll=(grid[r][c]-'0');
					double horcentre=totals[r][c]*horc[r][c]+totss*horss-totsl*horsl-totls*horls
						-gll*c-gls*(c-k+1)
						-gsl*c-gss*(c-k+1);
					horcentre/=(totals[r][c]+totss-totsl-totls
						-gll-gls
						-gsl-gss);
					//cout << horcentre << endl;
					double err1=1, err2=1;
					err1=abs(horcentre-(c-double(k-1)/2));
					if (err1<10E-8) {
						double vercentre=totals[r][c]*verc[r][c]+totss*verss-totsl*versl-totls*verls
							-gll*r-gls*r
							-gsl*(r-k+1)-gss*(r-k+1);
						vercentre/=(totals[r][c]+totss-totsl-totls
							-gll-gls
							-gsl-gss);
						err2=abs(vercentre-(c-double(k-1)/2));
						if (err2<10E-10) {
							if (maxk<k) {
								maxk=k;
								if (maxerr<err1) maxerr=err1;
								if (maxerr<err2) maxerr=err2;
								//cout << horcentre-(c-double(k-1)/2) << " " << ((horcentre-(c-double(k-1)/2))<10E-8) << " " << 10E-8 << endl;
								//cout << k << " " << r << " " << c << " " << horcentre << " " << vercentre << endl;
							}
						}
						else {
							if (minerr>err2) minerr=err2;
						}
					}
					else if (minerr>err1) minerr=err1;
				}
			}
		}
		
		cout << "Case #" << t << ": ";
		if (maxk==0) cout << "IMPOSSIBLE";
		else cout << maxk;
		cout << endl;
	}
	clog << "MAXERR: " << maxerr << endl;
	clog << "MINERR: " << minerr << endl;
	return 0;
}*/
/*for (int r=0;r<R;r++) {
			for (int c=0;c<C;c++) {
				printf("%3d ",totals[r][c]);
			}
			cout << endl;
		}
		cout << endl;
		for (int r=0;r<R;r++) {
			for (int c=0;c<C;c++) {
				printf("%3lf ",horc[r][c]);
			}
			cout << endl;
		}
		cout << endl;
		for (int r=0;r<R;r++) {
			for (int c=0;c<C;c++) {
				printf("%3lf ",verc[r][c]);
			}
			cout << endl;
		}*/

	/*
	cout << 1 << endl;
	cout << "500 500 1" << endl;
	for (int i=0;i<500;i++) {
		for (int i=0;i<500;i++) cout << "1";
		cout << endl;
	}*/