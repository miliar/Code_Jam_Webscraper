#include<iostream>
using namespace std;

struct POINT{
	int i,j, altitude;
	int nBasin;
	bool if_label;
	static int sink_num, sink_pointer;
	static int queue_num, queue_pointer;
	
	POINT & operator=(POINT & p){
		i = p.i;
		j = p.j;
		altitude = p.altitude;
		nBasin = p.nBasin;
		if_label = p.if_label;
		return *this;
	}
};
int POINT::sink_num = 0;
int POINT::sink_pointer = 0;
int POINT::queue_num = 0;
int POINT::queue_pointer = 0;

struct TRANSLATION{
	char letter;
	bool if_char;
	static char current_letter;
};
char TRANSLATION::current_letter = 'a';


POINT map[102][102];
int H, W;


bool if_sink(int i, int j){
	if(map[i][j].altitude <= map[i-1][j].altitude &&
			map[i][j].altitude <= map[i+1][j].altitude &&
			map[i][j].altitude <= map[i][j-1].altitude &&
			map[i][j].altitude <= map[i][j+1].altitude)
		return true;
	return false;
}

bool if_flow(int i, int j, char dir)
//dir is for direction: n for north, s for south, e for east, w for west
{
	if(if_sink(i, j))
		return false;
	switch(dir){
	case 'n':
		if(i-1>=1 &&
			((j-1>=1 && map[i-1][j].altitude <= map[i][j-1].altitude) || j-1<1) &&
			((j+1<=W && map[i-1][j].altitude <= map[i][j+1].altitude) || j+1>W) &&
			((i+1<=H && map[i-1][j].altitude <= map[i+1][j].altitude) || i+1>H) )
			return true;
		return false;
	case 'w':
		if(j-1>=1 &&
			((i-1>=1 && map[i][j-1].altitude <  map[i-1][j].altitude) || i-1<1) &&
			((j+1<=W && map[i][j-1].altitude <= map[i][j+1].altitude) || j+1>W) &&
			((i+1<=H && map[i][j-1].altitude <= map[i+1][j].altitude) || i+1>H) )
			return true;
		return false;
	case 'e':
		if(j+1<=W &&
			((i-1>=1 && map[i][j+1].altitude <  map[i-1][j].altitude) || i-1<1) &&
			((j-1>=1 && map[i][j+1].altitude <  map[i][j-1].altitude) || j-1<1) &&
			((i+1<=H && map[i][j+1].altitude <= map[i+1][j].altitude) || i+1>H) )
			return true;
		return false;
	case 's':
		if(i+1<=H &&
			((i-1>=1 && map[i+1][j].altitude <  map[i-1][j].altitude) || i-1<1) &&
			((j-1>=1 && map[i+1][j].altitude <  map[i][j-1].altitude) || j-1<1) &&
			((j+1<=W && map[i+1][j].altitude <  map[i][j+1].altitude) || j+1>W) )
			return true;
		return false;
	}
	return false;
}


