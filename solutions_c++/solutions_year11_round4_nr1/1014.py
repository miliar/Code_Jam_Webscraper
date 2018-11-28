// round1-a.cpp : 定¨义?控?制?台?应畖用?程ì序ò的?入?口ú点?。￡
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include<vector>
#include<algorithm>
#include   <iomanip> 

using namespace std;

int T;
double S;
double wspeed;
double rspeed;
double t;
int N;

struct W{
	int b;
	int e;
	int s;
};

struct W walks[1001];

int cmp ( const void* p, const void* q){
	struct W* a = (struct W*)p;
	struct W*b = (struct W*)q;
	return a->s - b->s;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("D:\A-small-attempt0 (3).in");
	ofstream out("D:\A-small.out");
	
	cout <<fixed <<setprecision(10) ;
	out <<fixed <<setprecision(10) ;

	in >> T;
	int cur = 0;
	while(cur++ < T){
		int i,j;

		in >> S;
		in >> wspeed;
		in >> rspeed;
		in >> t;
		in >> N;

		double left = S;
		
		for(i=0;i<N;i++){
			in >> walks[i].b;
			in >> walks[i].e;
			in >> walks[i].s;
			left -= walks[i].e - walks[i].b;
		}
		int len = N;
		if( left > 0 ){
			walks[len].b = 0;
			walks[len].e = left;
			walks[len].s = 0; 
			len ++;
		}

		qsort(walks,len,sizeof(walks[0]),cmp);

		double curspeed = rspeed;
		double sum_t = 0;
		for( i=0;i<len;i++){
			double temp = (walks[i].e - walks[i].b)/(curspeed+walks[i].s);
			//cout << temp<<" "<<walks[i].e;
			if( temp <= t ){
				t -= temp;
				sum_t += temp;
			}
			else{
				sum_t+= t;
				double s1 = t*(curspeed+walks[i].s);
				sum_t += (walks[i].e - walks[i].b-s1)/(wspeed+walks[i].s);
				i ++;
				break;
			}
		}

		//cout <<"hello " <<sum_t<<" "<<t<<endl;

		for( i;i<len;i++){
			double temp = (walks[i].e - walks[i].b)/(wspeed+walks[i].s);
			//cout <<i<<" " <<sum_t<<" "<<t<<endl;
			sum_t += temp;
		}
		//cout << sum_t<<endl;
		out << "Case #"<<cur<<": "<<sum_t<<endl;

	}

	in.close();
	out.close();
	return 0;
}


