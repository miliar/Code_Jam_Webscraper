// code03.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

long ch(char *b){
	long n,m,i = 0, s= 0, e = 0, k, u, w = 0, aa, ts,zz, zc;
	n = atoi(b);
	while(b[i]!=' '){i++;};
	m = atoi(&b[i+1]);
	i = n;
	while(i>0){i = i / 10; e++;}; // e 는 자리수 1의자리는1, 10의자리는2, ....
	i = 0;
	char *l = new char[e+1];
	char *tmp = new char[e+1];
		//sprintf(l,"%d",n);
	if(e == 1){delete[] l;delete[] tmp;	return 0;}
	
	for (i = n; i <= m; i++){
		long *qq = new long[e+1];
		memset(qq,0,e+1);
		for(k = 0; k < e-1; k++){

					sprintf(l,"%d",i);
					w = 0;
					memset(tmp,0,e+1);
					//cout<<"사이즈 : "<<e<<endl;
					//cout<<"k값    : "<<k<<endl;
					//cout<<l<<endl;

			for (u = 0; u <= k; u++){
				tmp[u] = l[u];
				//cout<<tmp<<endl;
			}
			//cout<<"temp : "<<tmp<<endl;
			for (u = 0; u < e-k-1; u++){		//앞의 1을 제외한 00   숫자 3-1 = 2
				l[u] = l[u+k+1];				//  
			}
			u--;
			//cout<<"u 값 : "<<u<<endl;
			for (aa = 0; aa <= k; aa++){
				l[u+1+aa] = tmp[aa];
				//w+=1;
			}
			
			ts = atoi(l);
			

			if(ts<=m&&ts>=n&&ts>i){
				zc = 0;
				for(zz = 0; zz <= k; zz++){
					if(qq[zz]==ts){
						zc++;
					}
				}

				if(zc<1){
					qq[k] = ts;
				
					s++;}

			}
			//cout<<l<<endl;
		}
			
	delete[] qq;
	}
		
	



	delete[] tmp;
	delete[] l;
	return s;
}

int _tmain(int argc, _TCHAR* argv[])
{

	char buf[1000];
	long a, b;
	ifstream fin;
	ofstream fout;
	fin.open("C-large.in");
	fout.open("output.txt");
	
	fin.getline(buf,1000);
	a = atoi(buf);

	for(long c = 0 ; c < a ; c++){
		fin.getline(buf,1000);

		b = ch(buf);	// 계산

		fout<< "Case #"<<c+1<<": "<<b << endl;
	}

	fin.close();
	fout.close();


	return 0;
}