int main()
{
	int T;
	POINT sink[10000];
	POINT queue[10000];
	TRANSLATION translation[26];
	const int EDGE = 20000;
	
	for(int i=0; i<102; i++)
		for(int j=0; j<102; j++){
			map[i][j].i = i;
			map[i][j].j = j;
		}
	
	cin>>T;
	for(int t=1; t<=T; t++){
		cin>>H>>W;
		for(int i=1; i<=H; i++)
			map[i][0].altitude = map[i][W+1].altitude = EDGE;
		for(int j=1; j<=W; j++)
			map[0][j].altitude = map[H+1][j].altitude = EDGE;
		
		POINT::sink_num = POINT::sink_pointer = 0;
		TRANSLATION::current_letter = 'a';
		memset(translation, 0, sizeof(translation));
		
		for(int i=1; i<=H; i++){
			for(int j=1; j<=W; j++){
				cin>>map[i][j].altitude;
				map[i][j].if_label = false;
			}
		}
		
		for(int i=1; i<=H; i++){
			for(int j=1; j<=W; j++){
				if(if_sink(i,j)){
					sink[POINT::sink_num ++] = map[i][j];
				}
			}
		}
		
		for(POINT::sink_pointer = 0; POINT::sink_pointer < POINT::sink_num; POINT::sink_pointer ++){
			POINT::queue_num = POINT::queue_pointer = 0;
			
			queue[POINT::queue_pointer] = sink[POINT::sink_pointer];
			map[queue[POINT::queue_pointer].i][queue[POINT::queue_pointer].j].if_label = true;
			map[queue[POINT::queue_pointer].i][queue[POINT::queue_pointer].j].nBasin = POINT::sink_pointer;
			
			while(POINT::queue_pointer <= POINT::queue_num){
				if(queue[POINT::queue_pointer].i-1>=1 && !map[queue[POINT::queue_pointer].i-1][queue[POINT::queue_pointer].j  ].if_label &&
						if_flow(queue[POINT::queue_pointer].i-1, queue[POINT::queue_pointer].j  , 's')){
					queue[++ POINT::queue_num] = map[queue[POINT::queue_pointer].i-1][queue[POINT::queue_pointer].j  ];
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].if_label = true;
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].nBasin = POINT::sink_pointer;
				}
				if(queue[POINT::queue_pointer].j-1>=1 && !map[queue[POINT::queue_pointer].i  ][queue[POINT::queue_pointer].j-1].if_label &&
						if_flow(queue[POINT::queue_pointer].i  , queue[POINT::queue_pointer].j-1, 'e')){
					queue[++ POINT::queue_num] = map[queue[POINT::queue_pointer].i  ][queue[POINT::queue_pointer].j-1];
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].if_label = true;
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].nBasin = POINT::sink_pointer;
				}
				if(queue[POINT::queue_pointer].j+1<=W && !map[queue[POINT::queue_pointer].i  ][queue[POINT::queue_pointer].j+1].if_label &&
						if_flow(queue[POINT::queue_pointer].i  , queue[POINT::queue_pointer].j+1, 'w')){
					queue[++ POINT::queue_num] = map[queue[POINT::queue_pointer].i  ][queue[POINT::queue_pointer].j+1];
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].if_label = true;
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].nBasin = POINT::sink_pointer;
				}
				if(queue[POINT::queue_pointer].i+1<=H && !map[queue[POINT::queue_pointer].i+1][queue[POINT::queue_pointer].j  ].if_label &&
						if_flow(queue[POINT::queue_pointer].i+1, queue[POINT::queue_pointer].j  , 'n')){
					queue[++ POINT::queue_num] = map[queue[POINT::queue_pointer].i+1][queue[POINT::queue_pointer].j  ];
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].if_label = true;
					map[queue[POINT::queue_num].i][queue[POINT::queue_num].j].nBasin = POINT::sink_pointer;
				}
				
				POINT::queue_pointer ++;
			}
		}
		
		cout<<"Case #"<<t<<':'<<endl;
		
		for(int i = 1; i <= H; i++){
			for(int j = 1; j <  W; j++){
				if(translation[map[i][j].nBasin].if_char)
					cout<<translation[map[i][j].nBasin].letter<<' ';
				else{
					translation[map[i][j].nBasin].letter = TRANSLATION::current_letter ++;
					translation[map[i][j].nBasin].if_char = true;
					cout<<translation[map[i][j].nBasin].letter<<' ';
				}
			}
			if(translation[map[i][W].nBasin].if_char)
				cout<<translation[map[i][W].nBasin].letter<<endl;
			else{
				translation[map[i][W].nBasin].letter = TRANSLATION::current_letter ++;
				translation[map[i][W].nBasin].if_char = true;
				cout<<translation[map[i][W].nBasin].letter<<endl;
			}
		}	
	}
	return 0;
}
