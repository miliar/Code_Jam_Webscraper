#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>
using namespace std;

int main(){
	string  xau, buf, cur;
	int len;
	char a['z' + 1]['z' +1], b['z' + 1]['z' + 1];
	int i, j, c, d, n, ntest, tttest = 0;
	ifstream fi;
	ofstream fo;
	fi.open("B-large.in", ios::in);
	
	fo.open("out.txt", ios::out);
	fi >> ntest;
	while(ntest--){
		tttest ++;
		fi >> c;
		memset(a, '@', sizeof(a));
		memset(b, '0', sizeof(b));

		for(i = 1; i <= c; i++){
			fi >> buf;
			a[buf[0]][buf[1]] = buf[2];
			a[buf[1]][buf[0]] = buf[2];
		}

		fi >> d;
		
		for(i =1; i <= d; i ++){
			fi >> buf;
			b[buf[0]][buf[1]] = '1';
			b[buf[1]][buf[0]] = '1';
		}

		fi >> n;
		fi >> xau;
		
		cur = "";
		
		for(i = 0; i <= n-1; i ++){
			cur = cur + xau[i];
			len = cur.length();
			
			if(i < 1)
				continue;
			else{
				if(a[cur[len -1]][cur[len -2]] != '@'){
					cur.replace(len-2, 2 , 1, a[cur[len -1]][cur[len -2]]);
				}
				
				len = cur.length();			
				for(j = 0; j < len -1; j++)
					if(b[cur[j]][cur[len - 1]] == '1')
						cur = "";
			}
		}
		len = cur.length();
		fo << "Case #" << tttest<<": [";
		for( int k = 0; k < len -1; k ++)
			fo << cur[k] << ", ";
		if(len >0)
			fo << cur[len-1];
		fo <<"]" <<endl;
	}

	return 0;
}
