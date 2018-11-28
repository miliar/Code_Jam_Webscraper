#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;

int main(){

	string xau;
	int otime = 0, btime = 0;
	int ntest, tttest = 0 , n, a[201], b [201], c[201], d[201], danhdau[201], time[201];
	int i, j, h, k;
	int opost = 1, bpost = 1;
	
	ifstream fi;
	ofstream fo;
	fi.open("A-large.in",ios::in);
	fo.open("out.txt", ios::out);
	
	fi >> ntest;
	while(ntest--){
		tttest ++;
		otime = btime = 0;
		opost = bpost = 1;
		fi >> n;

		k = h = 0;
		for(i = 1; i <= n; i++){
			fi >> xau;
			if(xau == "O"){
				k++;
				fi >> a[k];
				b[k] = i;
			}
			if(xau == "B"){
				h++;
				fi >> c[h];
				d[h] = i;
			}
			danhdau[i] = 0;
			time[i] = 0;
		}
		
		danhdau[0] =1;
		i = j = 1;

		while(!danhdau[n]){
			if(i <= k){
				if(opost != a[i]){
					otime +=   abs(a[i] - opost);
					opost = a[i];
				}
				else{
					if(danhdau[b[i] - 1]){
						if(otime < time[b[i] - 1])
							otime = time[b[i] -1];
						otime++;
						danhdau[b[i]] = 1;
						time[b[i]] = otime;

						i++;
					}
				}
			}
			
			if(j <= h){
				if(bpost != c[j]){
					btime +=   abs(c[j] - bpost);
					bpost = c[j];
				}
				else{
					if(danhdau[d[j] -1]){
						if(btime < time[d[j] -1])
							btime = time[d[j] -1];
						btime++;
						danhdau[d[j]] = 1;
						time[d[j]] = btime;
						j++;
					}
				}
			}
			
		}
		 fo << "Case #" << tttest<< ": " << time[n] << endl;  
	}

	return 0;
}
