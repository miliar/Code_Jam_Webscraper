#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(){
	int T;
	int N;

	FILE *fp;
	FILE *fin;
	fp = fopen("output.txt","w");
	if( fp == NULL ){
		printf("error\n");
		exit(1);
	}
	fin = fopen("input.txt","r");
	if( fin == NULL ){
		printf("error\n");
		exit(1);
	}
	//fscanf(fin,"%d\n",&T);
	
	cin >> T;
	
	for(int i=0 ; i<T ; i++ ){
		vector<int> O,B;
		vector< vector<int> > f;
		int state = 0;
		int sec = 0;
		int blue = 1;
		int orange = 1;
		int blueNext = -1;
		int orangeNext = -1;

		cin >> N;
		//fscanf(fin,"%d",&N);
		for(int j=0 ; j<N ; j++ ){
			char r;
			int p;
			vector<int> pair;
			cin >> r >> p;
			//fscanf(fin,"%d %d",&r,&p);

			if( r == 'O' ){
				pair.push_back(-1);
				pair.push_back(p);
				O.push_back(p);
			}else{
				pair.push_back(-2);
				pair.push_back(p);
				B.push_back(p);
			}
			f.push_back(pair);
		}
		
		while( state != N ){
			for(int j=state ; j<N ; j++ ){
				if( f[j][0] == -1 ){
					orangeNext = f[j][1];
					break;
				}
			}
			for(int j=state ; j<N ; j++ ){
				if( f[j][0] == -2 ){
					blueNext = f[j][1];
					break;
				}
			}
			bool flag = false;
			if( orangeNext < orange ){
				orange--;
			}else if( orangeNext > orange ){
				orange++;
			}else if( f[state][0] == -1 ){
				state++;
				flag = true;
			}
			if( state == N ){
				sec++;
				break;
			}
			if( blueNext < blue ){
				blue--;
			}else if( blueNext > blue ){
				blue++;
			}else if( f[state][0] == -2 && flag == false ){
				state++;
			}
			sec++;
		}
		//cout << "Case #" << (i+1) << ": " << sec << endl;
		fprintf(fp,"Case #%d: %d\n", i+1 , sec );
		
	}

	fclose(fp);
	fclose(fin);
}