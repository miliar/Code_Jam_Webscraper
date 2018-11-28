#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <cstdio>
#include <cstdlib>


int turnTime;
int na,nb;

typedef struct TrainTime
{
    int begin;
	int end;
	bool ok;
} TrainTime;

TrainTime timea[105];
TrainTime timeb[105];


void sort( TrainTime* time,int size ){
	TrainTime temp;
	for( int h = 0; h < size; h++ ){
		for( int k = 0; k < size-h-1; k++ ){
			if( time[k].begin > time[k+1].begin ||
				( time[k].begin == time[k+1].begin && time[k].end > time[k+1].end) )
			{

				temp.begin = time[k].begin;
				temp.end = time[k].end;

				time[k].begin = time[k+1].begin;
				time[k].end = time[k+1].end;

				time[k+1].begin = temp.begin;
				time[k+1].end = temp.end;
			}
		}
	}
}



int main(int argc, char * argv[])
{
//	freopen( "input1","r",stdin );
	int n;
	int begin_h,begin_m,end_h,end_m;
	scanf( "%d",&n );
	for( int i = 0; i < n; i++ ){
		scanf( "%d",&turnTime );
		scanf( "%d%d",&na,&nb );

		for( int h = 0; h < na; h++ ){
			scanf( "%d:%d",&begin_h,&begin_m );
			scanf( "%d:%d",&end_h,&end_m );
			timea[h].begin = begin_h*60+begin_m;
			timea[h].end = end_h*60+end_m;
			timea[h].ok = false;
		}

		for( int h = 0; h < nb; h++ ){
			scanf( "%d:%d",&begin_h,&begin_m );
			scanf( "%d:%d",&end_h,&end_m );
			timeb[h].begin = begin_h*60+begin_m;
			timeb[h].end = end_h*60+end_m;
			timeb[h].ok = false;
		}

		sort( timea,na );
		sort( timeb,nb );

		int train_a,train_b;
		train_a = na;
		train_b = nb;
		for( int aa = 0; aa < na; aa++ ){
			for( int bb = 0; bb < nb; bb++ ){
				if( timeb[bb].ok == false && timea[aa].end+turnTime <= timeb[bb].begin ){
					train_b--;
					timeb[bb].ok = true;
					break;
				}
			}
		}
		for( int bb = 0; bb < nb; bb++ ){
			for( int aa = 0; aa < na; aa++ ){
				if( timea[aa].ok == false && timeb[bb].end+turnTime <= timea[aa].begin ){
					train_a--;
					timea[aa].ok = true;
					break;
				}
			}
		}
		std::cout<<"Case #"<<i+1<<": "<<train_a<<" "<<train_b<<std::endl;
		
	}
    return 0;
}


